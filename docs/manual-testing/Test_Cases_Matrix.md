# Test Cases and Traceability Matrix: SauceDemo

## Document Control

| Field | Value |
| --- | --- |
| Status | Draft |
| Version | 0.1.0 |
| Related strategy | [Test Strategy](Test_Strategy_SauceDemo.md) |

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
| TC-INV-001 | Inventory | US-02 | R-02 | P1 | Positive | Not run |
| TC-INV-002 | Sorting | US-02 | R-03 | P2 | Positive | Not run |
| TC-CART-001 | Cart | US-03 | R-04 | P1 | Positive | Not run |
| TC-CART-002 | Cart | US-03 | R-04 | P2 | Negative / boundary | Not run |
| TC-CHK-001 | Checkout | US-04 | R-05 | P1 | Positive | Not run |
| TC-CHK-002 | Checkout | US-04 | R-05 | P1 | Negative / boundary | Not run |
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

### TC-INV-001: Inventory is displayed

- **Preconditions:** User is successfully authenticated.
- **Given:** The customer has reached the inventory page.
- **When:** The inventory page finishes loading.
- **Then:** Products and their purchase controls are visible.

### TC-INV-002: Products can be sorted

- **Preconditions:** User is on the inventory page.
- **Given:** Multiple products are displayed.
- **When:** The customer selects each supported sort option.
- **Then:** Product order matches the selected name or price direction.

### TC-CART-001: Product can be added to the cart

- **Preconditions:** User is on the inventory page.
- **Given:** A product is available.
- **When:** The customer adds that product to the cart.
- **Then:** The cart indicator updates and the item appears in the cart.

### TC-CART-002: Product can be removed from the cart

- **Preconditions:** The cart contains one product.
- **Given:** The customer is viewing the cart.
- **When:** The customer removes the product.
- **Then:** The product is no longer listed and the cart state updates.

### TC-CHK-001: Checkout accepts valid customer data

- **Preconditions:** The cart contains at least one product.
- **Data:** Valid first name, last name, and postal code.
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
| All cases | Pending | Pending | Pending | Not run | Pending |
