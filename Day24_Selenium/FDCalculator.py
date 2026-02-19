import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager

from Python2.Day24_Selenium import XLUtils

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.nism.ac.in/NISM%20Financial%20Calculators/FD%20Calc/index.html")

file=r"E:\Pavan_Trainings\test_data.xlsx"

rows = XLUtils.getRowCount(file,"FDC")

for current_row in range(2,rows+1):
    amount=XLUtils.readData(file,"FDC",current_row,1)
    interestrate=XLUtils.readData(file,"FDC",current_row,2)
    year=XLUtils.readData(file,"FDC",current_row,3)
    return_expected=XLUtils.readData(file,"FDC",current_row,4)

    loan_amount_txt=driver.find_element(By.XPATH,"//div[@class='group']//child::input[@class='loan-amount']")
    loan_amount_txt.clear()
    loan_amount_txt.send_keys(amount)

    interst_rate_txt=driver.find_element(By.XPATH,"//div[@class='group']//child::input[@class='interest-rate']")
    interst_rate_txt.clear()
    interst_rate_txt.send_keys(interestrate)

    year_txt=driver.find_element(By.XPATH,"//div[@class='group']//following::input[@type='number'][3]")
    year_txt.clear()
    year_txt.send_keys(year)

    calulate_btn=driver.find_element(By.XPATH,"//div[@style='padding-left:25px;']//child::button[@class='calculate-btn']")
    calulate_btn.click()



    actual_amount_value=driver.find_element(By.XPATH,"//div[@class='result']//descendant-or-self::div/div[@id='TI']").text
    actual_amount_value = actual_amount_value.replace(",", "")
    XLUtils.writeData(file, "FDC", current_row, 5,float(actual_amount_value))

    if float(return_expected)==float(actual_amount_value):
        print("Test Passed")
        XLUtils.writeData(file,"FDC",current_row,6,"Passed")

    else:
        print("Test Failed")
        XLUtils.writeData(file,"FDC",current_row,6,"Failed")

    loan_amount_txt.clear()
    interst_rate_txt.clear()
    year_txt.clear()

    time.sleep(2)
