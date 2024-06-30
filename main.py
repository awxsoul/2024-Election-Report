# The libraries used here are requests, beautifulsoup4 and pandas
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

#main base page
url='https://results.eci.gov.in'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#soup of Parliamentary Constituencies Page
pc_url=soup.find_all('a')[1].get('href') #the second link is to Parliamentary Constituencies
pc_response = requests.get(pc_url)
pc_soup = BeautifulSoup(pc_response.text, 'html.parser')

#use of selenium driver to navigate and find info
driver = webdriver.Chrome('./chromedriver.exe')

#dataframe
df = pd.DataFrame(columns=["State","Constituency","Candidate","Party","EVM_votes","Postal_votes","total_votes","percentage_of_votes"])
print(df)
#get all the state lists from dropdown menu
pc_links=[]
for state in (pc_soup.find_all('option')):
    pc_links.append([state.text,])
pc_links.pop(0)

#to navigate driver to state pages
for state_index in range(0,len(pc_links)):
    driver.get(pc_url)
    select= Select(driver.find_element('name','state')) #locate the dropdown menu
    select.select_by_visible_text(pc_links[state_index][0]) #selecting options
    pc_links[state_index].append(driver.current_url)#get url after navigating to the page

    #PARSE for Constituency
    #soup of state pages
    st_url=driver.current_url
    st_response = requests.get(st_url)
    st_soup = BeautifulSoup(st_response.text, 'html.parser')

    #get all the constituency lists from dropdown menu
    pc_links[state_index].append([])
    for constituency in (st_soup.find_all('option')):
         c_name=' '.join(map(str,constituency.text.split()))
         # this is to ensure that all the text labels have equal spacing
         pc_links[state_index][2].append(c_name)
    pc_links[state_index][2].pop(0)
    
    #to navigate driver to constituency pages
    for constituency_index in range(0,len(pc_links[state_index][2])):
        driver.get(st_url)
        select= Select(driver.find_element('name','state')) #locate the dropdown menu
        select.select_by_visible_text(pc_links[state_index][2][constituency_index]) #selecting options

        #open table format page
        driver.find_element(By.XPATH,'(//div[@class="switch-list"]//a)[2]').click()

        #soup of state table info pages
        ta_url=driver.current_url
        ta_response = requests.get(ta_url)
        ta_soup = BeautifulSoup(ta_response.text, 'html.parser')

        #table found
        table=ta_soup.find('table')
        
        #parse through table
        for row in table.tbody.find_all('tr'):
            row_data=row.find_all('td')
            
            sta=pc_links[state_index][0]
            con=pc_links[state_index][2][constituency_index]
            can=row_data[1].text.strip()
            par=row_data[2].text.strip()
            ev=row_data[3].text.strip()
            po=row_data[4].text.strip()
            to=row_data[5].text.strip()
            pe=row_data[6].text.strip()
            df_add = pd.DataFrame({
                "State":[sta],
                "Constituency":[con],
                "Candidate":[can],
                "Party":[par],
                "EVM_votes":[ev],
                "Postal_votes":[po],
                "total_votes":[to],
                "percentage_of_votes":[pe]
                })
            df = pd.concat([df, df_add], ignore_index=False)    

print(pc_links)

driver.close()