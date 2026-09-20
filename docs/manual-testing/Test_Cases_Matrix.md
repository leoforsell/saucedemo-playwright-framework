# Test Cases and Traceability Matrix: SauceDemo

## Document Control

| Field | Value |
| --- | --- |
| Status | Draft |
| Version | 0.1.0 |
| Related strategy | [Test Strategy](Test_Strategy_SauceDemo.md) |

These are proposed portfolio expectations, to be reviewed during the first walkthrough. Use independent clean sessions and the standard demo account unless a case states otherwise. The ten baseline cases are retained; TC-AUTH-003 adds the invalid-login scenario required in Week 2. All remain **Not run**.

Technique notes: removing the last cart item is a valid state transition (one item → empty), not a negative test. An empty required field is an invalid equivalence partition; do not label it boundary-value analysis without a specified numeric or ordered boundary.

## User Stories

| ID | User story |
| --- | --- |
| US-01 | As a registered customer, I want to sign in so that I can shop. |
| US-02 | As a customer, I want to browse and sort products so that I can choose an item. |
| US-03 | As a customer, I want to manage my cart so that I can review my order. |
| US-04 | As a customer, I want to enter checkout information so that I can complete an order. |
| US-05 | As a customer, I want clear order confirmation so that I know the purchase succeeded. |
| US-06 | As a customer, I want to log out so that my session is closed. |

## Test Case Matrix

| Test ID | Module | User story | Risk | Priority | Type | Status |
| --- | --- | --- | --- | --- | --- | --- |
| TC-AUTH-001 | Authentication | US-01 | R-01 | P1 | Positive | Not run |
| TC-AUTH-002 | Authentication | US-01 | R-01 | P1 | Negative | Not run |
| TC-AUTH-003 | Authentication | US-01 | R-01 | P1 | Negative / equivalence partition | Not run |
| TC-INV-001 | Inventory | US-02 | R-02 | P1 | Positive | Not run |
| TC-INV-002 | Sorting | US-02 | R-03 | P2 | Positive | Not run |
| TC-CART-001 | Cart | US-03 | R-04 | P1 | Positive | Not run |
| TC-CART-002 | Cart | US-03 | R-04 | P2 | Positive / state transition | Not run |
| TC-CHK-001 | Checkout | US-04 | R-05 | P1 | Positive | Not run |
| TC-CHK-002 | Checkout | US-04 | R-05 | P1 | Negative / equivalence partition | Not run |
| TC-ORD-001 | Order confirmation | US-05 | R-06 | P1 | Positive | Not run |
| TC-LOG-001 | Logout | US-06 | R-07 | P2 | Positive | Not run |

## Formal Test Cases

### TC-AUTH-001: Successful login

- **Preconditions:** User is on the login page with no active session.
- **Data:** `standard_user` / `secret_sauce`
- **Given:** A valid user is on the SauceDemo login page.
- **When:** The user enters valid credentials and selects Login.
- **Then:** The user reaches `/inventory.html` and sees the Products heading.

### TC-AUTH-002: Locked user cannot log in

- **Preconditions:** User is on the login page.
- **Data:** `locked_out_user` / `secret_sauce`
- **Given:** A locked user is on the SauceDemo login page.
- **When:** The user submits valid credentials for the locked account.
- **Then:** The user remains on the login page and sees a clear error message.

### TC-AUTH-003: Invalid credentials are rejected

- **Preconditions:** Fresh browser session on the login page.
- **Data:** `standard_user` / `deliberately_invalid_password` (synthetic).
- **Given:** A valid username with an incorrect password.
- **When:** The user submits the credentials.
- **Then:** The user remains on the login page, a visible authentication error is shown, and inventory access is denied.
- **Technique:** Invalid credential equivalence partition; keep the locked-account case separate.
- **Automation mapping:** Planned Week 2 in `tests/e2e/auth.spec.js`, alongside TC-AUTH-001. Add exact test titles and run links only after implementation.

### TC-INV-001: Inventory is displayed

- **Preconditions:** User is successfully authenticated.
- **Given:** The customer has reached the inventory page.
- **When:** The inventory page finishes loading.
- **Then:** Products and their purchase controls are visible.

### TC-INV-002: Products can be sorted

- **Preconditions:** User is on the inventory page.
- **Given:** Multiple products are displayed.
- **When:** The customer selects each supported sort option.
- **Then:** For each of the four name/price directions, compare the full displayed sequence against an independently sorted copy. Compare prices as numbers, not text. Record each option separately within the execution record.

### TC-CART-001: Product can be added to the cart

- **Preconditions:** User is on the inventory page.
- **Given:** A product is available.
- **When:** The customer adds that product to the cart.
- **Then:** From an initially empty cart, the badge becomes 1 and the selected item appears with the same name and unit price. Record the chosen item and observed price before adding it.

### TC-CART-002: Product can be removed from the cart

- **Preconditions:** The cart contains one product.
- **Given:** The customer is viewing the cart.
- **When:** The customer removes the product.
- **Then:** No cart item remains and the badge no longer shows a positive count. Return to inventory and confirm the item can be added again.

### TC-CHK-001: Checkout accepts valid customer data

- **Preconditions:** The cart contains at least one product.
- **Data:** Synthetic first name `Test`, last name `Shopper`, postal code `12345`. This is a completeness check, not proof of real postal validation.
- **Given:** The customer starts checkout with a non-empty cart.
- **When:** The customer enters valid information and continues.
- **Then:** The customer reaches the order overview.

### TC-CHK-002: Checkout rejects missing postal code

- **Preconditions:** The customer is on the checkout information form.
- **Data:** First name and last name populated; postal code empty.
- **Given:** Required checkout data is incomplete.
- **When:** The customer continues without a postal code.
- **Then:** The form remains open and identifies the missing required field.

### TC-ORD-001: Order can be completed

- **Preconditions:** The order overview contains a valid cart item and customer data.
- **Given:** The customer reviews a valid order.
- **When:** The customer completes the order.
- **Then:** A confirmation page communicates that the order was placed.

### TC-LOG-001: User can log out

- **Preconditions:** User is authenticated.
- **Given:** The customer opens the navigation menu.
- **When:** The customer selects Logout.
- **Then:** The user returns to the login page and cannot access the inventory without signing in again.

## Execution Record

| Test ID | Tester | Environment | Date | Result | Evidence |
| --- | --- | --- | --- | --- | --- |
| No execution recorded | Pending | Pending | Pending | Not run | Pending |

Use one row per case/run and link a completed [execution record](Execution_Record_Template.md). Keep automation status and manual results separate. Future coverage additions: independent subtotal/total calculations, all required checkout fields, and direct navigation after logout; a mapped case does not prove every aspect of its risk is covered.

