from tobetoInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.alert import Alert
import time

class Deneme:
    def __init__(self,username,password):
      self.driver = webdriver.Chrome()
      self.username=username
      self.password=password
   

    def login(self):
        self.driver.get("https://tobeto.com/")
        self.driver.maximize_window()
        
        time.sleep(3)

        self.driver.find_element(By.XPATH,"//*[@id='__next']/div/section[1]/nav/div/div/a[1]").click()
        
        time.sleep(3)

        username=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]")
        username.send_keys(self.username)
        password=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]")
        password.send_keys(self.password)
        time.sleep(3)

        girisYap=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")
        girisYap.click()

        self.driver.save_screenshot("screenshot.png")
        time.sleep(3)

        
        

        

       


    

      


deneme=Deneme(username,password)
deneme.login()
