from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

timeout = 20

option = webdriver.ChromeOptions()
option.add_argument('— incognito')

browser = webdriver.Chrome('./chromedriver',chrome_options = option)

list_of_colleges = ['Maharaja Surajmal Institute of Technology']

for college in list_of_colleges:
    browser.get("https://www.google.com/search?q=" + college + "&start=" + str(10 * 0))
    class_used = 'LrzXr'
    college_data = browser.find_elements_by_class_name(class_used)
    print(college_data[0].text)