
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoSeleniumlearning():
    def demo_browser_methods(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://training.rcvacademy.com/m")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.minimize_window()
        driver.quit()
        time.sleep(15)
        driver.find_element(By.linktext("ALL COURSES").click())