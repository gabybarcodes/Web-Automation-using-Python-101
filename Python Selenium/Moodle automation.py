from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://moodle.hochschule-heidelberg.de")

wait = WebDriverWait(driver, 10)
login_with_365 = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login mit M365")))
login_with_365.click()


username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i0116")))
username.send_keys("11027697@STUD.HOCHSCHULE-HEIDELBERG.DE")  

next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
next_button.click()

password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i0118")))
password.send_keys("GWagon2023!")

sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
sign_in_button.click()
