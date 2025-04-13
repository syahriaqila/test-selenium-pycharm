from sys import executable

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByIDandName():
    def locate_by_id_demo(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://battwo.com/signin")
        #driver.find_element_by_id('username-:nullr0:').send_keys('test@test.com')
        driver.find_element(By.ID, 'username-:nullr0:').send_keys('test@test.com')
        driver.quit()
        time.sleep(15)


if __name__ == "__main__":
    findbyid = DemoFindElementByIDandName()
    findbyid.locate_by_id_demo()