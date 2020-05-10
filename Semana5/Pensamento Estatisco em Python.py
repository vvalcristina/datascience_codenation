#!/usr/bin/env python
# coding: utf-8

# # Desafio 4
# 
# Neste desafio, vamos praticar um pouco sobre testes de hipóteses. Utilizaremos o _data set_ [2016 Olympics in Rio de Janeiro](https://www.kaggle.com/rio2016/olympic-games/), que contém dados sobre os atletas das Olimpíadas de 2016 no Rio de Janeiro.
# 
# Esse _data set_ conta com informações gerais sobre 11538 atletas como nome, nacionalidade, altura, peso e esporte praticado. Estaremos especialmente interessados nas variáveis numéricas altura (`height`) e peso (`weight`). As análises feitas aqui são parte de uma Análise Exploratória de Dados (EDA).
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Setup_ geral

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sct
import seaborn as sns
import statsmodels.api as sm


# In[2]:


#%matplotlib inline

from IPython.core.pylabtools import figsize


figsize(12, 8)

sns.set()


# In[3]:


athletes = pd.read_csv("athletes.csv")


# In[4]:


def get_sample(df, col_name, n=100, seed=42):
    """Get a sample from a column of a dataframe.
    
    It drops any numpy.nan entries before sampling. The sampling
    is performed without replacement.
    
    Example of numpydoc for those who haven't seen yet.
    
    Parameters
    ----------
    df : pandas.DataFrame
        Source dataframe.
    col_name : str
        Name of the column to be sampled.
    n : int
        Sample size. Default is 100.
    seed : int
        Random seed. Default is 42.
    
    Returns
    -------
    pandas.Series
        Sample of size n from dataframe's column.
    """
    np.random.seed(seed)
    
    random_idx = np.random.choice(df[col_name].dropna().index, size=n, replace=False)
    
    return df.loc[random_idx, col_name]


# ## Inicia sua análise a partir daqui

# In[5]:


# Sua análise começa aqui.
df = athletes
df.head()


# In[6]:


#Informações sobre o DataFrame analisado
df.info()


# In[7]:


df.shape


# In[8]:


#Vendo a estatística descritiva
df.describe()


# In[9]:


#Verificando se há dados nulos
df.isna().sum()


# ## Questão 1
# 
# Considerando uma amostra de tamanho 3000 da coluna `height` obtida com a função `get_sample()`, execute o teste de normalidade de Shapiro-Wilk com a função `scipy.stats.shapiro()`. Podemos afirmar que as alturas são normalmente distribuídas com base nesse teste (ao nível de significância de 5%)? Responda com um boolean (`True` ou `False`).

# In[10]:


def q1():
    height_get_sample = get_sample(df, 'height', n=3000)
    result = sct.shapiro(height_get_sample)
    result_bool = bool(result[1]>0.05)
    return result_bool
q1()


# H0: as alturas são normalmente distribuídas.
# 
# Após aplicarmos o teste de Shapiro-Wilk que retorna um booleano *false* H0 é rejeitada

# __Para refletir__:
# 
# * Plote o histograma dessa variável (com, por exemplo, `bins=25`). A forma do gráfico e o resultado do teste são condizentes? Por que?
# * Plote o qq-plot para essa variável e a analise.
# * Existe algum nível de significância razoável que nos dê outro resultado no teste? (Não faça isso na prática. Isso é chamado _p-value hacking_, e não é legal).

# In[11]:


#Histograma bins=25 
df.height.hist(bins=25)


# In[12]:


#Q-Q plot
sm.qqplot(df.height.dropna(), fit=True, line="45");


# __Refletindo__:
# 
# * A forma dos gráficos e o resultado são condizentes, a curtose do gráfico não se assemelha a uma distribuição normal. 
# 
# * O gráfico Q-Q plot nos mostra pequenos desvios nas caudas. 
# 
# * Com um nível de significância menor que 5.681722541339695e-07 pressupõe-se que os resultados sejam divergentes.

# In[13]:


#Nível de significância que retorna outro resultado no teste
height_get_sample = get_sample(df, 'height', n=3000)
result= sct.shapiro(height_get_sample)
print(result[1])


# ## Questão 2
# 
# Repita o mesmo procedimento acima, mas agora utilizando o teste de normalidade de Jarque-Bera através da função `scipy.stats.jarque_bera()`. Agora podemos afirmar que as alturas são normalmente distribuídas (ao nível de significância de 5%)? Responda com um boolean (`True` ou `False`).

# In[14]:


def q2():
    height_get_sample = get_sample(df, 'height', n=3000)
    result = sct.jarque_bera(height_get_sample)
    result_bool = bool(result[1]>0.05)
    return result_bool
q2()


# __Para refletir__:
# 
# * Esse resultado faz sentido?

# Sim, pois testamos essa mesma amostra com o Teste de Shapiro-Wilk.

# ## Questão 3
# 
# Considerando agora uma amostra de tamanho 3000 da coluna `weight` obtida com a função `get_sample()`. Faça o teste de normalidade de D'Agostino-Pearson utilizando a função `scipy.stats.normaltest()`. Podemos afirmar que os pesos vêm de uma distribuição normal ao nível de significância de 5%? Responda com um boolean (`True` ou `False`).

# In[15]:


def q3():
    weight_get_sample = get_sample(df, 'weight', n=3000)
    result = sct.normaltest(weight_get_sample)
    result_bool = bool(result[1]>0.05)
    return result_bool
q3()


# H0: as alturas são normalmente distribuídas.
# 
# Após aplicarmos o teste de D'Agostino-Pearson que retorna um booleano *false* , logo H0 é rejeitada

