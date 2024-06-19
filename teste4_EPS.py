from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


options = Options()
cloud_options = {}
cloud_options['build'] = "build_1"
cloud_options['name'] = "test_abc"
options.set_capability('cloud:options', cloud_options)
driver = webdriver.Remote("http://localhost:4444/wd/hub", options=webdriver.ChromeOptions())

#driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub')

#driver = webdriver.Remote(
#   command_executor='http://127.0.0.1:4444/wd/hub',
#   options=webdriver.ChromeOptions()
#)

#driver = webdriver.Firefox()
#driver = webdriver.Chrome()

driver.get("https://www.espaceps.com/fr/identification/authentification.html")



username = driver.find_element(By.NAME, "user")
username.send_keys("login")
password = driver.find_element(By.NAME,"pass")
password.send_keys("mdp")

submit_button = driver.find_element(By.ID, 'login-submit')
submit_button.click()

#driver.switch_to.alert.accept()

try:
    element = WebDriverWait(driver, 10).until(
        EC.title_contains("Correio :: Caixa de Entrada")
    )
finally:
    print(driver.title)
    driver.quit()



driver.quit()
