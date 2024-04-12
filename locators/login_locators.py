class LoginPage_Locators:

    # Buttons Locators
    TITLE = ("css selector", "body h1")
    BEGIN_BTN = ("css selector", "button[id='startTest']")
    REGISTER_BTN = ("css selector","button[id='register']")

    # Login Locators
    LOGIN = ("css selector", "input[type='text']")
    PASSWORD = ("css selector", "input[type='password']")
    CHECKBOX = ("css selector","input[type='checkbox']")
    LOADING_INDICATOR = ("css selector","div[id='loader']")
    SUCCESSFUL_MESSAGE = ("css selector","p[id='successMessage']")