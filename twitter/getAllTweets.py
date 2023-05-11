from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
import time

browser = webdriver.Chrome()

browser.get("https://twitter.com/")

time.sleep(3)

 # bu değişken giriş yapma butonuyla alakalı

giris_yap = browser.find_element("xpath","//*[@id='layers']/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span")

giris_yap.click()

time.sleep(5)

username = browser.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")

username.send_keys("metehanplt17051705@gmail.com")

ilerle = browser.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")

ilerle.click()
time.sleep(5)
password = browser.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")

password.send_keys("mete12345")

ilerlePassword = browser.find_element("xpath","//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/span/span")

ilerlePassword.click()

time.sleep(5)

browser.close()





