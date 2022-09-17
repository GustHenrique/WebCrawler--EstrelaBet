from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

option = Options()
option.headless = True
driver = webdriver.Firefox()

################################### X-PATHS  ###################################################

next_game = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/app-fixture-search/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div[3]/a[1]'
missing_days = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/div[1]'
missing_hours = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div[1]'
missing_minutes = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]'
missing_seconds = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[4]/div[1]'
probability_of_victory = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]'
probability_of_lose = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]'
probability_of_draw = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]'
opponent_team = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div'
game_day = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]'
game_hour = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[3]'

################################### X-PATHS  ###################################################

futebol_team = 'cruzeiro'

url = f"https://estrelabet.com/ptb/bet/search/{futebol_team}"

initiation_time = datetime.utcnow()
finalization_time = datetime.utcnow()

print(f"Robô INICIADO em {initiation_time}")

driver.get(url)
time.sleep(5)
driver.find_element(By.XPATH, next_game).click()
time.sleep(5)
dias_faltantes = driver.find_element(By.XPATH, missing_days).get_attribute('innerHTML')
horas_faltantes = driver.find_element(By.XPATH, missing_hours).get_attribute('innerHTML') 
minutos_faltantes = driver.find_element(By.XPATH, missing_minutes).get_attribute('innerHTML') 
segundos_faltantes = driver.find_element(By.XPATH, missing_seconds).get_attribute('innerHTML') 
chance_vitoria = driver.find_element(By.XPATH, probability_of_victory).get_attribute('innerHTML') 
chance_derrota = driver.find_element(By.XPATH, probability_of_lose).get_attribute('innerHTML') 
chance_empate = driver.find_element(By.XPATH, probability_of_draw).get_attribute('innerHTML') 
time_adversario = driver.find_element(By.XPATH, opponent_team).get_attribute('innerHTML') 
dia_jogo = driver.find_element(By.XPATH, game_day).get_attribute('innerHTML') 
hora_jogo = driver.find_element(By.XPATH, game_hour).get_attribute('innerHTML') 

print(f'O próximo jogo do {futebol_team} é no dia {dia_jogo} às {hora_jogo}.') 
print(f'Faltam {dias_faltantes} dias e {horas_faltantes}:{minutos_faltantes}:{segundos_faltantes} para o próximo jogo do cruzeiro!')
print(f'A chance de vitória é de {chance_vitoria}%, com a probabilidade de derrota de {chance_derrota}% mas com a possibilidade de empate de {chance_empate}%.')

driver.close()








