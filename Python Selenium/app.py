from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://github.com")

# Click on the 'Sign in' button
log_in = driver.find_element(By.LINK_TEXT, "Sign in")
log_in.click() 

# Perfect until here

username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login_field")))
username.send_keys("gabybarcodes")  # replace 'your_username' with your actual GitHub username

# Wait for the password field to be loaded
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
password.send_keys("passcode")
