#### fixed deposit calculator.py  ####
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from day_14 import xlutils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file = "C:\\Users\\gobul\\OneDrive\\Desktop\\Python workspace\\Book1.xlsx"
rows=xlutils.getRowCount(file,"Sheet1")

###   Reading data from excel ####
for r in range(2,rows+1):
    pric=xlutils.readData(file,"Sheet1",r,1)
    rateofinterest=xlutils.readData(file,"Sheet1",r,2)
    per1=xlutils.readData(file,"Sheet1",r,3)
    per2=xlutils.readData(file,"Sheet1",r,4)
    fre=xlutils.readData(file,"Sheet1",r,5)
    exp_mvalue=xlutils.readData(file,"Sheet1",r,6)

    ### Passing data to the Application ###
    driver.find_element(By.XPATH,"//*[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"//*[@id='interest']").send_keys(rateofinterest)
    driver.find_element(By.XPATH,"//*[@id='tenure']").send_keys(per1)

    perioddrp=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per2)

    frequencydrp=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    frequencydrp.select_by_visible_text(fre)
    time.sleep(5)
    # from selenium.webdriver.support.ui import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC

    # Optional wait for pop-up to appear
    # try:
    #     # Adjust selector based on actual pop-up structure
    #     WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'popup') or contains(@id,'popup')]")))
    #     # Try closing via button
    #     close_btn = driver.find_element(By.XPATH, "//button[text()='Close' or contains(@class,'close')]")
    #     close_btn.click()
    #     print("Pop-up closed successfully.")
    # except:
    #     print("No pop-up detected or already dismissed.")

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()

    act_mvalue=driver.find_element(By.XPATH,"//*[@id='resp_matval']/strong").text   # Customized Path

### Validation ###
    if float(exp_mvalue)==float(act_mvalue):
        print("test passed")
        xlutils.writeData(file,"Sheet1",r,8,"Passed")
        xlutils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        xlutils.writeData(file, "Sheet1", r, 8, "Failed")
        xlutils.fillRedColor(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]").click() #//*[@id="fdMatVal"]/div[2]/a[2]
    time.sleep(5)
driver.close()
driver.quit()
