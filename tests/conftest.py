import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--mybrowser",
        action="store",
        default="chrome",
        help="指定瀏覽器: chrome 或 firefox"
    )

@pytest.fixture(scope="module")
def driver(request):
    browser = request.config.getoption("--mybrowser")

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"❌ 不支援的瀏覽器: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()