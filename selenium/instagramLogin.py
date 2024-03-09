from instagramUserInfo import email,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

class Instagram:
    def __init__(self,email,password):
        self.browser=webdriver.Chrome()
        self.browserProfile = webdriver.ChromeOptions() #dil secimi
        self.email=email
        self.password=password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        print(usernameInput.text)
        usernameInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

instgrm=Instagram(email,password)
instgrm.signIn()