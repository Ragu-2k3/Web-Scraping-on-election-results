# -*- coding: utf-8 -*-
"""Web Scraping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zBX60RFX8VokCdYevYce1xPHU7hmG1b5

IMPORTING MODULES
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

"""GATHERING THE CONTENTS FROM THE WEB PAGES"""

url = 'https://results.eci.gov.in/PcResultGenJune2024/index.htm'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html')
print(soup)

"""EXTRACTING THE REQUIRED
DATA
"""

soup.find_all('table')

soup.find('table', class_ = 'table')

table = soup.find_all('table')
print(table)

"""PRINTING THE HEADINGS"""

for t in table:
    titles = t.find_all('th')
titles

titles_tab = [title.text for title in titles[0:4]]
print(titles_tab)

df = pd.DataFrame(columns = titles_tab)
df

"""CONNECTING TO THE DRIVE"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd drive/MyDrive/WEB

"""FINAL CODE FOR THE PARTY WISE RESULTS STATUS

"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
results = []
table = soup.find('table', {'class': 'table'})
if not table:
    print("Table not found")
else:
    headers = [header.text.strip() for header in table.find_all('th')[:4]]
    rows = table.find_all('tr')
    print("Headers:", headers)
    for row in rows[1:-1]:
        cols = row.find_all('td')
        party_data = [col.text.strip() for col in cols]
        results.append(party_data)
    print("Sample data row:", results[0])
    df = pd.DataFrame(results, columns=headers)
    df.to_excel('Results_1.xlsx', index=False)
    print("Data has been exported to Results_1.xlsx")

"""STATE WISE RESULTS"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


excel_writer = pd.ExcelWriter('Results_2.xlsx', engine='openpyxl')
for i in range(1, 30):
    state_code = f"S{i:02}"
    url = f"https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-{state_code}.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    header_tag = soup.find('h2')
    if not header_tag:
        print(f"Header not found for state code: {state_code}")
        continue

    state_name = header_tag.text.strip().split('(')[0].strip()[:31]
    table = soup.find('table', {'class': 'table'})
    if not table:
        print(f"Table not found for state: {state_name}")
        continue

    headers = [header.text.strip() for header in table.find_all('th')[:4]]
    rows = table.find_all('tr')

    results = []
    for row in rows[1:-1]:
        cols = row.find_all('td')
        party_data = [col.text.strip() for col in cols]
        results.append(party_data)


    df = pd.DataFrame(results, columns=headers)
    df.to_excel(excel_writer, sheet_name=state_name, index=False)
    print(f"Data for {state_name} has been exported to Results_2.xlsx")


excel_writer.book.save('Results_2.xlsx')
excel_writer.close()

print("All data has been exported.")

""" UNION TERRITORIES WISE RESULTS"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


excel_writer = pd.ExcelWriter('Results_3.xlsx', engine='openpyxl')
for i in range(1, 10):
    union_code = f"U{i:02}"
    url = f"https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-{union_code}.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    header_tag = soup.find('h2')
    if not header_tag:
        print(f"Header not found for union territory code: {union_code}")
        continue

    ut_name = header_tag.text.strip().split('(')[0].strip()[:31]
    table = soup.find('table', {'class': 'table'})
    if not table:
        print(f"Table not found for union territory: {ut_name}")
        continue

    headers = [header.text.strip() for header in table.find_all('th')[:4]]
    rows = table.find_all('tr')

    results = []
    for row in rows[1:-1]:
        cols = row.find_all('td')
        party_data = [col.text.strip() for col in cols]
        results.append(party_data)


    df = pd.DataFrame(results, columns=headers)
    df.to_excel(excel_writer, sheet_name=ut_name, index=False)
    print(f"Data for {ut_name} has been exported to Results_3.xlsx")

excel_writer.book.save('Results_3.xlsx')
excel_writer.close()

print("All data has been exported.")

"""BOTH STATE AND UNION TERRITORIES WISE RESULTS"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

