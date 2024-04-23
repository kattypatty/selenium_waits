import os
from dotenv import load_dotenv

from login_page.click_page import BtnPage

load_dotenv()

class TestClickBtnTest:
    btn_url = os.getenv("BUTTON_URL")

    def test_double_click(self, driver):
        page = BtnPage(driver, self.btn_url)
        page.open()
        message_text = page.double_click_to_elem()
        assert message_text == "You have done a double click"
