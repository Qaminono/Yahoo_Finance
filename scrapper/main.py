import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


companies = ['PD', 'ZUO', 'PINS', 'ZM', 'PVTL', 'DOCU', 'CLDR', 'RUN']

driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get("https://finance.yahoo.com")
assert "Yahoo" in driver.title

for company in companies:
    wait = WebDriverWait(driver, 3)
    elem = driver.find_element_by_name("yfin-usr-qry")
    elem.send_keys(company)
    headers = list()
    try:
        headers = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'modules_quoteSymbol__3Vtbg'))
        )
        is_find = True
    except TimeoutException:
        is_find = False
    if is_find and headers[0].text == company:
        elem.send_keys(Keys.RETURN)
    else:
        print(f'No matches for "{company}" were found.')
        elem.clear()
        continue
    #  elem = driver.find_element_by_partial_link_text('Historical Data')
    elem = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-test='HISTORICAL_DATA']"))
    )
    try:
        elem.click()
    except ElementClickInterceptedException:
        time.sleep(1)
        elem = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-test='HISTORICAL_DATA']"))
        )
        elem.click()
    # elem = driver.find_element_by_class_name('dateRangeBtn')
    elem = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'dateRangeBtn'))
    )
    elem.click()
    # elem = driver.find_element_by_css_selector("button[data-value='MAX']")
    elem = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-value='MAX']"))
    )
    elem.click()
    # elem = driver.find_element_by_css_selector("a[download]")
    elem = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[download]"))
    )

    if not os.path.exists('data'):
        os.mkdir('data')
    with open(f'data/{elem.get_attribute("download")}', 'wb') as file:
        file.write(requests.get(elem.get_attribute('href')).content)

    with open(f'data/{elem.get_attribute("download")}') as file:
        for line in file.readlines()[1:]:
            date, open_, high, low, close, adj_close, volume = line.split(',')
            payload = {
                "company": company,
                "date": date,
                "open": open_,
                "high": high,
                "low": low,
                "close": close,
                "adj_close": adj_close,
                "volume": int(volume)
            }
            requests.post('http://localhost:8000', data=payload)
        print(f'All the data related to {company} was posted on service.')


driver.close()
