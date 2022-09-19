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
missing_days_path = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/div[1]'
missing_hours_path = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div[1]'
missing_minutes_path = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]'
missing_seconds_path = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div[4]/div[1]'
probability_of_lose1 = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]'
probability_of_victory1 = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]'
probability_of_lose2 = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]'
probability_of_victory2 = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]'
team1 = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div'
probability_of_draw = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]'
opponent_team = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div'
game_day_path = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]'
game_hour_path = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[3]'
model_content = 'fixture-container'
previous_draw = '//*[@id="content1"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]'
previous_lose1 = '//*[@id="content1"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]'
previous_victory1 = '//*[@id="content1"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]'
previous_lose2 = '//*[@id="content1"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]'
previous_victory2 = '//*[@id="content1"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]'

################################### X-PATHS  ###################################################

team_url = 'cruzeiro'
team_all_name = 'Cruzeiro MG'

url = f"https://estrelabet.com/ptb/bet/search/{team_url}"

initiation_time = datetime.today().replace(microsecond=0)

print(f"Crawler INICIADO em {initiation_time}")

driver.get(url)
time.sleep(20)
if driver.find_element(By.XPATH, next_game):
    name_team_search = driver.find_element(By.XPATH, next_game)
    model_games =  driver.find_elements(By.CLASS_NAME, model_content)
else:
    driver.refresh()
    time.sleep(20)
    name_team_search = driver.find_element(By.XPATH, next_game)
    model_games =  driver.find_elements(By.CLASS_NAME, model_content)

for item in model_games:
    if team_all_name.lower() in item.get_attribute('innerHTML').lower():
        name_team_search.click()
        break

time.sleep(10)
try:
    missing_days = driver.find_element(By.XPATH, missing_days_path).get_attribute('innerHTML')
    missing_hours = driver.find_element(By.XPATH, missing_hours_path).get_attribute('innerHTML') 
    missing_minutes = driver.find_element(By.XPATH, missing_minutes_path).get_attribute('innerHTML') 
    missing_seconds = driver.find_element(By.XPATH, missing_seconds_path).get_attribute('innerHTML') 
    missing_time = missing_hours + ':' + missing_minutes + ':' + missing_seconds
except Exception:
    missing_days = None
    missing_hours = None  
    missing_minutes = None 
    missing_seconds = None 
    missing_time = None

if  team_url.lower() in driver.find_element(By.XPATH, team1).get_attribute('innerHTML').lower():
    chance_defeat = driver.find_element(By.XPATH, probability_of_lose1).get_attribute('innerHTML') + '%'
    chance_victory= driver.find_element(By.XPATH, probability_of_victory1).get_attribute('innerHTML')  + '%'
else:
    chance_win = driver.find_element(By.XPATH, probability_of_victory2).get_attribute('innerHTML') + '%'
    chance_defeat = driver.find_element(By.XPATH, probability_of_lose2).get_attribute('innerHTML')  + '%'
if  team_url.lower() in driver.find_element(By.XPATH, team1).get_attribute('innerHTML').lower():
    previous_victories = driver.find_element(By.XPATH, previous_victory1).get_attribute('innerHTML')
    previous_defeats = driver.find_element(By.XPATH, previous_lose1).get_attribute('innerHTML')
else:
    previous_victories = driver.find_element(By.XPATH, previous_victory2).get_attribute('innerHTML')
    previous_defeats = driver.find_element(By.XPATH, previous_lose2).get_attribute('innerHTML')

missing_draws = driver.find_element(By.XPATH, previous_draw).get_attribute('innerHTML')
chance_draw = driver.find_element(By.XPATH, probability_of_draw).get_attribute('innerHTML')  + '%'
opposing_team = driver.find_element(By.XPATH, opponent_team).get_attribute('innerHTML') 
game_day = driver.find_element(By.XPATH, game_day_path).get_attribute('innerHTML') 
game_hour = driver.find_element(By.XPATH, game_hour_path).get_attribute('innerHTML') 
previous_encounters = int(previous_victories) + int(previous_defeats) + int(missing_draws)

first_text = (f'O próximo jogo do {team_all_name} é no dia {game_day} às {game_hour} e vai jogar contra o {opposing_team}.') 
if missing_days != None:
    second_text = (f'Faltam {missing_days} dias e {missing_time} horas para o próximo jogo do {team_all_name}!')
else:
    second_text = (f'Ainda falta ser anunciado o tempo que falta para o jogo')
third_text = (f'A chance de vitória para o {team_all_name} é de {chance_victory} porém existe a probabilidade de derrota de {chance_defeat} mas com a possibilidade de empate de {chance_draw}.')
fourth_text = (f'Os times {team_all_name} e {opposing_team} tiveram {previous_encounters} encontros anteriore(s), dentre ele(s)  o {team_all_name} teve {previous_victories} vitória(s), {previous_defeats} derrota(s) e {missing_draws} empate(s).')
separador = '----->---------------------------------------------->------------------------------------------->------------->---------------------------------------------->------------------------------------------->---------------------------------->--------'
data = [first_text, second_text, third_text, fourth_text, separador]

driver.close()
file = open("next_games.txt", "a", newline="")
for text in data:
    file.write(text+'\n')
file.close()
