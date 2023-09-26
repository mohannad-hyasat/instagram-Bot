from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException


username = "<your username here>"
password = "<your password here>"
path = "https://www.instagram.com/accounts/login/?source=auth_switcher"
account = "<name of account you want to follow people that are following that account>"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.get(path)
time.sleep(2)

username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(username)
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)
time.sleep(5)

search_button = driver.find_element(By.XPATH, "(//a[@role='link'])[3]")
search_button.click()
time.sleep(1)

search_bar = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
search_bar.send_keys(account)
search_bar.send_keys(Keys.RETURN)
time.sleep(1)

result = driver.find_element(By.CSS_SELECTOR, "a[role='link'][href='/chefsteps/']")
result.click()
time.sleep(4)

followers_button = driver.find_element(By.CSS_SELECTOR, "a[href='/chefsteps/followers/']")
followers_button.click()
time.sleep(2)

modal = driver.find_element(By.XPATH, "(//div[@class='_aano'])[1]")

for i in range(10):
    #In this case we're executing some Javascript, that's what the execute_script() method does.
    #The method can accept the script as well as a HTML element.
    #The modal in this case, becomes the arguments[0] in the script.
    #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    time.sleep(2)
all_buttons = driver.find_elements(By.XPATH, "//body/div/div/div/div/div/div/div/div/div/div/div/div[@role='dialog']/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/button")

for button in all_buttons:
    try:
        button.click()
        time.sleep(1)
    except ElementClickInterceptedException:
        cancel_button = driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")
        cancel_button.click()
