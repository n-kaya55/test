
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

class Pizza():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def pizza(self):
        self.driver.get("https://tomspizzeria.b4a.app/")
        self.driver.maximize_window()
        time.sleep(3)

        #radio button
        orta_boy=self.driver.find_element(By.CSS_SELECTOR,"input[value='Orta']")
        # zeytin=self.driver.find_element(By.CSS_SELECTOR,"input[value='zeytin']")
        # mantar=self.driver.find_element(By.CSS_SELECTOR,"input[value='mantar']")

        print(orta_boy.is_selected()) #tıklı mı?
        orta_boy.click()
        print(orta_boy.is_selected())

        #dropdown Select classı !!
        dropdown=self.driver.find_element(By.ID,"odeme-tipi")
        odeme=Select(dropdown)
        odeme_Tipleri=odeme.options  # web element listesi doner

        for i in odeme_Tipleri:
            print(i.text)
        time.sleep(2)
        odeme.select_by_visible_text("Kredi Kartı")
        time.sleep(2)
        odeme.select_by_index(3)
        time.sleep(3)


pizza=Pizza()
pizza.pizza()