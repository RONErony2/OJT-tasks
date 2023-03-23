# 1. Write an automation script using seleniumn which should choose the desired product from any
# e-commerce site such as flipkart or amazon add it to the cart (make sure you should also login using
# the automation script) and then redirect you to the payment page. As payment will require to get
# OTP info and bank details, you can stop your work till the payment page. If you really want to
# explore more then you can explore how you can automate the payment procedure too.
# Also please try to do this usecase for the automation --
# 1) log in to Flipkart and search for dell laptop in Search.
# 2) On the left side, choose the processor as Core i5.
# 3) Fetch the laptop details and print the output like Name, model, price, RAM, etc.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path="D:\\Downloads\\chromedriver_win32\\chromedriver.exe")

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service_obj, options=options)

driver.implicitly_wait(15)

driver.get("https://www.amazon.in/")

driver.maximize_window()


driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']").click()

driver.find_element(By.CSS_SELECTOR, "input[id='ap_email']").send_keys("jc.cgs.999@gmail.com")

driver.find_element(By.CSS_SELECTOR, "input[id='continue']").click()

driver.find_element(By.CSS_SELECTOR, "input[id='ap_password']").send_keys("SjcAmazonCgs@999")

driver.find_element(By.CSS_SELECTOR, "input[id='signInSubmit']").click()

driver.find_element(By.CSS_SELECTOR, "input[id='twotabsearchtextbox']").send_keys("Dell i5")
time.sleep(3)

dynamic_list = driver.find_elements(By.CSS_SELECTOR, "div[class='s-suggestion-container']")

dynamic_list[0].click()

list_of_dell_laptop = driver.find_elements(By.XPATH, "//div/div/h2/a")

list_of_dell_laptop[0].click()

windows_opened = driver.window_handles

driver.switch_to.window(windows_opened[1])

features = driver.find_elements(By.XPATH, "//div[@id='feature-bullets']/ul/li/span")

print("LAPTOP DESCRIPTION : ")

for bullet in features:
    print(bullet.text)

driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']").click()

driver.find_element(By.XPATH, "//span[@id='attach-sidesheet-checkout-button']").click()

