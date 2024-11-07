from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
try:
    # Entrando na pagina de login do ava
    driver.get("https://ava.unicatolicaquixada.edu.br/portal3/login/index.php")
    time.sleep(2)

    # inserindo a matricula
    matricula = driver.find_element(By.XPATH, '//*[@id="username"]') # procurando o input
    matricula.send_keys('matricula') # digitando
    time.sleep(2)

    # inserindo a senha
    passw = driver.find_element(By.XPATH, '//*[@id="password"]') # procurando o input
    passw.send_keys('senha') # digitando
    time.sleep(2)

    # clicando no botão de login
    clickbtn = driver.find_element(By.XPATH, '//*[@id="loginbtn"]') # procurando o button
    clickbtn.click() # click
    time.sleep(2)
    
    # icone de chat
    clickicon = driver.find_element(By.XPATH, '/html/body/div[3]/nav/div[2]/div[2]/a')
    clickicon.click()
    time.sleep(2)
    
    # chat's privados
    clickchat = driver.find_element(By.XPATH, '/html/body/div[3]/div[6]/div/div[3]/div[5]/div/div[3]/div[1]/button')
    clickchat.click()
    time.sleep(2)
    
    # chat user
    clickuser = driver.find_element(By.XPATH, '/html/body/div[3]/div[6]/div/div[3]/div[5]/div/div[3]/div[2]/div[2]/a[1]')
    clickuser.click()
    time.sleep(4)

    # auto mensagem
    for i in range(100):
        text = driver.find_element(By.XPATH, '/html/body/div[3]/div[6]/div/div[4]/div[1]/div[1]/div[2]/textarea');
        text.send_keys('Happy Nation')
        text.send_keys(Keys.RETURN)

    time.sleep(50)
finally:
    print(f'Error: Not Found')
