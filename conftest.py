import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from loguru import logger

from page_objects.screens import Screen
from helpers.clean_up import CleanUp

clean_up = CleanUp()

def pytest_addoption(parser):
    parser.addoption("--url", help="URL of Application")
    parser.addoption('--chrome_version', default="78", help='Chrome version to use')


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def chrome_version(request):
    return request.config.getoption("--chrome_version")


@logger.catch()
@pytest.fixture(scope="class")
def set_up(url, chrome_version):
    logger.info("START")
    clean_up.clean_dir("verified_elements")
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(f"drivers/chromedriver_{chrome_version}", chrome_options=options)
    driver.implicitly_wait(15)
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1200, height + 100)
    driver.get(url)
    screens = Screen(driver)
    data_provider = DataProvider(driver, screens)
    logger.info(f"url: {url}")
    yield data_provider
    logger.info("Finish")
    try:
        pass
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        driver.close()


class DataProvider:

    def __init__(self, driver, screens):
        self.driver = driver
        self.screens = screens
