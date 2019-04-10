#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import random
timeout = 5

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print "Carregando Log in..."

driver.find_element_by_xpath("//input[@name='username']").send_keys("USERNAME")
driver.find_element_by_xpath("//input[@name='password']").send_keys("PASSWORD")
driver.find_element_by_xpath("//button[contains(.,'Entrar')]").click()
sleep( 60 )
try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print "Nome Armazenado..."
driver.get("https://www.instagram.com/p/LINK/")


# file handle fh
f = open("mentions.txt", "r")
for x in f:
    
        driver.find_element_by_xpath("//span[@aria-label='Comentar']").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//form[@class='X7cDz']//textarea[contains(@placeholder,'Adicione')]"))).send_keys(x)
        driver.find_element_by_xpath("//textarea[contains(@aria-label,'Adicione')]").send_keys(Keys.ENTER)
        print "Marcado:",x
        sleep( 60 )