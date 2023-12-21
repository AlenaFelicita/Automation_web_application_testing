from testpage import OperationHelper
import logging
import time

import yaml

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)
    name = data["username"]
    paswd = data["password"]


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    time.sleep(3)
    assert testpage.get_error_text() == "401", "Test_1 FAIL"


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(name)
    testpage.enter_pass(paswd)
    testpage.click_login_button()
    time.sleep(2)
    assert testpage.get_profile_text() == f"Hello, {name}", "Test_2 FAIL"


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationHelper(browser)
    testpage.click_to_do_new_post()
    testpage.enter_title("Hello, world")
    testpage.enter_description("help")
    testpage.enter_content("Bye, world")
    testpage.click_save_post_button()
    time.sleep(5)
    assert testpage.get_title_text() == "Hello, world", "Test_3 FAIL"




def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationHelper(browser)
    testpage.click_contact_button()
    testpage.enter_name("Eva")
    testpage.enter_email("any@mail.ru")
    testpage.enter_contact_content("my contact")
    testpage.contact_us_save_button()
    time.sleep(3)
    assert testpage.get_alert_text() == "Form successfully submitted", "Test_4 FAIL"
