import time
from dotenv import load_dotenv
import os

from login_page.drag_drop_page import DragDropPage

load_dotenv()

class TestDragDrop:
    drag_drop_url = os.getenv("DRAG_AND_DROP")
    
    def test_drag_drop_elem_acceptable(self, driver):
        page = DragDropPage(driver, self.drag_drop_url)
        text = page.drag_and_drop_copy()
        assert text == "Select this element and drag to the Copy Drop Zone."
