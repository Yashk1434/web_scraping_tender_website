from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

#changing name according to given in assignment text message
csv_cols = {
    "NIT/RFP NO": "ref_no",
    "Name of Work / Subwork / Packages": "title",
    "Estimated Cost": "tender_value",
    "Bid Submission Closing Date & Time": "bid_submission_end_date",
    "EMD Amount": "emd",
    "Bid Opening Date & Time": "bid_open_date"
}

#chrome driver
driver = webdriver.Chrome()
driver.get("https://etender.cpwd.gov.in/")
time.sleep(5)

#a pop arises on the website to tackle it
try:
    alert = driver.switch_to.alert
    alert.accept()
    print("Alert accepted.")
except:
    print("No alert found.")
time.sleep(3)

#clicking on new tenders
driver.find_element(By.LINK_TEXT, "New Tenders").click()
time.sleep(3)

#clicking on all subtab
driver.find_element(By.LINK_TEXT, "All").click()
time.sleep(3)

#set dropdown menu to show 20 rows
select_element = Select(driver.find_element(By.NAME, "awardedDataTable_length"))
select_element.select_by_visible_text("20")
time.sleep(3)

#waiting until rows are loading
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//table[@id="awardedDataTable"]/tbody/tr'))
)

#getting rows
rows = driver.find_elements(By.XPATH, '//table[@id="awardedDataTable"]/tbody/tr')
print(f"Total rows found: {len(rows)}")

data = []

#extracting details from first 20 rows
for row in rows[:20]:
    cols = row.find_elements(By.TAG_NAME, 'td')
    if len(cols) >= 8:
        data.append({
            csv_cols["NIT/RFP NO"]: cols[1].text.strip(),
            csv_cols["Name of Work / Subwork / Packages"]: cols[2].text.strip(),
            csv_cols["Estimated Cost"]: cols[4].text.strip(),
            csv_cols["Bid Submission Closing Date & Time"]: cols[6].text.strip(),
            csv_cols["EMD Amount"]: cols[5].text.strip(),
            csv_cols["Bid Opening Date & Time"]: cols[7].text.strip(),
        })

driver.quit()

#creating Pandas Dataframe and saving csv file
df = pd.DataFrame(data)
print(df.head())

df.to_csv("tender_data.csv", index=False)
print("CSV generated successfully.")
