from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #  When the “detach” option is set to True, the Chrome browser window will not automatically close when the script finishes executing.

driver = webdriver.Chrome(options= options, service= Service(ChromeDriverManager().install()))
driver.get("https://github.com")

log_in = driver.find_element(By.LINK_TEXT, "Sign in")
log_in.click()

# pipenv install webdriver_manager
