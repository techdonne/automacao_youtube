import time 

from selenium import webdriver

from selenium.webdriver.common.keys import Keys 

class bot():
    def __init__(self):
        service = webdriver.chrome.service.Service(r'C:\Users\danni\OneDrive\Documentos\GitHub\automacao_youtube\chromedriver.exe')
        self.drive = webdriver.Chrome(service=service)


if __name__ == '__main__':
    bot = bot()