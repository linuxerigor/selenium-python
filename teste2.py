from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://url/webmail.php")

username = driver.find_element(By.NAME, "imapuser")
username.send_keys("....")
password = driver.find_element(By.NAME,"pass")
password.send_keys("....")

submit_button = driver.find_element(By.CLASS_NAME, 'button')
submit_button.click()

driver.switch_to.alert.accept()

try:
    element = WebDriverWait(driver, 10).until(
        EC.title_contains("Correio :: Caixa de Entrada")
    )
finally:
    print(driver.title)
    driver.quit()



driver.quit()