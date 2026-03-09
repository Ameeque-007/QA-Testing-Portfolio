from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://yourappurl.com/login")

# Login first
driver.find_element(By.ID, "email").send_keys("testuser@example.com")
driver.find_element(By.ID, "password").send_keys("Test@1234")
driver.find_element(By.ID, "loginButton").click()

# Check Dashboard element
assert driver.find_element(By.ID, "welcomeMessage").is_displayed()
driver.quit()