# __Para refletir__:
# 
# * Plote o histograma dessa variável (com, por exemplo, `bins=25`). A forma do gráfico e o resultado do teste são condizentes? Por que?
# * Um _box plot_ também poderia ajudar a entender a resposta.

# __Refletindo__:
# 
# * A forma gráfica é condizendo com os testes, pois o histograma não possui a forma de uma distribuição normal e esses dados possuem *outliers*.

# In[16]:


df.weight.hist(bins=25)


# In[17]:


sns.boxplot(df.weight)


# In[18]:


#Q-Q plot
sm.qqplot(df.weight.dropna(), fit=True, line="45");


# ## Questão 4
# 
# Realize uma transformação logarítmica em na amostra de `weight` da questão 3 e repita o mesmo procedimento. Podemos afirmar a normalidade da variável transformada ao nível de significância de 5%? Responda com um boolean (`True` ou `False`).

# In[19]:


df['log_weight'] = np.log(df.weight)
def q4():
    weight_get_sample = get_sample(df, 'log_weight', n=3000)
    result = sct.normaltest(weight_get_sample)
    result_bool = bool(result[1]>0.05)
    return result_bool
q4()


# __Para refletir__:
# 
# * Plote o histograma dessa variável (com, por exemplo, `bins=25`). A forma do gráfico e o resultado do teste são condizentes? Por que?
# * Você esperava um resultado diferente agora?

# __Refletindo__:
# 
# * A forma do gráfico é condizente com os resultados. Observando-se o histograma percebe-se que os dados dessa coluna mesmo sendo transformados em logaritmícos não seguem uma distribuição normal, mas se tornam mais uniformes.
# 
# * Esperava que o log torna-se os dados mais uniformes, os tornando próximos a uma distribuição normal, mas não necessariamente seguindo a mesma. Isso pode ser observado no gráfico Q-Q plot.

# In[20]:


df.log_weight.hist(bins=25)


# In[21]:


sns.boxplot(df.log_weight)


# In[22]:


sm.qqplot(athletes.log_weight.dropna(), fit=True, line='45');


# > __Para as questão 5 6 e 7 a seguir considere todos testes efetuados ao nível de significância de 5%__.

# ## Questão 5
# 
# Obtenha todos atletas brasileiros, norte-americanos e canadenses em `DataFrame`s chamados `bra`, `usa` e `can`,respectivamente. Realize um teste de hipóteses para comparação das médias das alturas (`height`) para amostras independentes e variâncias diferentes com a função `scipy.stats.ttest_ind()` entre `bra` e `usa`. Podemos afirmar que as médias são estatisticamente iguais? Responda com um boolean (`True` ou `False`).

# In[23]:


#Verificando os dados de nacionalidade (siglas)
df.nationality.unique()


# In[24]:


#Obtendo os atletas
bra = df.query('nationality == "BRA"')
usa = df.query('nationality == "USA"')
can = df.query('nationality == "CAN"')
def q5():
    #Verificando as médias entre Brasil e EUA
    result = sct.ttest_ind(bra.height, usa.height, equal_var=False, nan_policy='omit')
    result_bool = bool (result[1]>0.05)
    return result_bool
q5()


# A Hipótese nula é rejeitada, já que as médias das alturas dos atletas brasileiros e norte americanos não são estatisticamente iguais, conforme pode ser verificado no gráfico abaixo.

# In[25]:


#Histograma das alturas Brasileiras e Norte-Americanas
sns.distplot(bra.height.dropna(), label='BRA')
sns.distplot(usa.height.dropna(), label='USA')
plt.legend()


# ## Questão 6
# 
# Repita o procedimento da questão 5, mas agora entre as alturas de `bra` e `can`. Podemos afimar agora que as médias são estatisticamente iguais? Reponda com um boolean (`True` ou `False`).

# In[26]:


def q6():
    #Verificando as médias de alturas entre Brasil e Canada
    result = sct.ttest_ind(bra.height, can.height, equal_var=False, nan_policy='omit')
    result_bool = bool (result[1]>0.05)
    return result_bool
q6()


# A hipótese h0 de que as médias de alturas entre os atletas brasileiros e canadenses, para um intervalo de confiança de 5% são estatisticamente iguais.

# In[27]:


#Histograma das alturas Brasileiras e Canadenses
sns.distplot(bra.height.dropna(), label='BRA')
sns.distplot(can.height.dropna(), label='CAN')
plt.legend()


# ## Questão 7
# 
# Repita o procedimento da questão 6, mas agora entre as alturas de `usa` e `can`. Qual o valor do p-valor retornado? Responda como um único escalar arredondado para oito casas decimais.

# In[28]:


def q7():
    #Verificando as médias entre EUA e Canada
    result = sct.ttest_ind(usa.height, can.height, equal_var=False, nan_policy='omit')
    pvalue = round(result[1],8)
    return float(pvalue)
q7()


# Para um pValor de 0.00046601 com um nível de significância de 5% a hipótese nula (H0) de que a média de altura entre os atletas do Canadá e dos EUA são estatisticamente iguais.

# __Para refletir__:
# 
# * O resultado faz sentido?
# * Você consegue interpretar esse p-valor?
# * Você consegue chegar a esse valor de p-valor a partir da variável de estatística?

# __Refletindo__:
# 
# * Sim. Pois quando observamos a curva de distribuição de altura dos atletas do Brasil, Canadá e Estados Unidos da América conseguimos perceber a proximidade entre as curvas do Brasil e do Canadá e a distância da curva dos Estados Unidos da de ambos os países.
# 
# 

# In[29]:


#Plotando as 3 curvas para comparação
sns.distplot(bra.height.dropna(), label='BRASIL')
sns.distplot(usa.height.dropna(), label='EUA')
sns.distplot(can.height.dropna(), label='CANADA')
plt.legend()

