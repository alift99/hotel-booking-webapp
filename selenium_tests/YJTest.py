# check landing page works
from pydoc import pager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
import random

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
N_ROOMS_FIELD.send_keys(Keys.ENTER)
time.sleep(0.5)
N_ADULTS_FIELD.send_keys(1)
N_ADULTS_FIELD.send_keys(Keys.ENTER)
time.sleep(0.5)
N_CHILDREN_FIELD.send_keys(1)
N_CHILDREN_FIELD.send_keys(Keys.ARROW_DOWN)
time.sleep(3)
N_CHILDREN_FIELD.send_keys(Keys.ENTER)
time.sleep(0.5)
SUBMIT_BTN.click()
time.sleep(0.5)

time.sleep(5)
SUBMIT_PATH = '//*[@id="selbtn"]'
PREV_PAGE_PATH= '//*[@id="root"]/section/main/div/div/div[1]/div[2]/div/div[3]/div'
PREV_PAGE = driver.find_element(By.XPATH, PREV_PAGE_PATH)

//*[@id="root"]/section/main/div/div/div[2]/div/div/nav/ul
for x in range(10):  
    hotel_choice = random.randint(0,9)
    z = random.randint(0,1)
    if (z==0):
        i = random.randint(1,9)
        PAGINATION_PATH= f'//*[@id="root"]/section/main/div/div/div[2]/div/div/nav/ul/li[{i}]/a'
        NEXT_PAGINATION_PATH = driver.find_element(By.XPATH, PAGINATION_PATH)
        NEXT_PAGINATION_PATH.click()
        time.sleep(3)
        SUBMIT_BUTTON = driver.find_elements(By.XPATH, SUBMIT_PATH)
        SUBMIT_BUTTON[hotel_choice].click()
        time.sleep(1)
        PREV_PAGE.click()
        time.sleep(5)
    
    elif (z==1):
        SUBMIT_BUTTON = driver.find_elements(By.XPATH, SUBMIT_PATH)
        SUBMIT_BUTTON[hotel_choice].click()
        time.sleep(3)
        PREV_PAGE.click()
        time.sleep(5)


    # time.sleep(5)
    # SUBMIT_BUTTON = driver.find_elements(By.XPATH, SUBMIT_PATH)
    # SUBMIT_BUTTON[hotel_choice].click()
    # time.sleep(1)
    # PREV_PAGE.click()
    


