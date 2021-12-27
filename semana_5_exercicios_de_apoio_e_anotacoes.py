# -*- coding: utf-8 -*-
"""semana_5_exercicios de apoio e anotacoes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QsT5H2hk5HmEizIfzZJ_0Dlf18UFgZsF

#Exercícios

1 – Indique 3 algoritmos da biblioteca Scikit-Learn que podem ser utilizados tanto para regressão quanto para classificação.
"""

# Temos o SVM - Máquinas de vetor de suporte (Support-Vector Machine), Stochastic Gradient Descent - SGD (Descida Gradiente Estocástica) e Árvores de decisão (Decision Tree)

"""2 – Importe os dados de um arquivo CSV de avaliações de um modelo de Iphone, disponível no Kaggle (https://www.kaggle.com/kmldas/apple-iphone-se-reviews-ratings).  Uso de bibliotecas é por sua conta!"""

import pandas as pd
modelos =pd.read_csv("semana_5_APPLE_iPhone_SE.csv")

"""3 – Quantas linhas tem o arquivo?"""

modelos

#O arquivo tem 9713 linhas

"""4 – Qual a média das notas atribuídas?"""

modelos.describe(include= 'all')

# A média de notas atribuidas eh de 4,456399

"""5 – Qual é a nota mais atribuída? Quantas vezes ela foi atribuída? Quantos % das notas totais"""

import sweetviz
eda = sweetviz.analyze(modelos)
eda.show_html()

modelos['Ratings'].value_counts()

# A nota mais atribuida eh o 5, aparecendo 6788 vezes, o que representa 70% do total

"""6 – Qual a nota menos atribuída? Qual a porcentagem que ela representa no todo?"""

# A nota menos atribuida eh o 2, aparecendo 199 vezes e representando 2% do total

#Outra opção para saber a % das notas é:
modelos['Ratings'].value_counts()/9713*100

"""7 – Um dos comentários atribuídos é “Worth every penny” ou seja, “Vale cada centavo”. Faça a alteração nessas linhas do texto em inglês para o texto em português."""

modelos['Comment'].replace("Worth every penny","Vale cada centavo",inplace=True)
modelos[modelos['Comment']=="Vale cada centavo"]

"""8 – Exclua todas as linhas em que o Comentário é “Hated it!”. Esse comentário aparece 23 vezes na lista de comentários."""

modelos.shape[0]

modelos.drop(modelos.loc[modelos['Comment']=='Hated it!'].index, inplace=True)

modelos.shape[0]