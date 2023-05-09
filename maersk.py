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
# From city and To city options : merchant_haulage or carrier_haulge

def maersk(from_city, to_city, option_from_city, option_to_city, commodity, container_type, container_quantity, weight, month, day):
    
    username = "javed1"
    password = "Chennai08"

    from_city_option =  {"merchant_haulage":"/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[1]/div[2]/div/div[1]/div[2]/label",
                    "carrier_haulage":"/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[1]/div[2]/div/div[1]/div[3]/label"}
    
    to_city_option = {"merchant_haulage": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[1]/div[2]/div/div[2]/div[2]/label",
                  "carrier_haulage": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[1]/div[2]/div/div[2]/div[3]/label"}
    
    container_types = {
        "20 DRY STANDARD": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/ul/li[1]/div/div",
        "40 DRY STANDARD": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/ul/li[2]/div/div",
        "40 DRY HIGH": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/ul/li[3]/div/div",
        "45 DRY HIGH": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/ul/li[4]/div/div",
        "20 REEFER STANDARD": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[2]/ul/li[1]/div/div",
        "40 REEFER HIGH": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[2]/ul/li[2]/div/div",
        "20 OPEN TOP": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[3]/ul/li[1]/div/div",
        "40 OPEN TOP": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[3]/ul/li[2]/div/div",
        "40 OPEN TOP HIGH": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[3]/ul/li[3]/div/div",
        "40 FLAT STANDARD": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[3]/ul/li[4]/div/div",
        "40 FLAT HIGH": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[3]/ul/li[5]/div/div",
        "20 TANK": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[4]/ul/li[1]/div/div",
        "40 TANK": "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div[2]/div/div/div[4]/ul/li[3]/div/div"
    }

    
    try:
        subprocess.call("TASKKILL /F /IM chrome.exe", shell=True)
    except: 
        print("No apps closed")
    
    driver = uc.Chrome()
    driver.get("https://www.maersk.com/instantPrice")
        
    while True:

        try:
            driver.maximize_window() # For maximizing window
            sleep(1)
            driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[1]/div[2]/div/div[1]/div[1]/div/div/div/div/div/input").send_keys(from_city) # Entering details to from city
            elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "typeahead__suggestions__line--1")))
            elements_from_city = driver.find_elements(By.CLASS_NAME, "typeahead__suggestions__line--1") # SELECTING FIRST OPTION FROM "FROM CITY"
            elements_from_city[0].click() # First element under search result of From city
            toc = driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[1]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/input") # Entering detail into To city
            toc.click()
            toc.send_keys(to_city)
            elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "typeahead__suggestions__line--1")))
            try:
                elements_to_city = driver.find_elements(By.CLASS_NAME, "typeahead__suggestions__line--1") # SELECTING FIRST OPTION FROM "TO CITY"
                elements_to_city[0].click() # First element under search result of To city
            except:
                print("Not found")

            driver.find_element("xpath", from_city_option[option_from_city]).click() # Merchant Haulage - From city
            driver.find_element("xpath", to_city_option[option_to_city]).click() # Merchant Haulage - To City
            
            driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[2]/div[2]/div/div/div/div[1]/div/div/input").send_keys(commodity) # Commodity 
            elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "typeahead__suggestions__line--1")))
            elements_commodity = driver.find_elements(By.CLASS_NAME, "typeahead__suggestions__line--1") # SELECTING FIRST OPTION FROM "FROM COMMODITY"
            elements_commodity[0].click() # First element under search result of From city            
            try:
                elem = WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, "/fieldset/div[3]/div[1]/div/div/div/div/div/input")))
                driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div/div/div/input").click()
                driver.find_element("xpath", str(container_types[container_type])).click()
            except:
                print("Unable to fetch container detais try again later")
                break
            
            container_quantity_element = driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[2]/div[1]/div/div/div/div/input")
            driver.execute_script("arguments[0].value = ''", container_quantity_element) # Container Quantity
            container_quantity_element.send_keys(container_quantity)
            container_quantity_element.send_keys(Keys.RETURN)

            container_weight_element = driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[2]/div[2]/div/div/div/div/input") # Weight of each container
            driver.execute_script("arguments[0].value = ''", container_weight_element) # weight Quantity
            container_weight_element.send_keys(weight)
            container_weight_element.send_keys(Keys.RETURN)

            element = driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[4]/div[2]/div/div/div[1]/input")
            driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
            months_button = driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[4]/div[2]/div/div/div[2]/div/div[1]/a[5]").click()
            months = driver.find_elements(By.CLASS_NAME, "cell")
            for i in months:
                if i.text == month:
                    i.click()
                    break
            dates = driver.find_elements(By.CLASS_NAME, "cell.cur-month")

            for i in dates:
                if (i.text == day):
                    try:
                        i.click()
                        break
                    except:
                        print("Date not available")
            #driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[4]/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[7]").click() # DATE 
            print("selected succesffully")

            sleep(0.5)

            driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/div[2]/div/div/button").click()
            print("Process Completed Succesfully -- Result Image Saved")
            
            driver.execute_script("window.open('40 feet');")
            allTabs = driver.window_handles
            driver.switch_to.window(allTabs[-1])
            driver.get('https://www.maersk.com/instantPrice/quotes')
            elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#webapp > div > article > section > div > div > p")))
            driver.find_element(By.CSS_SELECTOR, "#webapp > div > article > section > section.request-summary.action-card > div.docs__row.request-summary__info.flex--row.top > div.request-summary__info--edit").click() # Clicking on edit request
            elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div/div/div/a")))
            sleep(1)
            driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div/div/div/a").click() # Clearing container detail
            try:
                driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[3]/div[3]/div[1]/div/div/div/div/div/input").click()
                elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, str(container_types["40 DRY STANDARD"]))))
                driver.find_element("xpath", str(container_types["40 DRY STANDARD"])).click()
            except:
                print("Unable to fetch container detais try again later")
                break

            driver.find_element("xpath", "/html/body/div[2]/main/div/article/section/section/section/div/form/div[2]/div/div/button").click()


            break
        except:
            try:
                driver.find_element("xpath", "/html/body/div[1]/div/div/div[1]/div[2]/button[2]").click()
                sleep(0.5)
                driver.find_element("name", "usernameInput").send_keys(username)
                driver.find_element("name", "passwordInput").send_keys(password)
                driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div/form/button").click()

                print("logged in successfully")
                #/html/body/div[2]/div/div/div/div/div/div[1]/h1
                #/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[1]/div[2]/div/div[1]/div[1]/div/div/div/div/div/input
                elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[1]/div[2]/div/div[1]/div[1]/div/div/div/div/div/input")))
                
                continue
            except:
            
                driver.find_element("name", "usernameInput").send_keys(username)
                driver.find_element("name", "passwordInput").send_keys(password)
                driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div/form/button").click()

                print("logged in successfully")
                #/html/body/div[2]/div/div/div/div/div/div[1]/h1
                #/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[1]/div[2]/div/div[1]/div[1]/div/div/div/div/div/input
                elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/article/section/section/section/div/form/fieldset[1]/div[2]/div/div[1]/div[1]/div/div/div/div/div/input")))
                continue

todays_date = date.today()
two_weeks = todays_date + timedelta(weeks = 2)  
day = two_weeks.day
month = calendar.month_abbr[two_weeks.month]

maersk(sys.argv[1], sys.argv[2], "merchant_haulage", "merchant_haulage", "machinery", "20 DRY STANDARD", "1", "22000", str(month), str(day))

#maersk("chennai", "hamburg", "merchant_haulage", "merchant_haulage", "machinery", "20 DRY STANDARD", "3", "23000", "May", "14")
