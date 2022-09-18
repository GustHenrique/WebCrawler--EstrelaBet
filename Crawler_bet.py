from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.headless = True
driver = webdriver.Firefox()

################################### X-PATHS  ###################################################

next_game = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/app-fixture-search/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div[3]/a[1]'
missing_days = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/div[1]'
missing_hours = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div[1]'
missing_minutes = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]'
missing_seconds = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[4]/div[1]'
probability_of_lose = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]'
probability_of_victory = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]'
probability_of_draw = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]'
opponent_team = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div'
game_day = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]'
game_hour = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[3]'
model_content = 'fixture-container'

################################### X-PATHS  ###################################################

team_url = 'cruzeiro'
team_all_name = 'Cruzeiro MG'

url = f"https://estrelabet.com/ptb/bet/search/{team_url}"

initiation_time = datetime.today().replace(microsecond=0)

print(f"Robô INICIADO em {initiation_time}")

driver.get(url)
time.sleep(10)
name_team_search = driver.find_element(By.XPATH, next_game)
model_games =  driver.find_elements(By.CLASS_NAME, model_content)
for item in model_games:
    if team_all_name.lower() in item.get_attribute('innerHTML').lower():
        name_team_search.click()
        break
time.sleep(10)
dias_faltantes = driver.find_element(By.XPATH, missing_days).get_attribute('innerHTML')
horas_faltantes = driver.find_element(By.XPATH, missing_hours).get_attribute('innerHTML') 
minutos_faltantes = driver.find_element(By.XPATH, missing_minutes).get_attribute('innerHTML') 
segundos_faltantes = driver.find_element(By.XPATH, missing_seconds).get_attribute('innerHTML') 
chance_derrota = driver.find_element(By.XPATH, probability_of_lose).get_attribute('innerHTML') + '%'
chance_vitoria = driver.find_element(By.XPATH, probability_of_victory).get_attribute('innerHTML')  + '%'
chance_empate = driver.find_element(By.XPATH, probability_of_draw).get_attribute('innerHTML')  + '%'
time_adversario = driver.find_element(By.XPATH, opponent_team).get_attribute('innerHTML') 
dia_jogo = driver.find_element(By.XPATH, game_day).get_attribute('innerHTML') 
hora_jogo = driver.find_element(By.XPATH, game_hour).get_attribute('innerHTML') 
tempo_faltante = horas_faltantes + ':' + minutos_faltantes + ':' + segundos_faltantes

print(horas_faltantes)
print(f'O próximo jogo do {team_all_name} é no dia {dia_jogo} às {hora_jogo} e vai jogar contra o {time_adversario}.') 
print(f'Faltam {dias_faltantes} dias e {tempo_faltante} horas para o próximo jogo do cruzeiro!')
print(f'A chance de vitória para o Cruzeiro é de {chance_vitoria} porém existe a probabilidade de derrota de {chance_derrota} mas com a possibilidade de empate de {chance_empate}%.')

driver.close()










