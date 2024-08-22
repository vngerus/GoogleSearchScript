from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

# Configurar las opciones de Chrome.
options = Options()
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")

# Realizar la búsqueda.
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys("Yuri El Apagón YouTube" + Keys.RETURN)

try:
    # Esperar a que aparezca el enlace de YouTube.
    video_link = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "youtube.com/watch")]'))
    )

    # Desplazar hasta el enlace para asegurarse de que es visible.
    driver.execute_script("arguments[0].scrollIntoView(true);", video_link)
    sleep(1)  # Esperar un segundo para asegurar que el scroll se complete.

    # Hacer clic en el enlace usando JavaScript para evitar intercepciones.
    driver.execute_script("arguments[0].click();", video_link)

    # Esperar un momento para asegurarse de que el video comience a reproducirse.
    sleep(10)

except Exception as e:
    print(f"An error occurred: {str(e)}")
    with open("error_page.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
finally:
    # Cerrar el navegador después de esperar un tiempo.
    sleep(10)
    driver.quit()
