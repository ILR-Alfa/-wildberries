from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from openpyxl import load_workbook, Workbook


url = "https://vkusnoitochka.ru/menu"
firefox_options = FirefoxOptions()
firefox_options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
firefox_options.set_preference("permissions.default.geo", 2) 
firefox_options.set_preference("geo.enabled", False)
firefox_options.add_argument("--headless")


service = FirefoxService(r"D:\projects\Parser wildberis\driver\geckodriver.exe")


driver = webdriver.Firefox(service=service, options=firefox_options)
wait = WebDriverWait(driver, 10)