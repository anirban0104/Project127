import pandas as pd 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

START_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_url)
time.sleep(10)
stars_data = []

def scrape():
    for i in range(0, 10):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for table_tag in soup.find_all('table', class_='wikitable'):
            tbody_tag = table_tag.find('tbody')
            for tr_tag in tbody_tag.find_all('tr')[1:]: # Skip the first row (header row)
                temp_list = []
                for td_tag in tr_tag.find_all('td'):
                    temp_list.append(td_tag.get_text().strip())
                stars_data.append(temp_list)
        browser.find_element(by=By.XPATH, value='//*[@id="mw-content-text"]/div[1]/table/tbody/tr/td[3]/span/a').click() # Clicking on the next page link

scrape()

headers = ['Star Name', 'Distance', 'Mass', 'Radius', 'Luminosity']
star_df = pd.DataFrame(stars_data, columns=headers)
star_df.to_csv('stars_data.csv', index=False)

