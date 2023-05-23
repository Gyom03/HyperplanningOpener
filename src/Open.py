from selenium.webdriver.firefox.options import Options
from imaplib import Commands
from pydoc import cli
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

firefox_options = Options()
firefox_options.set_preference('detach', True)
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://hehplanning2022.umons.ac.be/invite")

found = False

while found == False :
    try:
        sleep(0.1)
        element = driver.find_element(By.CSS_SELECTOR, ".ObjetSaisie_cont")
        found = True
    except:
        continue
    break

sleep(0.2)
found = False
element.click()

while found == False :
    try:
        sleep(0.1)
        element = driver.find_element(By.ID, "GInterface.Instances[1].Instances[1]_62")
        found = True
    except:
        continue
    break

sleep(0.2)
found = False
element.click()

while found == False :
    try:
        sleep(0.1)
        element = driver.find_element(By.ID, "GInterface.Instances[1].Instances[2].bouton")
        found = True
    except:
        continue
    break

sleep(0.2)
found = False
element.click()

while found == False :
    try:
        sleep(0.1)
        element = driver.find_element(By.ID, "GInterface.Instances[1].Instances[2]_5")
        found = True
    except:
        continue
    break
sleep(0.2)
found = False
element.click()

while found == False :
    try:
        sleep(0.1)
        element = driver.find_element(By.CSS_SELECTOR, "I.icon_afficher_cours_TD_plus_promo.bt-activable.btnImage.OmbreFocus")
        found = True
    except:
        continue
    break
sleep(0.2)
found = False
element.click()

while 1 == 1:
    try:
        myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'id_body')))
        print ("oui!")
        sleep(0.5)
    except TimeoutException:
        exit()