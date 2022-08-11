from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
import time


try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.NAME, "first_name")
    for element in elements:
        element.send_keys("Alexey")
        
    elements = browser.find_elements(By.NAME, "last_name")
    for element in elements:
        element.send_keys("Navalniy")
        
    elements = browser.find_elements(By.CLASS_NAME, "form-control.city")
    for element in elements:
        element.send_keys("free@navalnii.ru")
        
    elements = browser.find_elements(By.ID, "country")
    for element in elements:
        element.send_keys("хуй") 
        

    button = browser.find_element(By.XPATH, '//div[@class="container"]//div[6]/button[3]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла