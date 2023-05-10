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


def happag(from_city, to_city, date, timesmall=1, timemed=3, timelarge=5):
    try:
        subprocess.call("TASKKILL /F /IM chrome.exe", shell=True)
    except:
        print("No apps closed")
        
    driver = uc.Chrome()

# /html/body/div[4]
# body > div.q-loading-bar.q-loading-bar--top
    while True:
        try:
            # #azureFormSpinner > svg
            
            driver.get("https://solutions.hapag-lloyd.com/quick-quotes")
            elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "desktop.no-touch.body--light")))
            sleep(4)
            start_loc = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/label/div/div[1]/div[2]/div[1]/input")
            start_loc.click()
            start_loc.send_keys(from_city)
            elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "q-item__section.column.q-item__section--main.justify-center")))
            sleep(0.3)
            option = driver.find_elements(By.CLASS_NAME, "q-item__section.column.q-item__section--main.justify-center")
            option[0].click()

            sleep(0.5)
            end_loc = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/label/div/div/div[2]/div[1]/input")
            end_loc.click()
            end_loc.click()
            end_loc.send_keys(to_city)
            elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "q-item__section.column.q-item__section--main.justify-center")))
            sleep(0.3)
            option = driver.find_elements(By.CLASS_NAME, "q-item__section.column.q-item__section--main.justify-center")
            option[0].click()


            #q-item__label
            driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[2]/div[2]/div[2]/div[1]/div/div/label/div/div/div[1]/input").click()
            date_element = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[2]/div[2]/div[2]/div[1]/div/div/label/div/div/div[1]/input")
            date_element.send_keys(Keys.CONTROL, 'a')
            date_element.send_keys(Keys.BACKSPACE)
            driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[2]/div[2]/div[2]/div[1]/div/div/label/div/div/div[1]/input").send_keys(date)
            # q-item__section column q-item__section--main justify-center

            driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/label/div/div/div[1]/div[1]").click()
            elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "q-item__section.column.q-item__section--main.justify-center")))
            sleep(0.3)
            container_types = driver.find_elements(By.CLASS_NAME, "q-item__section.column.q-item__section--main.justify-center")
            container_types[1].click() # 0 CHOOSES 20' GENERAL PURPOSE, 1 CHOOSES 40' GENERAL PURPOSE

            commodity = driver.find_element(By.CSS_SELECTOR, "div[placeholder='Select commodity']")
            commodity.click()
            # /html/body/div[8]/div/div[2]
            elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div[2]")))

            checkbox = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[3]/div[2]/div[2]/div/div[1]/label/div/div/div/div/div[1]")
            checkbox.click()

            sleep(0.1)

            driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/form/div/div[3]/div[2]/div[2]/div/div[2]/button").click()
           
            break


        except:
     
            try:
                try:
                    driver.find_element(By.CSS_SELECTOR, "#onetrust-pc-sdk > div.ot-button-group-parent > div.ot-button-group > button.save-preference-btn-handler.onetrust-close-btn-handler").click()
                    
                    wait = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/iframe")))
                    iframe = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/iframe")

                    driver.switch_to.frame(iframe)
                    wait = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div")))
                    driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[1]/input').click()
                    driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[1]/input').click()
                    driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[1]/input').send_keys("timescantaufeek")

                    #/html/body/div[2]/div/div/form/div[3]/div[2]/input

                    driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[2]/input').click()
                    driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[2]/input').click()
                    driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[2]/input').send_keys("TIMESCAN")

                    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/div[3]/div[4]/button").click()
                    driver.switch_to.default_content()
                    wait = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/label/div/div[1]/div[2]/div[1]/input")))
                    continue
                
                except:
                    
                    #wait = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/iframe")))
                    try:
                        iframe = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/iframe")
                    except:
                        wait = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/iframe")))
                        iframe = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/iframe")


                    driver.switch_to.frame(iframe)
                    wait = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div")))
                    driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[1]/input').click()
                    driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[1]/input').click()
                    driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[1]/input').send_keys("timescantaufeek")

                    #/html/body/div[2]/div/div/form/div[3]/div[2]/input

                    driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[2]/input').click()
                    driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[2]/input').click()
                    driver.find_element("xpath", '/html/body/div[2]/div/div/form/div[3]/div[2]/input').send_keys("TIMESCAN")

                    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/div[3]/div[4]/button").click()
                    driver.switch_to.default_content()
                    wait = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/label/div/div[1]/div[2]/div[1]/input")))
                    continue

            except:
                print("solve captcha and rerun")
                quit()

todays_date = date.today()
two_weeks = todays_date + timedelta(weeks = 2)  
two_weeks_list = str(two_weeks).split("-")
date_input = two_weeks_list[2] + "." + two_weeks_list[1] + "." + two_weeks_list[0]


#happag(sys.argv[1], sys.argv[2], date_input)
happag("chennai", "norfolk", date_input)