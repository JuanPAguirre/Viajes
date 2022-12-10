from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.maximize_window()

#time.sleep(1)

driver.get("https://www.viajesexito.com/")
#time.sleep(1)

#oferta =  driver.find_element(By.XPATH, '/html/body/div[36]/div/div/div[1]/button/span')
#oferta.click()
#Este oferta de arriba es porque en ocasiones aparece un anuncio entonces es para tratar de prevenirlo y cerrarlo, aunque en ocasiones no aparece y por el tiempo puede generar error

paquetes =  driver.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[2]/a/p')
paquetes.click()

time.sleep(1)

destino =  driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div/div/input')
destino.click()
destino.send_keys("Punta Cana, Republica Dominicana (PUJ)")

time.sleep(1)

fechaIda = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/input')
fechaIda.click()

time.sleep(1)

diaIda = driver.find_element(By.XPATH, '/html/body/div[21]/div[1]/table/tbody/tr[3]/td[3]/a')
diaIda.click()

time.sleep(1)

diaVue = driver.find_element(By.XPATH, '/html/body/div[21]/div[1]/table/tbody/tr[4]/td[4]/a')
diaVue.click()

time.sleep(1)

habitacion = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div/p')
habitacion.click()

time.sleep(1)

adultos = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div/span[2]/button')
adultos.click()

time.sleep(1)

aplicar = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/button')
aplicar.click()

time.sleep(1)

buscar = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/a')
buscar.click()

time.sleep(1)

precio1 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/a/div/div[2]')
precio2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div[3]/a/div/div[2]')
precio3 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div[4]/a/div/div[2]')
print("----------Primer precio----------")
print(precio1)
print("----------Segundo precio----------")
print(precio2)
print("----------Tercer precio----------")
print(precio3)

time.sleep(1)

aerolinea =  driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
aerolinea.click()
aerolinea.send_keys("Avianca (AV)")

time.sleep(1)

buscar2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
buscar2.click()

time.sleep(3)

driver.quit()
