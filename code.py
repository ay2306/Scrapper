from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
import time
sys.stdin = open('colleges.txt','r')
sys.stdout = open('address.txt','w')
timeout = 20
PROXY = [
    "13.229.85.9:8118",
    "203.205.34.52:25",
    "103.81.12.1:57803",
    "103.217.78.1:41719",
    "177.67.10.15:48314",
    "78.30.214.81:52144",
    "117.54.250.2:60791",
    "194.150.143.7:37343",
    "123.49.41.129:23500",
    "95.161.231.10:32189",
    "45.120.119.55:59565",
    "121.120.241.9:61786",
    "145.239.169.40:1080",
    "178.76.69.132:45014",
    "78.186.237.112:53281",
    "103.229.177.51:57959",
    "140.227.213.165:3128",
    "102.176.160.29:48541",
    "124.41.211.212:23500",
    "177.105.192.126:55715"
    ]
req = 1
current = 0
# browser.get('https://www.whatismyip.com/my-ip-information/')
option = webdriver.ChromeOptions()
# option.add_argument('— incognito')
# option.add_argument('--proxy-server=%s'%PROXY[1])
browser = webdriver.Chrome('./chromedriver',chrome_options = option)
while(1):
    # if(req == 30):
    #     req = 0
    #     browser.close()
    #     current = current+1
    #     if current == len(PROXY):
    #         current = 0
    #     newoption = webdriver.ChromeOptions()
    #     # option.add_argument('— incognito')
    #     newoption.add_argument('--proxy-server=%s'%PROXY[current])
    #     browser = webdriver.Chrome('./chromedriver',chrome_options = newoption)
    try:
        college = input()
        req = req+1
        browser.get("https://www.google.com/search?q=" + college + "&start=" + str(10 * 0))
        class_used = 'LrzXr'
        college_data = browser.find_elements_by_class_name(class_used)
        if(len(college_data) > 0):
            print(college + '\t' + college_data[0].text)
        time.sleep(1)
    except EOFError:
        break

# browser.get('https://free-proxy-list.net/')
# time.sleep(5)
# data = browser.find_elements_by_class_name('odd')
# print(data)
# print(data[0])
# page = 1
# while(pag)