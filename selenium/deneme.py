
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.alert import Alert
import time

class Deneme():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def list(self):
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.maximize_window()
        time.sleep(3)

        #table 
        self.driver.find_element(By.XPATH,"//*[@id='content']/ul/li[41]/a").click()
        liste=self.driver.find_elements(By.XPATH,"//*[@id='table1']/tbody/tr/td[1]")

        for i in liste:
            print( i.text )


    
deneme=Deneme()
deneme.list()