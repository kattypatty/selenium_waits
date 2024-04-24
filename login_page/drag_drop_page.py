from locators.drag_drop_locators import DragDropLocators
from login_page.login import LoginPage

class DragDropPage(LoginPage):
    drag_drops_locators = DragDropLocators()

    def click_on_accept_btn(self):
        self.click_on_element(self.drag_drops_locators.ACCEPT_BTN)

    def drag_and_drop_copy(self):
        drag_elem = self.element_is_visible(self.drag_drops_locators.DRAG_COPY)

        drop_elem = self.element_is_visible(self.drag_drops_locators.DROP_COPY_TARGET)

        self.drag_and_drop(drag_elem, drop_elem)
        text = self.element_is_visible(self.drag_drops_locators.COPY_MESSAGE).text
        return text