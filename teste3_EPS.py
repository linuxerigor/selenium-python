from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver import FirefoxOptions
#from selenium.webdriver.firefox.options import Options



# export MOZ_HEADLESS=1

proxy = "dev-pxs-eps.cm-cic.fr:2090"
firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['proxy'] = {
    "proxyType": "MANUAL",
    "httpProxy": proxy,
    "sslProxy": proxy
}


driver = webdriver.Firefox(capabilities=firefox_capabilities)
#driver = webdriver.Firefox()

driver.get("https://www.espaceps.com/fr/identification/authentification.html")
#print(driver.title)

username = driver.find_element(By.NAME, "1099999999")
username.send_keys("_cm_user")
password = driver.find_element(By.NAME,"Az123456")
password.send_keys("_cm_pwd")

submit_button = driver.find_element(By.ID, 'login-submit')
submit_button.click()

#driver.switch_to.alert.accept()

print(driver.title)

try:
    element = WebDriverWait(driver, 10).until(
        EC.url_contains("Homepage")
    )
finally:
    print(driver.title)
    driver.quit()



driver.quit()
