import os
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import keyboard
import time

Permission = Options()
Permission.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })

lec = input("enter sub name : ")

def mainfunc(num):
    if(num==0):
        print("Do you want to record screen")
        ans = input("yes/no : ")
        if ans=="yes":
            print("This lec will be recorded")
            driver.maximize_window()
            keyboard.press_and_release('Alt+win+r') 

        else:
            print("Bot starting in 5 sec...")
        t=4
        while t > 0:
            print(f"starting in {t} ..." )
            t -= 1
            time.sleep(1)
        print("started")

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=Permission)  #chrome_options=block
    url="https://meetingsapac10.webex.com/webappng/sites/meetingsapac10/meeting/download/e78c8f71917e419dbc247a2c37c51d5f?siteurl=meetingsapac10&MTID=md9fe6772ba1c385563e2d5aac4c9bdf4"
    driver.minimize_window()
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.XPATH , '//*[@id="push_download_join_by_browser"]').click()  #join from browser
    time.sleep(3)
    driver.switch_to.frame("thinIframe")
    username = "68 vishal"
    time.sleep(1)
    driver.find_element(By.XPATH , '//*[@id="meetingSimpleContainer"]/div[3]/div[2]/div/input').send_keys(username)  # myname
    driver.find_element(By.XPATH , '//*[@id="guest_next-btn"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH , '//*[@id="meetingSimpleContainer"]/div[3]/div[2]/div[1]/div/div/button').click()  #disable mic
    driver.find_element(By.XPATH , '//*[@id="interstitial_join_btn"]').click() # join
    print("done till here")
    time.sleep(2) # lecture end time
    driver.quit()

def again():
    if lec=="oop":
        mainfunc(1)

    elif lec=="wp":
        mainfunc(1)

    elif lec=="mm":
        mainfunc(1)

    elif lec=="maths":
        mainfunc(1)

    else:
        mainfunc(1)

mainfunc(0)
again()

os.system("shutdown /s /t 1")