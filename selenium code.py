# selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:\program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH) # chrome driver PATH for the chrome browser

driver.get('https://techwithtim.net/') # target website

link = driver.find_element_by_link_text('Python Programming') # finds for this element
link.click()

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Beginner Python Tutorials'))) # waits until this element is located
    element.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sow-button-19310003'))) #Waits until this element is located
    element.click() # clicks the element

    driver.back() # Redirects to the previous page
    driver.back()
    driver.back()
except:
    driver.quit() # quits the entire browser
