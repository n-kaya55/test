
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self,email,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.email=email
        self.password=password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(3)


x=Twitter("min.kids.store34@gmail.com","minasilivri-1992")
x.signIn()


    