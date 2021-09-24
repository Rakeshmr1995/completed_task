import requests
from bs4 import BeautifulSoup
import lxml
from xlwt import *
workbook = Workbook(encoding='utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'Holiday Name')
table.write(0, 1, 'Holiday Date')
table.write(0, 2, 'Holiday Type')
table.write(0, 3, 'Holiday Comments')
line = 1
url ='https://www.officeholidays.com/countries/india/2021'
f = requests.get(url)
headers = {
    'User-Agent': 'Chrome/92.0.4515.159'
}
f = requests.get(url, headers=headers)
soup = BeautifulSoup(f.content, 'lxml')
holidays = soup.find('table', class_='country-table')
holidayName = holidays.find_all('a', class_='country-listing')
for hname in holidayName:
    print(hname.text)
    table.write(line, 0, hname.text)
    line += 1
line = 1
holidayDate = soup.find_all('time')
for hdate in holidayDate:
    print(hdate.text)
    table.write(line, 1, hdate.text)
    line += 1
line = 1
holidayType = soup.find_all('td', class_='comments')
for htype in holidayType:
    print(htype.text)
    table.write(line, 2, htype.text)
    line += 1
line = 1
holidayComments = soup.find_all('td', class_='hide-ipadmobile')
for hcmt in holidayComments:
    print(hcmt.text)
    table.write(line, 3, hcmt.text)
    line += 1

line += 1
workbook.save('HolidayLists.csv')