import contextlib
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import portfolio_plan as plan


class PlannerSafetyTests(unittest.TestCase):
    def setUp(self):
        self.items = plan.weeks((plan.ROOT / 'PORTFOLIO_PLAN.md').read_text())

    def test_missing_week_rejected(self):
        text = (plan.ROOT / 'PORTFOLIO_PLAN.md').read_text().replace('#### Week 2 -', '#### Week 99 -')
        with self.assertRaises(ValueError):
            plan.weeks(text)

    def test_closed_legacy_issue_skipped_without_writes(self):
        old = dict(number=2, title='Week 02: Older plan title', state='closed', body='Keep my notes')
        with patch.object(plan, 'gh_api', side_effect=[[old], []]) as api, contextlib.redirect_stdout(io.StringIO()):
            plan.apply([self.items[1]], 'issues', 'owner/repo')
        self.assertEqual(api.call_count, 2)
        self.assertTrue(all(len(call.args) == 1 for call in api.call_args_list))
        self.assertEqual(old['body'], 'Keep my notes')

    def test_duplicate_week_aborts_before_any_write(self):
        records = [dict(number=1, title='Week 01: A'), dict(number=2, title='Week 1: B')]
        with patch.object(plan, 'gh_api', side_effect=[records, []]) as api:
            with self.assertRaises(ValueError):
                plan.apply(self.items, 'issues', 'owner/repo')
        self.assertTrue(all(len(call.args) == 1 for call in api.call_args_list))

    def test_issue_creation_uses_milestone_number_and_real_criteria(self):
        item = self.items[1]
        milestone = dict(number=42, title=f"Week 02 - {item['title']}")
        created = dict(number=88, title=f"Week 02: {item['title']}")
        with patch.object(plan, 'gh_api', side_effect=[[], [milestone], created]) as api, contextlib.redirect_stdout(io.StringIO()):
            plan.apply([item], 'issues', 'owner/repo')
        payload = api.call_args.args[1]
        self.assertEqual(payload['milestone'], 42)
        self.assertIn(item['criteria'], payload['body'])
        self.assertIn('Both authentication tests pass', payload['body'])

    def test_rerun_skips_newly_created_milestone(self):
        item = self.items[0]
        created = dict(number=40, title=f"Week 01 - {item['title']}", state='open')
        with patch.object(plan, 'gh_api', side_effect=[[], created, [created]]) as api, contextlib.redirect_stdout(io.StringIO()):
            plan.apply([item], 'milestones', 'owner/repo')
            plan.apply([item], 'milestones', 'owner/repo')
        self.assertEqual(sum(len(call.args) == 2 for call in api.call_args_list), 1)

    def test_pr_not_confused_with_weekly_issue(self):
        self.assertIsNone(plan.existing_week([dict(title='Week 01: Change', pull_request={'url': 'example'})], 1))

    def test_missing_milestone_prevents_issue_write(self):
        with patch.object(plan, 'gh_api', side_effect=[[], []]) as api:
            with self.assertRaises(ValueError):
                plan.apply([self.items[0]], 'issues', 'owner/repo')
        self.assertTrue(all(len(call.args) == 1 for call in api.call_args_list))

    def test_preview_never_calls_github(self):
        with patch.object(sys, 'argv', ['portfolio_plan.py', '--kind', 'issues']), patch.object(plan, 'gh_api') as api, contextlib.redirect_stdout(io.StringIO()) as output:
            plan.main()
        api.assert_not_called()
        self.assertIn('Offline preview only', output.getvalue())


if __name__ == '__main__':
    unittest.main()
