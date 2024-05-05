from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= options, service= Service(ChromeDriverManager().install()))
driver.get("http://selenium.dev")

# pipenv install webdriver_manager