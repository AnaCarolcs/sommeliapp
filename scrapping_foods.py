from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import os

alimentos = ['lasanha', 'cachorro quente', 'feijoada', 'rabanada', 'rabada']
if not os.path.exists('images/'):
    os.makedirs("images/")

driver = webdriver.Chrome('./chromedriver') # Esse arquivo chromedriver tem que ser compatível com o SO usado, caso contrário vai dar erro
for comida in alimentos:
    driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')

    box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
    box.send_keys(comida)
    box.send_keys(Keys.ENTER)

    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            for i in range(1, 10): # caso precise de mais imagens aumenta aqui
                try:
                    driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot(f"images/{comida}({i}).png")
                except:
                    pass
            break
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height
