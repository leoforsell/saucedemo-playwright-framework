import { test, expect } from '@playwright/test';

test('valid credntials allow login', async({page}) =>{

    // Prepare

    await page.goto('https://www.saucedemo.com/');

    // Act

    await page.getByPlaceholder('Username').fill('standard_user');
    await page.getByPlaceholder('Password').fill('secret_sauce');
    await page.getByRole('button',{name: 'Login', exact: true}).click();
    
    // Assert

    await expect(page.getByText('Products',{exact: true})).toBeVisible();

    await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');
});

test('invalid credentials are rejected', async({page}) =>{

    // Prepare
    await page.goto('https://saucedemo.com');

    // Act

    await page.getByPlaceholder('Username').fill('standard_user');
    await page.getByPlaceholder('Password').fill('wrong_password');
    await page.getByRole('button',{name: 'Login', exact: true}).click();

    // Assert

    await expect(page.getByText('Epic sadface: Username and password do not match any user in this service', { exact: true })).toBeVisible();
    
    await expect(page).toHaveURL('https://www.saucedemo.com');
});
