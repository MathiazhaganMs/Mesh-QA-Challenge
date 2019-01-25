from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color


class ChallangeOne():
    

    def test(self):
        driverLocation = "C:\\Users\\Mathi\\Documents\\chromedriver_win32\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        # Open the provided URL
        driver.get("https://www.amazon.in/")
        # Searching for keyword books
        SearchBook=driver.find_element(By.ID, "twotabsearchtextbox")
        SearchBook.send_keys("Books")
        SearchBook.send_keys(Keys.ENTER)
        time.sleep(2)
        # Selecting First Book
        FirstBook=driver.find_element(By.XPATH,"//li[@id='result_2']//a[@class='a-link-normal a-text-normal']/img")
        FirstBook.click()
        time.sleep(5)
        # Handling Windows
        handles = driver.window_handles
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)
        for handle in handles:
            """
            This function will handle windows/tab
            Switch to new tab which is opened 
            """
            if handle not in parentHandle:
                driver.switch_to.window(handle)
        
        time.sleep(1)
        # Adding to Cart
        AddToCart=driver.find_element(By.ID, "add-to-cart-button")
        AddToCart.click()
        time.sleep(2)
        # Proceed to checkout
        ProceedToCheckout=driver.find_element(By.XPATH, "//a[@id='hlb-ptc-btn-native']")
        ProceedToCheckout.click()
        time.sleep(2)
        # Continuing without Login
        Contin=driver.find_element(By.ID, "continue")
        Contin.click()
        time.sleep(2)
        AlertMessage=driver.find_element(By.XPATH, "//div[contains(text(),'Enter')]")
        if AlertMessage is not None:
            print("Error Message'Enter your email or mobile phone number' is displayed")
        else:
            print("Error Message is not displayed")
        time.sleep(2)
        Location=AlertMessage.location
        print("Location of error message is " + str(Location))
        rgb=AlertMessage.value_of_css_property('background-color')
        hex1 = Color.from_string(rgb).hex
        print("Color of error Message is " + str(hex1))
        time.sleep(2)
        EmailField=driver.find_element(By.NAME, "email")
        # Sending input email
        EmailField.send_keys("hiring@meshedu.org")
        Contin.click()
        time.sleep(2)
        ErrorProblem=driver.find_element(By.XPATH, "//h4[contains(text(),'There ')]")
        if ErrorProblem is not None:
            print("Error Message 'We cannot find an account with that email address' is displayed")
        else:
            print("Error Message is not displayed")
        time.sleep(2)
        LocationError=ErrorProblem.location
        print("Location of error text " + str(LocationError))
        rgb2=ErrorProblem.value_of_css_property('background-color')
        hex2 = Color.from_string(rgb2).hex
        print("Color of text message is " + str(hex2))
        time.sleep(2)
        ErrorBox=driver.find_element(By.XPATH, "//div[@class='a-box-inner a-alert-container']")
        BoxLocation=ErrorBox.location
        print("Location of Box is " + str(BoxLocation))
        time.sleep(2)
        HazardIcon=driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-alert']")
        if HazardIcon is not None:
            print("Hazard Icon is visible")
        else:
            print("Icon is not visible")
        HazardLocation=HazardIcon.location
        print(HazardLocation)
             
#         
ff=ChallangeOne()
ff.test()       
        
        
        
        
        
        
        