excel_writer = pd.ExcelWriter('Results_4.xlsx', engine='openpyxl')
workbook = excel_writer.book
for i in range(1, 30):
    state_code = f"S{i:02}"
    url = f"https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-{state_code}.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    header_tag = soup.find('h2')
    if not header_tag:
        print(f"Header not found for state code: {state_code}")
        continue


    state_name = header_tag.text.strip().split('(')[0].strip()[:31]
    table = soup.find('table', {'class': 'table'})
    if not table:
        print(f"Table not found for state: {state_name}")
        continue

    headers = [header.text.strip() for header in table.find_all('th')[:4]]
    rows = table.find_all('tr')

    results = []
    for row in rows[1:-1]:
        cols = row.find_all('td')
        party_data = [col.text.strip() for col in cols]
        results.append(party_data)


    df = pd.DataFrame(results, columns=headers)
    df.to_excel(excel_writer, sheet_name=state_name, index=False)

    print(f"Data for {state_name} has been exported to Results_4.xlsx")

for i in range(1, 10):
    union_code = f"U{i:02}"
    url = f"https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-{union_code}.htm"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    header_tag = soup.find('h2')
    if not header_tag:
        print(f"Header not found for union territory code: {union_code}")
        continue

    ut_name = header_tag.text.strip().split('(')[0].strip()[:31]
    table = soup.find('table', {'class': 'table'})
    if not table:
        print(f"Table not found for union territory: {ut_name}")
        continue

    headers = [header.text.strip() for header in table.find_all('th')[:4]]
    rows = table.find_all('tr')

    results = []
    for row in rows[1:-1]:
        cols = row.find_all('td')
        party_data = [col.text.strip() for col in cols]
        results.append(party_data)

    df = pd.DataFrame(results, columns=headers)
    df.to_excel(excel_writer, sheet_name=ut_name, index=False)
    print(f"Data for {ut_name} has been exported to Results_4.xlsx")


workbook.save('Results_4.xlsx')
excel_writer.close()

print("All data has been exported.")

"""FINAL ALL TOGETHER"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

excel_writer = pd.ExcelWriter('Results_Final.xlsx', engine='openpyxl')
workbook = excel_writer.book

url = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
results = []
table = soup.find('table', {'class': 'table'})
if not table:
    print("Table not found")
else:
    headers = [header.text.strip() for header in table.find_all('th')[:4]]
    rows = table.find_all('tr')
    print("Headers:", headers)
    for row in rows[1:-1]:
        cols = row.find_all('td')
        party_data = [col.text.strip() for col in cols]
        results.append(party_data)
    print("Sample data row:", results[0])
    df = pd.DataFrame(results, columns=headers)
    df.to_excel(excel_writer, sheet_name='Party Wise Result', index=False)
    print("Data has been exported to the 'Party Wise Result' sheet in Results_Final.xlsx")

def fetch_and_process_data(url, name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'table'})
    if not table:
        print(f"Table not found for {name}")
        return

    headers = [header.text.strip() for header in table.find_all('th')[:4]]
    rows = table.find_all('tr')

    results = []
    for row in rows[1:-1]:
        cols = row.find_all('td')
        party_data = [col.text.strip() for col in cols]
        results.append(party_data)

    df = pd.DataFrame(results, columns=headers)
    df.to_excel(excel_writer, sheet_name=name, index=False)

    print(f"Data for {name} has been exported to Results_Final.xlsx")

for i in range(1, 30):
    state_code = f"S{i:02}"
    url = f"https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-{state_code}.htm"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    header_tag = soup.find('h2')
    if not header_tag:
        print(f"Header not found for state code: {state_code}")
        continue

    state_name = header_tag.text.strip().split('(')[0].strip()[:31]

    fetch_and_process_data(url, state_name)

for i in range(1, 10):
    union_code = f"U{i:02}"
    url = f"https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-{union_code}.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    header_tag = soup.find('h2')
    if not header_tag:
        print(f"Header not found for union territory code: {union_code}")
        continue
    ut_name = header_tag.text.strip().split('(')[0].strip()[:31]
    fetch_and_process_data(url, ut_name)

workbook.save('Results_Final.xlsx')
excel_writer.close()

print("All data has been exported.")

