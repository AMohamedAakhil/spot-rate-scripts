import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
import subprocess
import sys
from datetime import date, timedelta
import calendar
import random

def cma(from_city, to_city, day, month, container, weight, number_containers, commodity, soc=False, time_small=1, time_med=2, time_large=3):
    
    try:
        subprocess.call("TASKKILL /F /IM chrome.exe", shell=True)
    except:
        print("No apps closed")

    driver = uc.Chrome()
    driver.get("https://www.cma-cgm.com/ebusiness/pricing/instant-Quoting")

    while True:
        try:
            driver.find_element("xpath", "/html/body/div[2]/div/main/div/section/form/fieldset[1]/div/div[1]/div[2]/div/div/div[1]/input").send_keys(from_city)  # From city
            wait = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "el-scrollbar__view.el-autocomplete-suggestion__list")))
            sleep(0.5)
            li_elements = driver.find_elements(By.TAG_NAME, "li")
            li_elements[-1].click()
            sleep(random.uniform(0, 0.4))
            
            driver.find_element("xpath", "/html/body/div[2]/div/main/div/section/form/fieldset[1]/div/div[1]/div[3]/div/div/div[1]/input").send_keys(to_city)  # To city
            wait = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "el-scrollbar__view.el-autocomplete-suggestion__list")))
            sleep(0.5)
            li_elements = driver.find_elements(By.TAG_NAME, "li")
            li_elements[-1].click()
            sleep(random.uniform(0, 0.4))
            # Clicking on date picker
            driver.find_element("xpath", "/html/body/div[2]/div/main/div/section/form/fieldset[1]/div/div[2]/div/div/div/input").click()
            sleep(random.uniform(0, 0.4))
            current_month = driver.find_element(By.CSS_SELECTOR, "#body > div.el-picker-panel.el-date-picker.el-popper.has-sidebar > div.el-picker-panel__body-wrapper > div.el-picker-panel__body > div.el-date-picker__header > span:nth-child(4)").text
            sleep(random.uniform(0, 1))
            if current_month == month:
                # retrieving all available dates
                dates = driver.find_elements(By.CLASS_NAME, "available")
                for i in dates:
                    if i.text == day:
                        i.click()
                        break
            else:
                driver.find_element(By.CSS_SELECTOR, "#body > div.el-picker-panel.el-date-picker.el-popper.has-sidebar > div.el-picker-panel__body-wrapper > div.el-picker-panel__body > div.el-date-picker__header > button.el-picker-panel__icon-btn.el-date-picker__next-btn.el-icon-arrow-right").click()
                driver.find_element(By.CSS_SELECTOR, "#body > div.el-picker-panel.el-date-picker.el-popper.has-sidebar > div.el-picker-panel__body-wrapper > div.el-picker-panel__body > div.el-date-picker__header > button.el-picker-panel__icon-btn.el-date-picker__next-btn.el-icon-arrow-right").click()
                next_month = driver.find_element(By.CSS_SELECTOR, "#body > div.el-picker-panel.el-date-picker.el-popper.has-sidebar > div.el-picker-panel__body-wrapper > div.el-picker-panel__body > div.el-date-picker__header > span:nth-child(4)").text
                sleep(random.uniform(0, 0.4))
                if next_month == month:
                    new_dates = driver.find_elements(By.CLASS_NAME, "available")
                    for i in new_dates:
                        if i.text == day:
                            i.click()
                            break
                else:
                    print("Date not available")
            sleep(random.uniform(0, 0.2))
            if soc:
                driver.find_element("xpath", "/html/body/div[2]/div/main/div/section/form/fieldset[2]/div[1]/div/div/span[2]").click()  # SOC
            sleep(random.uniform(0, 0.2))
            driver.find_element("xpath", "/html/body/div[2]/div/main/div/section/form/fieldset[2]/div[2]/div[1]/div/div/div/input").click() # Clicking on Equiment Type
            equipment_types = driver.find_elements(By.CLASS_NAME, "el-select-dropdown__item")
            for i in equipment_types:
                print(i.text)
                if i.text == container:
                    i.click()
                    break
            
            weight_box = driver.find_element("xpath", "/html/body/div[2]/div/main/div/section/form/fieldset[2]/div[2]/div[2]/div").click()
            driver.find_element("xpath", "/html/body/div[2]/div/main/div/section/form/fieldset[2]/div[2]/div[2]/div/span/input").send_keys(weight)
            sleep(random.uniform(0, 0.2))

            for i in range(int(number_containers)-1):
                num_containers = driver.find_element("xpath", "/html/body/div[2]/div/main/div/section/form/fieldset[2]/div[2]/div[3]/div/div/button[2]").click()

            wait = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/main/div/section/form/fieldset[2]/div[3]/div/div/div/input")))		
            commodity_box = driver.find_element("xpath", "/html/body/div[2]/div/main/div/section/form/fieldset[2]/div[3]/div/div/div/input").click()
            commodity_elements = driver.find_elements(By.CLASS_NAME, "el-select-dropdown__item")
            for i in commodity_elements:
                print(i.text)
                if i.text == commodity:
                    i.click()
                    break
            sleep(random.uniform(0, 0.2))

            driver.find_element("xpath", "/html/body/div[2]/div/main/div/section/form/div/div/button[1]").click() # Submit Button	

            break
        except:
            try:
                driver.find_element(By.NAME, "pf.username").send_keys("javed@timescan.in")
                driver.find_element(By.NAME, "pf.pass").send_keys("TSLchennai1234")

                driver.find_element("xpath", "/html/body/div/div[2]/div[1]/form/fieldset/div[3]/button").click()
                sleep(time_large)
                continue
            except:
                print("Solve captcha and rerun!")
                break


todays_date = date.today()
two_weeks = todays_date + timedelta(weeks = 2)  
day = two_weeks.day
month = calendar.month_abbr[two_weeks.month]

cma(from_city=sys.argv[1], to_city=sys.argv[2], day = str(day), month = str(month), container = "20' Dry Standard", weight = "22000", number_containers = "1", commodity="Freight All Kinds")
#cma(from_city="chennai", to_city="norfolk", day = str(day), month = str(month), container = "20' Dry Standard", weight = "22000", number_containers = "1", commodity="Freight All Kinds")
