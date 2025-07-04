from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from scr import for_try
import pytest
import time

@pytest.mark.parametrize("index, expected", [
    (0, "選項一"),
    (1, "選項二"),
    (2, "選項三"),
])

def test_select(driver,index,expected):
    driver.get("file:///D:/PythonAutoTest/web/testweb.html")
    WebDriverWait
    def de_test():
        sel = Select(driver.find_element(By.ID,'select'))
        sel.select_by_index(index)
        sel_set = sel.first_selected_option.text
        show=driver.find_element(By.ID,"show").get_attribute("value")
        assert sel_set == expected
        assert show == expected

    for_try.use_try(driver,de_test,expected)
    time.sleep(0.3)