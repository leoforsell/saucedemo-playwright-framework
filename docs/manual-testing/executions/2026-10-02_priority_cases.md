# Priority test execution record

- Run ID: RUN-2026-10-02-01
- Date, time, and timezone: 2026-10-02
- Tester: Leo
- Repository commit: 
- Target URL: https://www.saucedemo.com/
- Target application version: Not exposed
- Browser and version: Google Chrome 152.x
- Operating system and version:
- Network constraints:
- Account scenario / synthetic input data:
- Reset method and preconditions:

| Case ID | Actual observations | Result | Evidence | Defect or blocker |
| TC-AUTH-001 | After typing in a valid Login, the browser navigated to /inventory.html. The product headings were visible | PASS | /screenshots/Screenshot 2026-10-05 at 10.14.53.png>| None observed |
| TC-CART-001 | After selecting a given product the cart counter increased to 1. The product selected matched the product inside the cart. | PASS | <../screenshots/Screenshot 2026-10-05 at 10.23.51.png> <../screenshots/Screenshot 2026-10-05 at 10.24.15.png> | None observed |

- Deviations from case steps:
- Retest of prior run (if applicable):
- Next action: