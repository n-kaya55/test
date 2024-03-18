from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert
import time

class WaitAlert():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def wait(self):
        self.driver.get("https://pynishant.github.io/Selenium-python-waits.html")
        self.driver.maximize_window()
      
        tryit=self.driver.find_element(By.XPATH, "/html//button[.='Try it']").click()
        WebDriverWait(self.driver, 45).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'CLICK ME')]")))
        clickme = self.driver.find_element(By.XPATH, "//button[contains(text(), 'CLICK ME')]").click()
        WebDriverWait(self.driver,3).until(expected_conditions.alert_is_present())
        alert=Alert(self.driver)
        alert.accept()
        time.sleep(3)





waitAlert=WaitAlert()
waitAlert.wait()