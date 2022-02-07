import random,time,os
from tkinter import X
from webbrowser import get
cwd = os.getcwd()
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import json

from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
 
firefox_options = webdriver.ChromeOptions()
firefox_options.add_argument('--no-sandbox')
 
firefox_options.headless = True
firefox_options.add_argument('--disable-setuid-sandbox')
firefox_options.add_argument('disable-infobars')
firefox_options.add_argument('--ignore-certifcate-errors')
firefox_options.add_argument('--ignore-certifcate-errors-spki-list')
mobile_emulation = {
    "deviceMetrics": { "width": 1920, "height": 1080, "pixelRatio": 1.8 },
    }
firefox_options.add_argument("--start-maximized")
firefox_options.add_argument('--no-first-run')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument("--disable-infobars")
firefox_options.add_argument("--disable-extensions")
firefox_options.add_argument("--disable-popup-blocking")
firefox_options.add_argument('--log-level=3') 
 
firefox_options.add_argument('--disable-blink-features=AutomationControlled')
firefox_options.add_experimental_option("useAutomationExtension", False)
firefox_options.add_experimental_option("excludeSwitches",["enable-automation"])
firefox_options.add_experimental_option('excludeSwitches', ['enable-logging'])
firefox_options.add_argument('--disable-notifications')

from faker import Faker
fake = Faker('en_US')
from selenium.webdriver.common.action_chains import ActionChains
random_angka = random.randint(100,999)
random_angka_dua = random.randint(10,99)
def xpath_ex(el):
    element_all = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all)

def xpath_fast(el):
    element_all = wait(browser,1).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all)

def xpath_exs(el):
    element_all = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    element_all.send_keys(Keys.ENTER)
    
def xpath_long(el):
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all) 

def xpath_type(el,word):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(word)
def xpath_id(el,word):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'//input[@{el}]'))).send_keys(word)
def login(datas):
    data = datas.split("|")
    email = data[0]
    password = data[1]
    global browser
    firefox_options.add_experimental_option("mobileEmulation", mobile_emulation)
    firefox_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")
    browser = webdriver.Chrome(options=firefox_options,executable_path=f"{cwd}\\chromedriver.exe")
    datas = open(f"{cwd}\\data.txt","r")
    datas = datas.read()
    get_data = datas.split("|")
    url = get_data[0]
    quantity = get_data[1]
    browser.get(url)
    xpath_long('//a[@title="LOGIN"]')
    print(f"[{time.strftime('%d-%m-%y %X')}] [{email}] Login")
    xpath_type('//input[@id="username"]',email)
    xpath_type('//input[@name="password"]', password)
    xpath_type('//input[@name="password"]', Keys.ENTER)
    
     
     
    try:
        xpath_ex('//button[@class="button-quick-tour"]')
         
    except:
        pass
    #browser.save_screenshot("Login.png")
    for i in range(0,int(quantity)):
        xpath_exs('//button[@class="btn-qty btn-right"]')
     
    xpath_long('//*[text()="BUY NOW"]')
    print(f"[{time.strftime('%d-%m-%y %X')}] [{email}] Trying to Buy!")
    xpath_long('//*[text()="GO TO SHOPPING BAG"]')
    #browser.save_screenshot("Buy.png")
    
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '(//div[@class="apply-title"])[2]')))
    browser.execute_script("arguments[0].scrollIntoView();", element_all)
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '(//a[text()="CHECKOUT"])[2]')))
    #browser.save_screenshot("Checkout.png")
    browser.execute_script("arguments[0].click();", element_all) 
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//button[text()=" Proceed to payment "]')))
    #browser.save_screenshot("Checkout-2.png")
    browser.execute_script("arguments[0].click();", element_all) 
    print(f"[{time.strftime('%d-%m-%y %X')}] [{email}] Waiting Voucher!")
    while True:
        try:
            xpath_long('//span[text()="Mandiri Virtual Account"]')
            xpath_fast('//*[contains(text()," Apply ")]')
            print(f"[{time.strftime('%d-%m-%y %X')}] [{email}] Voucher Found!")
            break
        except:
            pass
    print(f"[{time.strftime('%d-%m-%y %X')}] [{email}] Get Virtual Account!")
    xpath_long('//*[text()="PLACE ORDER"]')
    #browser.save_screenshot("Place_Order.png")
    get_codeva = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//p[@class="text text-bigger"]'))).text
    get_codeva = get_codeva.split("\n")
    get_codeva = get_codeva[0]
    get_price = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//h3[@class="amount"]'))).text
    print(f"[{time.strftime('%d-%m-%y %X')}] [{email}] {get_codeva} - {get_price}")
    
    
if __name__ == '__main__':
    print("[*] Auto Checkout Sociolla")
    global price
    url = input('[*] Input Link: ')
    quantity = int(input('[*] Input Quantity: '))
    quantity = quantity - 1
    with open('data.txt','w') as f: f.write(f'{url}|{quantity}\n')
    myfile = open(f"{cwd}\\list.txt","r")
    list_account = myfile.read()
    list_accountsplit = list_account.split("\n")
    with Pool(len(list_accountsplit)) as p:  
        p.map(login, list_accountsplit)