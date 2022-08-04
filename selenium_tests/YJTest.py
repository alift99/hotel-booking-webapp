# check landing page works
from pydoc import pager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
import random
import math

DESTINATION_PATH = '//*[@id="destination"]' 
DATE_1_PATH = '//*[@id="date"]'
DATE_2_PATH = '//*[@id="root"]/section/main/div/div/div[2]/div/div/div/form/div[2]/div/div/div/div/div/div/div[3]/input'
NUM_ROOMS_PATH = '//*[@id="numberOfRoom"]'
NUM_ADULTS_PATH = '//*[@id="numberOfAdult"]'
NUM_CHILDREN_PATH = '//*[@id="numberOfChild"]'
SUBMIT_BTN_PATH = '//*[@id="root"]/section/main/div/div/div[2]/div/div/div/form/div[4]/div/button/span'
WARNING_HOLDER_PATH = '/html/body/div[5]/div/div'

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()
driver.get('http://localhost:3000/')
time.sleep(3)

# link = driver.find_element(By.LINK_TEXT, 'Get Started Now')
# link.click()
# time.sleep(3)
# driver.back()
# time.sleep(3)
link = driver.find_element(By.LINK_TEXT, 'Get Started Now')
link.click()


DESTINATION_FIELD = driver.find_element(By.XPATH, DESTINATION_PATH)
DATE_1_FIELD = driver.find_element(By.XPATH, DATE_1_PATH)
DATE_2_FIELD = driver.find_element(By.XPATH, DATE_2_PATH)
N_ROOMS_FIELD = driver.find_element(By.XPATH, NUM_ROOMS_PATH)
N_ADULTS_FIELD = driver.find_element(By.XPATH, NUM_ADULTS_PATH)
N_CHILDREN_FIELD = driver.find_element(By.XPATH, NUM_CHILDREN_PATH)
SUBMIT_BTN = driver.find_element(By.XPATH, SUBMIT_BTN_PATH)


DESTINATION_FIELD.send_keys('Singapore, Singapore')
time.sleep(0.5)
DESTINATION_FIELD.send_keys(Keys.ENTER)
DATE_1_FIELD.send_keys('2022-08-05')
DATE_2_FIELD.send_keys('2022-09-01')
N_ROOMS_FIELD.send_keys(1)
time.sleep(3)
N_ROOMS_FIELD.send_keys(Keys.ENTER)
time.sleep(0.5)
N_ADULTS_FIELD.send_keys(1)
time.sleep(3)
N_ADULTS_FIELD.send_keys(Keys.ENTER)
time.sleep(0.5)
N_CHILDREN_FIELD.send_keys(1)
N_CHILDREN_FIELD.send_keys(Keys.ARROW_DOWN)
N_CHILDREN_FIELD.send_keys(Keys.ARROW_DOWN)
time.sleep(3)
N_CHILDREN_FIELD.send_keys(Keys.ENTER)
time.sleep(0.5)
SUBMIT_BTN.click()
time.sleep(0.5)

time.sleep(5)
SUBMIT_PATH = '//*[@id="selbtn"]'
HOTEL_DETAILS_PATH = '//*[@id="root"]/section/main/div/div/div[2]/div/div/div[3]/div/div/h3/b'
PREV_PAGE_PATH= '//*[@id="root"]/section/main/div/div/div[1]/div[2]/div/div[3]/div'
PREV_PAGE = driver.find_element(By.XPATH, PREV_PAGE_PATH)

HOTEL_NUMBER_PATH = '//*[@id="root"]/section/main/div/div/div[2]/div/div/p/b'
HOTEL_NUMBER = driver.find_element(By.XPATH, HOTEL_NUMBER_PATH).get_attribute('textContent')
HOTEL_NUMBER_SLICE = int(HOTEL_NUMBER[20:22])
NUMBER_OF_PAGE = math.ceil(HOTEL_NUMBER_SLICE/10)


# PAGINATION_PATH_2 = '//*[@id="root"]/section/main/div/div/div[2]/div/div/nav/ul'
# PAGINATION_LENGTH = len(PAGINATION_PATH_2)
# print(PAGINATION_LENGTH)
# NEXT_PAGINATION_PATH = driver.find_element(By.XPATH, PAGINATION_PATH_2[0])
# NEXT_PAGINATION_PATH.click()

lastpage = False

for x in range(10):  
    hotel_choice = random.randint(0,9)
    z = random.randint(0,1)
    HOTEL_NUMBER_PATH = '//*[@id="root"]/section/main/div/div/div[2]/div/div/p/b'
    HOTEL_NUMBER = driver.find_element(By.XPATH, HOTEL_NUMBER_PATH).get_attribute('textContent')
    HOTEL_NUMBER_SLICE = int(HOTEL_NUMBER[20:22])
    NUMBER_OF_PAGE = math.ceil(HOTEL_NUMBER_SLICE/10)
    LASTPAGE_NUMBER = HOTEL_NUMBER_SLICE % 10
    i = random.randint(1,NUMBER_OF_PAGE)
    
    # For Pagination
    if (z==0):
        
        
        PAGINATION_PATH= f'//*[@id="root"]/section/main/div/div/div[2]/div/div/nav/ul/li[{i}]/a'
        NEXT_PAGINATION_PATH = driver.find_element(By.XPATH, PAGINATION_PATH)
        NEXT_PAGINATION_PATH.click()
        time.sleep(5)
        try:
            assert driver.find_elements(By.XPATH, PAGINATION_PATH)
            print('Pagination Passed')
        except AssertionError:
            print('Pagination Failed')
       
    
    # For Hotel Select
    elif (z==1):
        if (i == NUMBER_OF_PAGE):
            lastpage = True
        else:
            lastpage = False

        if (lastpage == False):
            SUBMIT_BUTTON = driver.find_elements(By.XPATH, SUBMIT_PATH)
            SUBMIT_BUTTON[hotel_choice].click()
            time.sleep(3)
            try:
                assert driver.find_element(By.XPATH, HOTEL_DETAILS_PATH)
                print('Select Hotel Passed')
            except AssertionError:
                print('Select Hotel Failed')
            PREV_PAGE.click()
            time.sleep(5)
            try:
                assert driver.find_element(By.XPATH, HOTEL_NUMBER_PATH)
                print('Back Page Passed')
            except AssertionError:
                print('Back Page Failed')
            
        else:
            hotel_choice = random.randint(0,LASTPAGE_NUMBER-1)
            SUBMIT_BUTTON = driver.find_element(By.XPATH, SUBMIT_PATH)
            SUBMIT_BUTTON[hotel_choice].click()
            time.sleep(3)
            try:
                assert driver.find_elements(By.XPATH, HOTEL_DETAILS_PATH)
                print('Select Hotel Passed')
            except AssertionError:
                print('Select Hotel Failed')
            PREV_PAGE.click()
            time.sleep(5)
            try:
                assert driver.find_element(By.XPATH, HOTEL_NUMBER_PATH)
                print('Back Page Passed')
            except AssertionError:
                print('Back Page Failed')
            



    # time.sleep(5)
    # SUBMIT_BUTTON = driver.find_elements(By.XPATH, SUBMIT_PATH)
    # SUBMIT_BUTTON[hotel_choice].click()
    # time.sleep(1)
    # PREV_PAGE.click()
    

    


