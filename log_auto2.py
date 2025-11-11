from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdrvier.support.ui import #WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

# passo1: iniciar e abrir o chrome
driver = webdriver.Chrome()

#passo2: acessar a página da conta google
driver.get("https://redacao.pr.gov.br/")
time.sleep(5)

#passo3: clicar no botão estudante
pyautogui.click(x=502, y=624)
time.sleep(5)

#passo 4: Preencher o email
email_field = driver.find_element(By.ID,"identifierId")
email_field.send_keys("francisco.pellicano@escola.pr.gov.br")
driver.find_element(By.ID,"identifierNext").click()
time.sleep(2)

#aguardar senha e verificação em duas etapas
time.sleep(15)

driver.execute_script("window.open('https://classroom.google.com/');")
time.sleep(3)


print("Google Classroom acessado com sucesso! ")

input("pressione enter para fechar o chrome")