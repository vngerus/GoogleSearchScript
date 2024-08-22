from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Configurar las opciones de Chrome
options = Options()
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome(options=options)

# Navegar a Google
driver.get("https://www.google.com/")

# Realizar una búsqueda de prueba en Google
busqueda = "Con el apagón, que cosas suceden con el apagón?"
search_input = driver.find_element(By.XPATH, '//*[@name="q"]')
search_input.send_keys(busqueda + Keys.RETURN)

# Esperar a que se carguen los resultados
sleep(5)

# Clic en el primer resultado
primer_resultado = driver.find_element(By.XPATH, '(//h3)[1]')
primer_resultado.click()

# Esperar para observar la acción
sleep(5)

# Cerrar el navegador
driver.quit()
