import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

opts = Options()
opts.add_argument("--headless")
browser = webdriver.Firefox(executable_path="/home/patriciadesouzaramos/PycharmProjects/crawleraula1/geckodriver", options=opts)

cidades = ["Bauru, São Paulo","Pederneiras","Poços de Caldas"]
browser.get("https://weather.com/pt-BR/clima/10dias/l/2d32f83c608a98da447936afd58bcf00a01bc0735484895cb6660ef57a2ec71f")
time.sleep(5)

field_input = browser.find_element_by_xpath("//html/body/div[1]/div/div/div[8]/div[2]/div/div/div/div[1]/div/div[1]/div/input");

for cidade in cidades:
    print(cidade)

    field_input.send_keys(cidade)

    time.sleep(5)

    search = BeautifulSoup(browser.page_source, 'html.parser')
    list_find = search.find("div", {'class': 'styles__inner__3moHD'})

    search_url = list_find.find("ul").find_all("li")

    table = browser.find_element_by_class_name('twc-table')
    tbody = table.find_element_by_tag_name('tbody')

    print(browser.find_element_by_tag_name("h1").text)

    for tr in tbody.find_elements_by_tag_name("tr"):
        print("Dia: "+tr.find_elements_by_tag_name("td")[1].text)
        print("Descrição: "+tr.find_element_by_class_name("description").text)
        print("Temperatura:"+ tr.find_element_by_class_name("temp").text)
        print("Preciptação: "+ tr.find_element_by_class_name("precip").text)
        print("Vento: "+tr.find_element_by_class_name("wind").text)
        print("Humidade: "+tr.find_element_by_class_name("humidity").text)

        print("----------------------------")




