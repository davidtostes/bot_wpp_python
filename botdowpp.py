from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#INICIALIZA O NAVEGADOR
driver= webdriver.Chrome()

# Abre a pagina web e o tempo necessário de aguarde:
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver,100)

# Contato alvo que irá receber a mensagem + mensagem que será enviada:
target='"Meu Alvo"'
message="Minha mensagem"

contact_path='//span[contains(@title,'+ target +')]'
contact=wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
contact.click()
message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
message_box=wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))

#Numero de vezes que a mensagem será enviada:
for x in range(1):
    message_box.send_keys(message + Keys.ENTER)
    #intervalo de mensagens:
    time.sleep(3)



