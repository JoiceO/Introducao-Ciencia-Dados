# -*- coding: utf-8 -*-
"""semana_3_exercícios_de_apoio_e_anotações.ipynb

##Anotações das aulas
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

"""###Maptplotlib """

x=[1,2,3,4,5,6,7,8,9,10]
y=[1,2,3,4,2,6,7,8,9,10]

#Gráfico 1
plt.scatter(x,y) #gráfico de dispersão de acordo com os pontos passados acima no X e Y
plt.show

x1=np.arange(-100,100,1) #dados de -100 a 100

x1

#gráfico 2, em que o valor de Y está como o quadrado do valor de X)
plt.plot(x1,x1**2)
plt.show()

dias=np.arange(1,31)
dias

vacinados=np.random.randint(0, 1000,30)
contagios=np.random.randint(0,700,30)

vacinados

#Gráfico 3

#plt.style.use('classic') # estilo clássico
#plt.style.use('dark_background') #fundo escuro
plt.style.use('default') #estilo padrão

plt.figure(figsize=(10,5)) #tamanho
plt.bar(dias,vacinados) #eixo x e eixo y
plt.plot(dias,contagios,'r')
plt.ylabel('Vacinados por Dia')
plt.show()

#dataframe a partir do gráfico 3
dados=pd.DataFrame(dias, columns=['Dias'])

dados['Contágios']=contagios
dados['Vacinados']=vacinados

dados

#gráfico 4 - a partir do dataframe acima
dados.plot(kind='bar', x='Dias', y='Vacinados') #gráfico de barras

"""###Seaborn"""

#Gráfico 5 - Vacinados x Contágios por dia
sns.barplot(data=dados, x='Dias', y='Contágios')
sns.barplot(data=dados, x='Dias', y='Vacinados', color='r')
#sns.lineplot(data=dados, x='Dias', y='Vacinados', color='r')

"""###Raspagem"""

import requests
from bs4 import BeautifulSoup
#import pandas as pd

html=requests.get("https://statisticstimes.com/tech/top-computer-languages.php").content
soup=BeautifulSoup(html,'html5lib')

#mostrando o primeiro parágrafo por meio da tag <p>
primeiro_paragrafo=soup.find('p')
primeiro_paragrafo

todos_paragrafos=soup.find_all('p') #todos os parágrafos da página
todos_paragrafos

todoslinks=soup.find_all('a') #todos os links da página
todoslinks

#mostrando a variável ´´´primeiro_paragrafo´´´ em texto
primeiro_paragrafo.text

#Dentro da página há a tabela "PYPL Index (Worldwide)" que pode ser raspada desta forma:
tabela=soup.find('table',{'id':'table_id1'}).find('tbody')
tabela

#limpando a tabela acima e mostrando em texto:
linhas=tabela.find_all('tr')
for linha in linhas:
    dado=linha.find_all('td')
    print(dado[0].text)
    print(dado[2].text)
    print(dado[3].text)
    print('-----')

#Montando: 1) uma lista e 2) um dataframe
#1
linguagem=[]
pontos=[]
for linha in linhas:
    dado=linha.find_all('td')
    linguagem.append(dado[2].text)
    pontos.append(dado[3].text)
print(linguagem)
print (pontos)

#2
dados=pd.DataFrame(linguagem, columns=['Linguagem'])
dados['Pontos']=pontos
dados

"""##Exercícios

1. Carregue as bibliotecas NumPy, Pandas, BeautifulSoup, MatPlotLib, Requests, JSON e Seaborn
"""

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
import json
import seaborn as sns

"""2. Entre no site https://db-engines.com/en/ranking, faça um scraping e gere um DataFrame com a lista de banco de dados do Ranking."""

ranking  =requests.get("https://db-engines.com/en/ranking").content
soup = BeautifulSoup(ranking,'html5lib')

tabela_ranking = soup.find('table',{'class':'dbi'}).find('tbody')
tabela_ranking

linhas=tabela_ranking.find_all('tr')
contalinhas=0
banco=[]
pontos=[]
for linha in linhas:
    contalinhas+=1
    if contalinhas>3:
        dado=linha.find_all('td')
        dado2=linha.find('a')
        pontos.append(float(dado[3].text))
        #ao pegar o dado do link, ele monta um array com as informações, onde a primeira (0) é o nome do banco
        banco.append(dado2.contents[0])

dados=pd.DataFrame(banco,columns=['Banco de Dados'])
dados['Pontos no Mês']=pontos
dados

"""3. Com a Biblioteca Seaborn gere um gráfico de colunas, indicando o nome do banco e a quantidade de pontos do banco no mês atual."""

plt.figure(figsize = (8,6)) #configurando a medida do gráfico plotado
sns.barplot(data=dados.head(5), x='Banco de Dados', y='Pontos no Mês')

"""4. Gere um novo Dataframe com apenas as 10 primeiras posições da lista, crie um campo de Share (porcentagem de relevância de cada Banco de Dados em relação aos 10 listados, baseado na quantidade de pontos que eles tem). Informe qual é a porcentagem e o nome do banco que aparece em primeiro lugar."""

dados2 = dados.head(10)

total = dados2['Pontos no Mês'].sum()
dados2['Share'] = ((dados2['Pontos no Mês']/total)*100)
dados2

"""5.  Usando MatPlotLib, gere um gráfico baseado no Share de cada banco em relação aos outros 9 da lista gerada no Exercício 4."""

plt.pie(dados2['Share'],labels=dados2['Banco de Dados'])
plt.show #gráfico de pizza, apesar de não ser o correto para demonstrar 10 itens

"""6. Usando o Dataframe completo, crie também uma coluna Share informado a porcentagem de relevância de cada banco em relação aos demais."""

#no exercício 4 foram listados os 10 primeiros. Agora, serão todos
lista_completa = dados['Pontos no Mês'].sum()
dados['Share'] = (dados['Pontos no Mês']/total)*100
dados

"""7. Com o Dataframe gerado no Exercício 6, gere um arquivo do tipo CSV chamado “db-ranking.csv”."""

dados.to_csv("db-ranking.csv")

"""8. O Banco Central dispõe de um conjunto de APIs, sendo que uma delas é o valor do Dólar. Nesse endereço tem algumas delas: https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/recursos, sendo que a primeira delas é capaz de gerar a cotação do dólar de uma determinada data. <br> 
Utilizando Json, realize uma consulta direta a API e informe a cotação de venda do dólar do dia 16/09/2008.
"""

bacen = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='09-16-2008'&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"
resposta = requests.get(bacen)
cotacao = json.loads(resposta.text)
cotacao

print("A cotação de venda do dólar, em 16/09/2008, foi de:")
print(cotacao['value'][0]['cotacaoVenda'])
