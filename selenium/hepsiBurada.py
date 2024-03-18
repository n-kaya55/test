import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hepsiburada.com/")
time.sleep(3)
#WebDriverWait(driver,5).until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR,"button#onetrust-accept-btn-handler"))
cookie=driver.find_element(By.CSS_SELECTOR,"button#onetrust-accept-btn-handler").click()
