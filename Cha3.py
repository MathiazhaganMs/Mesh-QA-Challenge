from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.common.keys import Keys


class ChallangeThree():
    

    def test(self):
        driverLocation = "C:\\Users\\Mathi\\Documents\\chromedriver_win32\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        # Open the provided URL
        driver.get("https://student.meshedu.com/")
        SignUpButton=driver.find_element(By.XPATH,"//a[text()='Signup']")
        SignUpButton.click()
        time.sleep(2)
        FirstName=driver.find_element(By.ID,"signup-first-name")
        ActiveElement=driver.switch_to_active_element()
        if FirstName==ActiveElement:
            print("First Name is field is focusing")
        else:
            print("First Name field is not focused")
        FirstName.send_keys("M")
        time.sleep(2)
        continueText=driver.find_element(By.XPATH,"//p[@id='tick']/span")
        textState=continueText.is_displayed()
        print("Press Enter to continue is displayed ? " + str(textState))
        FirstName.clear()
        FirstName.send_keys("Mesh")
        time.sleep(2)
        continueText=driver.find_element(By.XPATH,"//p[@id='tick']/span")
        textState=continueText.is_displayed()
        print("Press Enter to continue is displayed ? " + str(textState))
        time.sleep(2)
        FirstName.clear()
        continueText=driver.find_element(By.XPATH,"//p[@id='tick']/span")
        textState=continueText.is_displayed()
        print("Press Enter to continue is displayed ? " + str(textState))
        time.sleep(2)
        FirstName.send_keys(Keys.ENTER)
        activeEle=driver.switch_to_active_element()
        LastName=driver.find_element(By.ID, "signup-last-name")
        if activeEle==LastName:
            print("It is switched to next tab when clicking on enter tab")
            
        else:
            print("It is not navigating to next tab")
        time.sleep(2)
        LastName.send_keys("Education")
        time.sleep(2)
        EmailField=driver.find_element(By.ID, "signup-email")
        EmailField.send_keys("hiring@meshedorg")
        time.sleep(2)
        EmailField.clear()
        EmailField.send_keys("msmathi")
        EmailField.send_keys(Keys.ENTER)
        toastMsg=driver.find_element(By.XPATH, "//div[contains(text(),'Please enter a valid email.')]")
        if toastMsg is not None:
            print("Error message 'Please enter a valid email' is displayed")
        else:
            print("Error message is not displayed")
        
        
    
ff=ChallangeThree()
ff.test()
