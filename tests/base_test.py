# Example shows BASIC reporting to Zebrunner:
# - passed/failed test methods
# - logs and screenshots inside them

import logging
import time

from pytest_zebrunner import attach_test_screenshot
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Logger configuring
logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


# # Test data
# url = "https://www.google.com/"
# cookies_dialog_test = "Before you continue to Google Search"
# search_value = "Zebrunner"


def test_simple(driver):
    # logger.info("'test_simple' test was started")

    # logger.info("Navigating to url: " + url)
    # driver.get(url=url)

    # logger.info("timeout1")
    # time.sleep(20)
    # logger.info("/timeout1")
    #
    # # attach_screenshot(driver)
    #
    # logger.info("timeout2")
    # time.sleep(20)
    # logger.info("/timeout2")
    assert True
    logger.info("test finished")


def test_simple1(driver):
    assert True
    logger.info("test1 finished")


def test_simple2(driver):
    assert True
    logger.info("test2 finished")


def test_simple3(driver):
    assert True
    logger.info("test3 finished")


# def attach_screenshot(driver):
#     driver.save_screenshot("screenshot.png")
#     attach_test_screenshot("screenshot.png")
