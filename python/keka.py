# 2. Write an automation script which should automate marking the attendence in Keka portal. Try to
# automate the marking for your username. This may require you to do extensive research as Keka
# login is under company. So please do not restrict your exploration.
# alignment missing patterns

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path="D:\\Downloads\\chromedriver_win32\\chromedriver.exe")

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service_obj, options=options)

driver.implicitly_wait(15)

driver.get("https://app.keka.com/Account/Login")

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='email']").send_keys("********")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.find_elements(By.XPATH, "//div/button")[1].click()

driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("******")

driver.find_element(By.XPATH, "//button[text()='Login']").click()

driver.find_element(By.XPATH, "//ul/li/a[@href='/#/me/leave']").click()

driver.find_element(By.XPATH, "//ul/li/a[@routerlink='attendance']").click()

driver.find_element(By.XPATH, "//div/a[text()='Work From Home']").click()

driver.find_elements(By.XPATH, "//div/span[text()='Select Date']")[0].click()

current_date = datetime.now()

day_ = current_date.day

driver.find_element(By.XPATH, f"(//tbody/tr/td/span[text()='{day_}'])[1]").click()
driver.find_element(By.XPATH, f"(//tbody/tr/td/span[text()='{day_}'])[1]").click()


driver.find_element(By.XPATH, "//div/textarea").send_keys("Due to Covid-19 pandemic.")

# driver.find_element(By.XPATH, "//div/button[text()='Request']").click()
# driver.find_element(By.XPATH, "//div/button[text()='Cancel']").click()






