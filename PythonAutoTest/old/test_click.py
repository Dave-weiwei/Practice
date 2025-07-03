from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
import time

def test_click(driver):
    driver.get("https://example.oxxostudio.tw/python/selenium/demo.html")
    time.sleep(1.5)

    try:
        big_title = driver.find_element(By.CSS_SELECTOR, 'h1[title="我是大標題"]')
        big_title.click()
        big_show = driver.find_element(By.ID, "show").get_attribute("value")
        assert big_show == "大標題"
    except Exception as e:
        driver.save_screenshot("fail_大標題.png")
        raise e

    time.sleep(0.5)

    try:
        secd_title = driver.find_element(By.CSS_SELECTOR, 'h2[title="我是次標題"]')
        secd_title.click()
        secd_show = driver.find_element(By.ID, "show").get_attribute("value")
        assert secd_show == "次標題"
    except Exception as e:
        driver.save_screenshot("fail_次標題.png")
        raise e

    time.sleep(0.5)

    try:
        link_click = driver.find_element(By.LINK_TEXT, "我是超連結，點擊會開啟 Google 網站")
        link_click.click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        assert "google.com" in driver.current_url
    except Exception as e:
        driver.save_screenshot("fail_link.png")
        raise e

    driver.quit()