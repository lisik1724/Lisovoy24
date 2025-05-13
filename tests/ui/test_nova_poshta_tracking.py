import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'modules')))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ui.page_objects.nova_poshta_page import NovaPoshtaPage

@pytest.mark.ui
def test_invalid_tracking_number():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    page = NovaPoshtaPage(driver)

    page.go_to()
    page.track_ttn("12345678901234")  # завідомо неіснуючий номер
    assert page.is_error_message_visible()

    page.close()
