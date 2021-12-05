from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
# import pytesseract as tess
import time
import datetime
from selenium.webdriver.chrome.options import Options
import keyboard



# tess.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"



Permission = Options()

# opt.add_argument("--disable-infobars")
# opt.add_argument("start-maximized")
# opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
Permission.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })


def mainfunc():
  driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=Permission)  #chrome_options=block
  url="https://meetingsapac10.webex.com/webappng/sites/meetingsapac10/meeting/download/e78c8f71917e419dbc247a2c37c51d5f?siteurl=meetingsapac10&MTID=md9fe6772ba1c385563e2d5aac4c9bdf4"
  driver.get(url)
  driver.maximize_window()
  time.sleep(2)
  driver.find_element(By.XPATH , '//*[@id="push_download_join_by_browser"]').click()  #join from browser
  time.sleep(5)

  driver.save_screenshot("meet.png")
  img = Image.open("meet.png")

  680,480 , 820 ,525
  area = (680,480,820,525)
  crop_img = img.crop(area)
  crop_img.save("meetcaptcha.png")

  captcha_img = Image.open('meetcaptcha.png')
  # captcha = tess.image_to_string(captcha_img)
  # print(captcha)


  driver.switch_to.frame("thinIframe")
  username = "your_name"
  precap = 'fgdfgd' # predefined captcha 
  driver.find_element(By.XPATH , '//*[@id="meetingSimpleContainer"]/div[3]/div[2]/div/input').send_keys(username)  # myname
  driver.find_element(By.XPATH , '//*[@id="meetingSimpleContainer"]/div[3]/div[3]/div/div[1]/div/input').send_keys(precap)  # captcha
  time.sleep(1)   
  driver.find_element(By.XPATH , '//*[@id="guest_next-btn"]').click()
  time.sleep(2)
  driver.find_element(By.XPATH , '//*[@id="meetingSimpleContainer"]/div[3]/div[2]/div[1]/div/div/button').click()  #disable mic
  driver.find_element(By.XPATH , '//*[@id="interstitial_join_btn"]').click() # join
  time.sleep(1)
  driver.find_element(By.XPATH , '/html/body/div[5]/div/div/div/div[3]/div/button[1]').click() # join without camera
  time.sleep(5)
  driver.find_element(By.XPATH , '//*[@id="layoutdomid"]/div[1]/div[3]/div[2]/div[4]/div/button[2]').click()
  time.sleep(1)
  driver.find_element(By.XPATH,'//*[@id="layoutdomid"]/div[1]/div[1]/div/div[1]/div/span[1]').click()
  
  time.sleep(3300) # lecture end time

  driver.quit()


# def record():
#     print("Recording will start in 15 second")
#     keyboard.press_and_release('Alt+win+r')   



# print("Do you want to record screen")
# ans = input("yes/no : ")

# if ans=="yes":
#   # record()
#   mainfunc()

mainfunc()

# else:
#   # mainfunc()
#   print("Bot starting in 5 sec...")
#   t=4
#   while t > 0:
#         print(f"starting in {t} ..." )
#         t -= 1
#         time.sleep(1)
#   print("started")
#   mainfunc()


# x = datetime.datetime.now()
# y= datetime.datetime.now()
# print(x.strftime("%X"))
# print(y.strftime("%p"))

# 07
# 08
# 8:10
# 09
# 9:10
# 10


# mainfunc()
