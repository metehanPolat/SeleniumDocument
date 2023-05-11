from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://www.instagram.com/")

time.sleep(2)

username = browser.find_element("name","username") # ismiyle almamın nedeni instegram xpath ini her yenilendiğinde değiştiriyor. Bu yüzden bu şekilde aldım.
password = browser.find_element("name","password")

username.send_keys("metehanplt1705@gmail.com")
password.send_keys("mete12345")

loginButton = browser.find_element("xpath","//*[@id='loginForm']/div/div[3]")

loginButton.click()

time.sleep(20)

try:
    TurnOnButton = browser.find_element("xpath","//*[@id='mount_0_0_f5']/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
    TurnOnButton.click()
except:
    print("şimdilik yok sayıldı")

profilButton = browser.find_element("xpath","//*[@id='mount_0_0_We']/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/div/a/div/div[2]/div/div")

profilButton.click()

buttons = browser.find_element(By.CSS_SELECTOR,)





time.sleep(20)










browser.close()

