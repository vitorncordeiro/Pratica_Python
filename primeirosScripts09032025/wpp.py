from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.wait import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.common.keys import Keys #type: ignore
from selenium.webdriver.common.action_chains import ActionChains #type: ignore

navegador = webdriver.Firefox()
navegador.get("https://web.whatsapp.com/")
navegador.maximize_window() #maximiza a tela do navegador
try:
    espera = WebDriverWait(navegador, 150) #seta o tempo de espera
    h1Conversas = espera.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Conversas")]')))
    # ^ define qual elemento vai ser o parametro para continuar o código. Nesse caso, é o h1 escrito "Conversas" do whatsapp, dando 150 segundos para o usuário escanear o qr code e entrar nessa pagina. O XPATH rígido é ruim, por isso tem esse aí que busca o "Conversas" escrito
except TimeoutError: #TimeoutError é o erro q aparece caso o tempo do wait chegue a zero e o usuário não scaneou 
    print('O tempo para escanear o QR Code expirou!')

divConversaContato = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[3]/div/div[3]/div[1]/div/div/div[8]/div/div/div/div[2]')
divConversaContato.click()
divCaixaDeTextoConversa = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]')
divCaixaDeTextoConversa.click()
#Digita pausadamente pq o div com editable=true da problema com digitação do .send_keys() padrão.
ActionChains(navegador)\
    .send_keys("Teste")\
    .pause(0.1)\
    .send_keys(Keys.ENTER)\
    .perform()