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
probability_of_lose1 = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]'
probability_of_victory1 = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]'
probability_of_lose2 = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]'
probability_of_victory2 = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]'
team1 = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div'
probability_of_draw = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]'
opponent_team = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div'
game_day = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]'
game_hour = '/html/body/app-root/app-out-component/div[1]/main/app-placebet/div/div/fixture-detail/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[3]'
model_content = 'fixture-container'
previous_draw = '//*[@id="content1"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]'
previous_lose1 = '//*[@id="content1"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]'
previous_victory1 = '//*[@id="content1"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]'
previous_lose2 = '//*[@id="content1"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]'
previous_victory2 = '//*[@id="content1"]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]'

################################### X-PATHS  ###################################################

team_url = 'vasco'
team_all_name = 'CR Vasco da Gama RJ'

url = f"https://estrelabet.com/ptb/bet/search/{team_url}"

initiation_time = datetime.today().replace(microsecond=0)

print(f"Robô INICIADO em {initiation_time}")

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
    dias_faltantes = driver.find_element(By.XPATH, missing_days).get_attribute('innerHTML')
    horas_faltantes = driver.find_element(By.XPATH, missing_hours).get_attribute('innerHTML') 
    minutos_faltantes = driver.find_element(By.XPATH, missing_minutes).get_attribute('innerHTML') 
    segundos_faltantes = driver.find_element(By.XPATH, missing_seconds).get_attribute('innerHTML') 
    tempo_faltante = horas_faltantes + ':' + minutos_faltantes + ':' + segundos_faltantes
except Exception:
    dias_faltantes = None
    horas_faltantes = None  
    minutos_faltantes = None 
    segundos_faltantes = None 
    tempo_faltante = None

if  team_url.lower() in driver.find_element(By.XPATH, team1).get_attribute('innerHTML').lower():
    chance_derrota = driver.find_element(By.XPATH, probability_of_lose1).get_attribute('innerHTML') + '%'
    chance_vitoria = driver.find_element(By.XPATH, probability_of_victory1).get_attribute('innerHTML')  + '%'
else:
    chance_vitoria = driver.find_element(By.XPATH, probability_of_victory2).get_attribute('innerHTML') + '%'
    chance_derrota = driver.find_element(By.XPATH, probability_of_lose2).get_attribute('innerHTML')  + '%'

if  team_url.lower() in driver.find_element(By.XPATH, team1).get_attribute('innerHTML').lower():
    vitorias_anteriores = driver.find_element(By.XPATH, previous_victory1).get_attribute('innerHTML')
    derrotas_anteriores = driver.find_element(By.XPATH, previous_lose1).get_attribute('innerHTML')
else:
    vitorias_anteriores = driver.find_element(By.XPATH, previous_victory2).get_attribute('innerHTML')
    derrotas_anteriores = driver.find_element(By.XPATH, previous_lose2).get_attribute('innerHTML')

empates_anteriores = driver.find_element(By.XPATH, previous_draw).get_attribute('innerHTML')
chance_empate = driver.find_element(By.XPATH, probability_of_draw).get_attribute('innerHTML')  + '%'
time_adversario = driver.find_element(By.XPATH, opponent_team).get_attribute('innerHTML') 
dia_jogo = driver.find_element(By.XPATH, game_day).get_attribute('innerHTML') 
hora_jogo = driver.find_element(By.XPATH, game_hour).get_attribute('innerHTML') 
encontros_anteriores = int(vitorias_anteriores) + int(derrotas_anteriores) + int(empates_anteriores)

text1 = (f'O próximo jogo do {team_all_name} é no dia {dia_jogo} às {hora_jogo} e vai jogar contra o {time_adversario}.') 
if dias_faltantes != None:
    text2 = (f'Faltam {dias_faltantes} dias e {tempo_faltante} horas para o próximo jogo do {team_all_name}!')
else:
    text2 = (f'Ainda falta ser anunciado o tempo que falta para o jogo')
text3 = (f'A chance de vitória para o {team_all_name} é de {chance_vitoria} porém existe a probabilidade de derrota de {chance_derrota} mas com a possibilidade de empate de {chance_empate}.')
text4 = (f'Os times {team_all_name} e {time_adversario} tiveram {encontros_anteriores} encontros anteriore(s), dentre ele(s)  o {team_all_name} teve {vitorias_anteriores} vitória(s), {derrotas_anteriores} derrota(s) e {empates_anteriores} empate(s).')
separador = '----->---------------------------------------------->------------------------------------------->------------->---------------------------------------------->------------------------------------------->---------------------------------->--------'
dados = [text1, text2, text3, text4, separador]

driver.close()

arquivo = open("proximos_jogos.txt", "a", newline="")
for texto in dados:
    arquivo.write(texto+'\n')
arquivo.close()
