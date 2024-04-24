
from locators.click_locators import ClickLocators
from login_page.login import LoginPage


class BtnPage(LoginPage):
    click_locators = ClickLocators()

    def double_click_to_elem(self):
        button = self.element_is_clickable(self.click_locators.DOUBLE_CLICK_BTN)
        self.double_click(button)
        text1 = self.element_is_visible(self.click_locators.DOUBLE_CLICK_MESSAGE).text
        return text1
    
    def right_click_to_elem(self):
        button = self.element_is_clickable(self.click_locators.RIGHT_CLICK_BTN)
        self.right_click(button)
        text2 = self.element_is_visible(self.click_locators.RIGHT_CLICK_MESSAGE).text
        return text2
    

