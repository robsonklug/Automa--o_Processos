from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# instalar o chromedriver https://chromedriver.chromium.org/downloads
# jogar o aquivo de download na pasta de instalação do Python

# comandos para executar o chrome em segundo plano
chrome_options = Options()
chrome_options.add_argument("--headless")
navegador = webdriver.Chrome(options=chrome_options)
####################################################

#navegador = webdriver.Chrome("chromedriver.exe")
navegador.get("https://www.google.com/")

navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")

navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element(By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value") 


print(cotacao_dolar)

# Passo 2: Pegar a cotação do Euro
navegador.get("https://www.google.com/")
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element(By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_euro)

# Passo 3: Pegar a cotação do Ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",", ".")
print(cotacao_ouro)

navegador.quit()