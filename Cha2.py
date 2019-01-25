from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


class ChallangeTwo():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        driverLocation = "C:\\Users\\Mathi\\Documents\\chromedriver_win32\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        # Open the provided URL
        driver.get("https://student.meshedu.com/")
        time.sleep(2)
        SignUpButton=driver.find_element(By.XPATH,"//a[text()='Signup']")
        SignUpButton.click()
        driver.quit()
        
        
        
ff=ChallangeTwo()
ff.test()