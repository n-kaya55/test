from tobetoInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

class Tobeto:
    def __init__(self,username,password):
        self.driver=webdriver.Chrome()
        self.username=username
        self.password=password    


    def login(self):
        self.driver.get("https://tobeto.com/")
        self.driver.maximize_window()
        time.sleep(3)

        self.driver.find_element(By.XPATH,"//div[@id='__next']//section[@class='web-header']/nav//a[@href='/giris']").click()
        time.sleep(3)

        username= self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]")
        username.send_keys(self.username)

        password=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]")
        password.send_keys(self.password)
        time.sleep(3)

        self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button").click()
        time.sleep(3)

        self.driver.save_screenshot("tobeto.png")
        time.sleep(3)

        welcome=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h3")
        print(welcome.text)

        expected_mesaj="TOBETO'ya hoş geldiniz"
        
        # if expected_mesaj == welcome.text:
        #     print("basarili")
        # else:
        #     print("yanlıs mesaj")

        assert expected_mesaj==welcome.text ,"hata"

        


tobeto=Tobeto(username,password)
tobeto.login()