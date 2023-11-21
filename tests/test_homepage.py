from playwright.sync_api import expect

def test_homepage_navbar(page, test_app, test_client, seed_test_database, flask_server):
    test_url = "http://localhost:5000/"
    page.goto(test_url)
    logo = page.locator('.logo')
    expect(logo).to_have_text('SHUFFLESHACK')
    nav_item_ps = page.locator('.nav-item p')
    expect(nav_item_ps).to_have_text([
        'Check in',
        'Check out',
        'City',
        'Guests'
    ])
    go_button = page.locator('.nav-item input[type="submit"]')
    expect(go_button).to_have_text('Go')

def test_homepage_random_30_properties(page, test_app, test_client, seed_test_database, flask_server):
    test_url = "http://localhost:5000/"
    page.goto(test_url)
    properties_container = page.locator('.properties-container')
    expect(properties_container).to_contain_text('Eine gemütliche Haus\nInnsbruck, Austria\nEine gemütliche Haus in der Nähe von Innsbruck\nFrom £90.00 per night')
    expect(properties_container).to_contain_text('Rubens Guest House\nLondon, United Kingdom\nA majestic five-star London hotel-like house near Buckingham Palace. The Rubens Guest House offers the perfect combination of classic elegance and unrivalled hospitality for business and leisure travellers alike.\nFrom £105.00 per night')

def test_homepage_register_and_login(page, test_app, test_client, seed_test_database, flask_server):
    test_url = "http://localhost:5000/"
    page.goto(test_url)
    page.click(".menu-icon")
    page.click("text='Register'")
    page.fill("#first_name", "Mike")
    page.fill("#last_name", "Test")
    page.fill("#user_name", "miketest")
    page.fill("#email", "miketest@gmail.com")
    page.fill("#phone_number", "01234567890")
    page.fill("#date_of_birth", "1990-01-01")
    page.fill("#nationality", "Testland")
    page.fill("#password", "Test123!")
    page.fill("#confirm_password", "Test123!")
    page.click("#submit_register")
    user_name = page.locator('.user-name')
    expect(user_name).to_have_text('mik')
    page.click(".menu-icon")
    page.click("text='Logout'")
    expect(user_name).to_have_text('Menu')
    page.click(".menu-icon")
    page.click("text='Login'")
    page.fill("#email_login", "miketest")
    page.fill("#password_login", "Test123!")
    page.click("#submit_login")
    expect(user_name).to_have_text('mik')
    page.click(".menu-icon")
    page.click("text='Logout'")
    expect(user_name).to_have_text('Menu')
    page.click(".menu-icon")
    page.click("text='Login'")
    page.fill("#email_login", "miketest@gmail.com")
    page.fill("#password_login", "Test123!")
    page.click("#submit_login")
    expect(user_name).to_have_text('mik')
