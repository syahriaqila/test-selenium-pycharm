from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.vfolio.hafiz.day/")
time.sleep(10)
driver.maximize_window()     # Replace with your actual URL
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Fill in the form happy flow
try:

    driver.find_element(By.NAME, "contact_name").send_keys("John Doe")
    driver.find_element(By.NAME, "contact_email").send_keys("john@example.com")
    driver.find_element(By.NAME, "contact_subject").send_keys("Test Subject")
    driver.find_element(By.NAME, "contact_message").send_keys("This is a test message.")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='Send Message']").click()

    # Wait and check for success message
    time.sleep(2)
    success_msg = driver.find_element(By.ID, "swal2-title").text
    assert "Success!" in success_msg  # Adjust based on your actual message

    driver.find_element(By.CSS_SELECTOR, "button.swal2-confirm").click()

    print("happy flow Test passed!")
except:
    print("happy flow Test failed!")

#bad flow email wrong
try:
    driver.find_element(By.NAME, "contact_name").clear()
    driver.find_element(By.NAME, "contact_email").clear()
    driver.find_element(By.NAME, "contact_subject").clear()
    driver.find_element(By.NAME, "contact_message").clear()
    time.sleep(3)

    driver.find_element(By.NAME, "contact_name").send_keys("John Doe")
    driver.find_element(By.NAME, "contact_email").send_keys("johnil.com")
    driver.find_element(By.NAME, "contact_subject").send_keys("Test Subject")
    driver.find_element(By.NAME, "contact_message").send_keys("This is a test message.")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='Send Message']").click()


    # Wait and check for success message
    time.sleep(2)
    success_msg = driver.find_element(By.ID, "swal2-title").text
    assert "Oops..." in success_msg  # Adjust based on your actual message

    driver.find_element(By.CSS_SELECTOR, "button.swal2-confirm").click()

    print("bad email Test passed!")
except:
    print("bad email Test failed!")

driver.quit()

#local script test pointing to production server