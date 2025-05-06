from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.wait import WebDriverWait # type: ignore
import time

navegador = webdriver.Firefox()
navegador.maximize_window()
canalYt = navegador.get('https://www.youtube.com/@BroxadaSinistra') 
time.sleep(10) # espera os botões carregarem
botoesNavNoCanal = navegador.find_elements(By.CLASS_NAME, 'yt-tab-shape-wiz__tab') # pega as div que tem os botões das modalidades do canal, "Ao Vivo", 'Vídeos', "Playlists", etc.
for botao in botoesNavNoCanal:
    if 'Ao vivo' in botao.text:
        botao.click()
        print('cliquei')
        break
    else:
        print('não cliquei')
        continue
time.sleep(10)
videosAoVivo = navegador.find_elements(By.ID, 'thumbnail')
for video in videosAoVivo:
    video.click()
    print('cliquei no video')
    break


