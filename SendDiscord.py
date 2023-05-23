from imaplib import Commands
from pydoc import cli
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
import discord
import sys

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://hehplanning2022.umons.ac.be/invite")
sleep(1)

element = driver.find_element(By.CSS_SELECTOR, ".ObjetSaisie_cont")
element.click()
sleep(0.7)
element = driver.find_element(By.ID, "GInterface.Instances[1].Instances[1]_62")
element.click()
element = driver.find_element(By.ID, "GInterface.Instances[1].Instances[2].bouton")
sleep(0.7)
element.click()

#Groupe
sleep(0.7)
element = driver.find_element(By.ID, "GInterface.Instances[1].Instances[2]_2")
element.click()
sleep(0.7)


#Bouton Général
element = driver.find_element(By.CSS_SELECTOR, "I.icon_afficher_cours_TD_plus_promo.bt-activable.btnImage.OmbreFocus")
element.click()
sleep(0.7)


driver.get_screenshot_as_file("photo/1.png")

#slider
element = driver.find_element(By.ID, "GInterface.Instances[1].Instances[2].bouton")
sleep(0.7)
element.click()
sleep(0.7)

#Groupe2
element = driver.find_element(By.ID, "GInterface.Instances[1].Instances[2]_3")
element.click()
sleep(0.7)
driver.get_screenshot_as_file("photo/2.png")

#slider
element = driver.find_element(By.ID, "GInterface.Instances[1].Instances[2].bouton")
sleep(0.7)
element.click()
sleep(0.7)

#Groupe3
element = driver.find_element(By.ID, "GInterface.Instances[1].Instances[2]_5")
element.click()
sleep(0.7)
driver.get_screenshot_as_file("photo/3.png")

#slider
element = driver.find_element(By.ID, "GInterface.Instances[1].Instances[2].bouton")
sleep(0.7)
element.click()
sleep(0.7)

#Groupe4
element = driver.find_element(By.ID, "GInterface.Instances[1].Instances[2]_6")
element.click()
sleep(0.7)
driver.get_screenshot_as_file("photo/4.png")



driver.close()
#myScreenshot = pyautogui.screenshot()
#myScreenshot.save(r'zizi.png')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
     
    ch = client.get_channel('[Channel]')
    await ch.purge(limit=100)
    await ch.send("Groupe 1 Dev :")
    await ch.send(file=discord.File("photo/1.png"))
    await ch.send("Groupe 2 Dev :")
    await ch.send(file=discord.File("photo/2.png"))
    await ch.send("Groupe 1 Sécu :")
    await ch.send(file=discord.File("photo/3.png"))
    await ch.send("Groupe 2 Sécu :")
    await ch.send(file=discord.File("photo/4.png"))
    sys.exit()




client.run('[Token]')