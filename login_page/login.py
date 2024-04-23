from selenium.webdriver.support.ui import WebDriverWait
from locators.login_locators import LoginPage_Locators
from locators.src.user_data import UserData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from dotenv import load_dotenv
import os
from selenium.webdriver import ActionChains
import pytest
import time

load_dotenv()

class LoginPage():
    user = UserData()
    timeout = 5
    
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout=10)
        self.open()

    # opening webrowser
    def open(self):
        self.driver.get(self.url)

    def open_registration_form(self):
        # Wait for the button to appear and click on it
        visible_button = self.wait.until(EC.element_to_be_clickable(LoginPage_Locators.BEGIN_BTN))
        visible_button.click()
        return self.get_text(LoginPage_Locators.BEGIN_BTN)

    def login(self):
        self.open_registration_form()
        
        self.filling_form()

        # Click on checkbox
        checkbox = self.element_is_visible(LoginPage_Locators.CHECKBOX)
        if checkbox.get_attribute("checked") != "true":
            checkbox.click()
        # Register
        self.element_is_visible(LoginPage_Locators.REGISTER_BTN).click()

        self.checking_loading()

        return self.checking_for_success_message()   
       

    # Fill in the Registration Form
    def filling_form(self):
        input_login = self.element_is_visible(LoginPage_Locators.LOGIN)
        input_password = self.element_is_visible(LoginPage_Locators.PASSWORD)
        input_login.send_keys(os.getenv("LOGIN"))
        input_password.send_keys(os.getenv("PASSWORD"))

    def registration_form_appeared(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def checking_loading(self):
        return self.element_is_visible(LoginPage_Locators.LOADING_INDICATOR)

    def checking_for_success_message(self):
        return self.get_text(LoginPage_Locators.SUCCESSFUL_MESSAGE)
    
    # waiting until the element becomes visible
    def element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    # checking an element is visible and enabled such that you can click it
    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    # getting text to check the actual title of the home page
    def get_text(self, locator):
        return self.element_is_visible(locator).text
    
    # double click on the button
    def double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    # right click on the button
    def right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()
