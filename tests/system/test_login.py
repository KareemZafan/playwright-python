import time
import pytest

# tests/system/test_login.py
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def open_login_page(page: Page):
    page.goto(
        "https://the-internet.herokuapp.com/login", timeout=60000)
    expect(page).to_have_title("The Internet")
    expect(page.locator("h2")).to_have_text("Login Page")

def test_successful_login(page: Page):

    # Fill credentials and submit
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button.radius")

    # Assert redirect to secure area
    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/secure")

    # Assert success flash message
    flash = page.locator(".flash.success")
    expect(flash).to_be_visible()
    expect(flash).to_contain_text(
        "You logged into a secure area!")
    expect(page.locator("a[href='/logout']")).to_be_visible()

def test_invalid_login_wrong_username(page: Page):

    # Fill credentials and submit
    page.fill("#username", "test")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button.radius")

    # Assert redirect to secure area
    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/login")

    # Assert success flash message
    flash = page.locator("#flash-messages #flash")
    expect(flash).to_be_visible()
    expect(flash).to_contain_text(
        "Your username is invalid!")

def test_invalid_login_wrong_password(page: Page):
   
    # Fill credentials and submit
    page.fill("#username", "tomsmith")
    page.fill("#password", "Wrongpassword")
    page.click("button.radius")

    # Assert redirect to secure area
    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/login")

    # Assert success flash message
    flash = page.locator("#flash-messages #flash")
    expect(flash).to_be_visible()
    expect(flash).to_contain_text(
        "Your password is invalid!")  
    

def test_invalid_login_empty_credentials(page: Page):

    # Fill credentials and submit
    page.fill("#username", "")
    page.fill("#password", "")
    page.click("button.radius")

    # Assert redirect to secure area
    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/login")

    # Assert success flash message
    flash = page.locator("#flash-messages #flash")
    expect(flash).to_be_visible()
    expect(flash).to_contain_text(
        "Your username is invalid!")  
    

def test_invalid_login_empty_credentials(page: Page):
   
    # Fill credentials and submit
    page.fill("#username", "tomsmith")
    page.fill("#password", "")
    page.click("button.radius")

    # Assert redirect to secure area
    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/login")

    # Assert success flash message
    flash = page.locator("#flash-messages #flash")
    expect(flash).to_be_visible()
    expect(flash).to_contain_text(
        "Your password is invalid!")
    


