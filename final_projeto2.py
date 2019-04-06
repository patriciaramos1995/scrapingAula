import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import datetime


opts = Options()
opts.add_argument("--headless")
driver = webdriver.Firefox(executable_path="/home/patriciadesouzaramos/PycharmProjects/crawleraula1/geckodriver",options=opts)

url = 'https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.XKjZwhRv-V5'


driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
li = soup.find_all('li', attrs={'class':'forecast-tombstone'})

cidade = soup.find("h2",attrs={'class':'panel-title'})

print("City:"+cidade.text)
print("Date now:"+str(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S")))

print("------------")

for item in li:
    name = item.find('p',{'class':'period-name'})
    temp = item.find('p',{'class':'temp'})
    print("Period: "+name.text)
    print("Temp: "+ temp.text)

    print("------------------")

