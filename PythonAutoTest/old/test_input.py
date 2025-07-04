from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_input(driver):

    driver.get("https://example.oxxostudio.tw/python/selenium/demo.html")
    time.sleep(1.5)
    show=driver.find_element(By.ID,"show")
    action=ActionChains(driver)
    action.move_to_element(show).click().send_keys("28aB@你好").perform()
    input_show = driver.find_element(By.ID,"show").get_attribute("value")
    try:
        assert input_show == "28aB@你好"
    except AssertionError:
        driver.save_screenshot("fail_input.png")
        raise
    
    driver.quit()