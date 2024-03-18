
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class Alerttt():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def alert(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.maximize_window()
        time.sleep(3)

        alert=Alert(self.driver)
        # 1. BUTTON
        # self.driver.find_element(By.XPATH, "//div[@id='content']//ul//button[.='Click for JS Alert']").click()
        # WebDriverWait(self.driver,3).until(expected_conditions.alert_is_present())
        #alert.accept()

        # expected_message="You successfully clicked an alert"
        # mesaj=self.driver.find_element(By.XPATH,"//*[@id='result']")
        # assert expected_message==mesaj.text 

        # 2. BUTTON

        # self.driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[2]/button").click()
        # WebDriverWait(self.driver,3).until(expected_conditions.alert_is_present())
        # alert.dismiss()
        # time.sleep(3)

        # 3. button

        self.driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[3]/button").click()
        WebDriverWait(self.driver,3).until(expected_conditions.alert_is_present())
        alert.send_keys("hello world")
        time.sleep(3)

        mesaj=self.driver.find_element(By.XPATH,"//*[@id='result']")
        print(mesaj.text)


alert=Alerttt()
alert.alert()