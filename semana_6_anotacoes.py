# -*- coding: utf-8 -*-
"""semana_6_anotacoes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cWmTCz1-4Ri1kawZkgHGQqg8kJSP4UY-

#Anotações
"""

from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df

"""Gerar um Target (Alvo)"""

df['target']=iris.target

df

"""Gerar um target name (apenas para demonstrar)"""

iris.target_names

df['target_name']=iris.target_names[df['target']]

df

"""Determinar as features (colunas, atributos) que vão fazer parte do estudo"""

iris_features=['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']

"""Determinar nosso alvo (y), lembrando que por fazer uma classificação usando KNN precisamos de um alvo numérico"""

y=df.target

"""Selecionar nossos dados, as features que serão utilizadas (X)"""

X=df[iris_features]

X

y

###Usar Scikit-learn
###Define = Escolha de modelo (define parâmetros)
###Fit = Treinar
###Predict = Fazer a Predição
###Evaluate = Avaliar os resultados

"""Importar o algoritmo KNN"""

from sklearn.neighbors import  KNeighborsClassifier

"""Selecionar o modelo"""

modelo = KNeighborsClassifier(3)

"""Treinar o modelo"""

modelo.fit(X,y)

X

"""Ver a predição"""

print(modelo.predict(X))

"""Vamos observar a Acurácia (porcentagem de acertos), lembrando que estamos colocando pra validação os mesmos dados que foram treinados."""

modelo.score(X,y)