import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="session")
def driver():
    zebrunner_selenium_grid = os.getenv("ZEBRUNNER_SELENIUM_GRID", "http://127.0.0.1:4444")

    # log_path = 'chromedriver.log'
    # service = ChromeService(log_path=log_path)

    ############################################################################################
    options = webdriver.ChromeOptions()
    options.platform_name = "linux"
    options.browser_version = "112.0"
    options.set_capability("enableVideo", "true")
    ############################################################################################

    driver = webdriver.Chrome(options=options)


    driver.implicitly_wait(10)
    # driver.maximize_window()

    yield driver

    driver.quit()
