import os
import pytest
from py.xml import html
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

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th("截圖"))

# 每個 fail 加入對應圖片
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    pytest_html = item.config.pluginmanager.getplugin("html")

    if report.when == "call" and report.failed:
        test_name = item.name
        folder = os.path.join("tests", "fail_screenshots")
        try:
            # 最新的日期資料夾
            latest_day = sorted(os.listdir(folder))[-1]
            full_path = os.path.join(folder, latest_day)

            # 模糊找圖（包含 test_name）
            matched = [f for f in os.listdir(full_path) if test_name in f]
            if matched:
                image_path = os.path.join(full_path, matched[0]).replace("\\", "/")
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(image_path))
                report.extra = extra
            else:
                print(f"[!] 找不到符合 {test_name} 的截圖檔案")
        except Exception as e:
            print(f"[!] 插入截圖到報告失敗: {e}")