import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class foodservice_ATS1(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_admin_MyAccount(self):
        user = "vish"
        pwd = "1instructor1"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/accounts/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/home")
        assert "Logged In"
        driver.find_element_by_xpath("//*[@id='myNavbar']/ul[2]/li/a").click()
        time.sleep(2)


    def teardown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


