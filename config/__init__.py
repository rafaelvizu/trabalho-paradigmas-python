from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Config:
    navegador = webdriver.Chrome(ChromeDriverManager().install())
    service = Service(ChromeDriverManager().install())

    @staticmethod
    def get_navegador():
        return Config.navegador

    @staticmethod
    def get_service():
        return Config.service
