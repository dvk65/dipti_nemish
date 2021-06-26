import os, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import matplotlib.pyplot as plt

chrome_options=Options()
chrome_options.binary_location = "C:\\Program Files\Google\Chrome\Application\chrome.exe"
driver=webdriver.Chrome(options=chrome_options,executable_path="C:\\Users\kulka\chromedriver.exe")

url="https://in.finance.yahoo.com/quote/AAPL?ltr=1"
driver.get(url)
time.sleep(5)

driver.find_element_by_xpath("//li[@data-test='HISTORICAL_DATA']").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@download='AAPL.csv']").click()
time.sleep(10)
print("downloaded")
driver.close()

os.chdir('C:\\Users\kulka\Downloads')
rcsv=pd.read_csv("AAPL.csv")
print("read csv")
pc=rcsv['Adj Close'].pct_change()[1:]
wr=(1+pc).cumprod()-1
print(wr)

f=plt.figure()
ax1=f.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(wr)
ax1.set_xlabel("Date")
ax1.set_ylabel("Cumulative Returns")
ax1.set_title("Cumulative Returns")
plt.show()