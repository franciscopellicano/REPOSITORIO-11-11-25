from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_path = "C:/chrome-win64/chrome.exe"
service = Service(executable_path="C:/chromedriver-win64/chromedriver.exe")

options = webdriver.ChromeOptions()
options.binary_location = chrome_path
options.add_experimental_option("detach", True)  # <-- mantém o Chrome aberto

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")

# Não precisa chamar driver.quit()