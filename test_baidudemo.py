import allure
import pytest
import yaml
from selenium import webdriver
import time

@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
# @pytest.mark.parametrize('test_ztc',['allure'])
@pytest.mark.parametrize('test_ztc',yaml.safe_load(open("./data/data.yml")))
def test_steps_demo(test_ztc):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome("D:\TestTools\webdriver\chromedriver.exe")
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词：{test_ztc}"):
        driver.find_element_by_id("kw").send_keys(test_ztc)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()

