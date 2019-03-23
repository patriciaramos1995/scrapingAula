import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/406/bauru-sp'
page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')

cidade = soup.find("h1",{"id":"momento-localidade"})
temperatura = soup.find("p",{"id":"momento-temperatura"})
condicao = soup.find("p",{"id":"momento-condicao"})
atualizacao = soup.find("p",{"id":"momento-atualizacao"})

print("Previsão do tempo de: "+ cidade.text.strip())

print("Data da pesquisa: " + str(datetime.now().strftime("%d %b %Y %H:%M:%S")))

print("Temperatura: "+ temperatura.text.strip())

print("Condição: "+ condicao.text.strip())

content =[]
for li in soup.find_all("ul",{"class":"condicoes-momento"}):
    for itens in list(li.find_all("li")):
        content.append(itens.text.strip())

print(content[0]+" : "+ content[4])
print(content[1]+" : "+ content[5])
print(content[2]+" : "+ content[6])
print(content[3]+" : "+ content[7].replace("\n",""))

print(atualizacao.text.strip())

