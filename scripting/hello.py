from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://in.linkedin.com/")
driver.find_element(By.NAME, "session_key").send_keys("rohitgaikwad9535@gmail.com")
driver.find_element(By.NAME, "session_password").send_keys("@Bigile9535")
driver.find_element(By.XPATH, "//button[@data-id='sign-in-form__submit-btn']").click()
driver.close()


