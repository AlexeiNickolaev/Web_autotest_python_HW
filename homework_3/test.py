import time
import pytest
from testpage import OperationHelper


username = 'Smol123'
password = 'f0976457a2'


def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login('Smol123')
    test_page1.enter_pswd('f0976457a2')
    test_page1.click_button()
    time.sleep(3)

    test_page1.click_contact()
    time.sleep(3)

    test_page1.enter_cont_name('Ivan')
    test_page1.enter_cont_email('IvanSmolin@mail.ru')
    test_page1.enter_cont_text('Hello, World!')
    time.sleep(1)

    test_page1.click_button()
    time.sleep(1)

    assert test_page1.get_alert_text() == 'Form successfully processed'
