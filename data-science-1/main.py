#!/usr/bin/env python
# coding: utf-8

# # Desafio 3
# 
# Neste desafio, iremos praticar nossos conhecimentos sobre distribuições de probabilidade. Para isso,
# dividiremos este desafio em duas partes:
#     
# 1. A primeira parte contará com 3 questões sobre um *data set* artificial com dados de uma amostra normal e
#     uma binomial.
# 2. A segunda parte será sobre a análise da distribuição de uma variável do _data set_ [Pulsar Star](https://archive.ics.uci.edu/ml/datasets/HTRU2), contendo 2 questões.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Setup_ geral

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sct
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF


# In[2]:


#%matplotlib inline

from IPython.core.pylabtools import figsize


figsize(12, 8)

sns.set()


# ## Parte 1

# ### _Setup_ da parte 1

# In[3]:


np.random.seed(42)
    
dataframe = pd.DataFrame({"normal": sct.norm.rvs(20, 4, size=10000),
                     "binomial": sct.binom.rvs(100, 0.2, size=10000)})


# ## Inicie sua análise a partir da parte 1 a partir daqui

# In[4]:


# Sua análise da parte 1 começa aqui.
dataframe.head()


# In[5]:


normal = np.percentile(dataframe['normal'], [25, 50, 75])
binomial = np.percentile(dataframe['binomial'], [25, 50, 75])
tuple(np.around(normal-binomial, 3))


# In[6]:


#Gravando o intervalo positivo e negativo

interv1 = (dataframe['normal'].mean() + dataframe['normal'].std())
interv2 = (dataframe['normal'].mean() - dataframe['normal'].std())

#Calculando a distribuição normal dos intervalos 

float(ECDF(dataframe['normal'])(interv1) - ECDF(dataframe['normal'])(interv2))


# In[7]:





# In[22]:





# ## Questão 1
# 
# Qual a diferença entre os quartis (Q1, Q2 e Q3) das variáveis `normal` e `binomial` de `dataframe`? Responda como uma tupla de três elementos arredondados para três casas decimais.
# 
# Em outra palavras, sejam `q1_norm`, `q2_norm` e `q3_norm` os quantis da variável `normal` e `q1_binom`, `q2_binom` e `q3_binom` os quantis da variável `binom`, qual a diferença `(q1_norm - q1 binom, q2_norm - q2_binom, q3_norm - q3_binom)`?

# In[8]:


def q1():
    # Retorne aqui o resultado da questão 1.
    
    #Calculando o percentil de 25,50,75%
    normal = np.percentile(dataframe['normal'], [25, 50, 75])
    binomial = np.percentile(dataframe['binomial'], [25, 50, 75])
    
    #salvando tupla
    return tuple(np.around(normal-binomial, 3)) 


# Para refletir:
# 
# * Você esperava valores dessa magnitude?
# 
# * Você é capaz de explicar como distribuições aparentemente tão diferentes (discreta e contínua, por exemplo) conseguem dar esses valores?

# ## Questão 2
# 
# Considere o intervalo $[\bar{x} - s, \bar{x} + s]$, onde $\bar{x}$ é a média amostral e $s$ é o desvio padrão. Qual a probabilidade nesse intervalo, calculada pela função de distribuição acumulada empírica (CDF empírica) da variável `normal`? Responda como uma único escalar arredondado para três casas decimais.

# In[9]:


def q2():
    # Retorne aqui o resultado da questão 2.
    #Gravando o intervalo positivo e negativo

    interv1 = (dataframe['normal'].mean() + dataframe['normal'].std())
    interv2 = (dataframe['normal'].mean() - dataframe['normal'].std())

    #Calculando a distribuição normal dos intervalos 

    return float(ECDF(dataframe['normal'])(interv1) - ECDF(dataframe['normal'])(interv2))    


# Para refletir:
# 
# * Esse valor se aproxima do esperado teórico?
# * Experimente também para os intervalos $[\bar{x} - 2s, \bar{x} + 2s]$ e $[\bar{x} - 3s, \bar{x} + 3s]$.

# ## Questão 3
# 
# Qual é a diferença entre as médias e as variâncias das variáveis `binomial` e `normal`? Responda como uma tupla de dois elementos arredondados para três casas decimais.
# 
# Em outras palavras, sejam `m_binom` e `v_binom` a média e a variância da variável `binomial`, e `m_norm` e `v_norm` a média e a variância da variável `normal`. Quais as diferenças `(m_binom - m_norm, v_binom - v_norm)`?

# In[10]:


def q3():
    # Retorne aqui o resultado da questão 3.
    
    #calculando a diferença da media
    media = np.around(dataframe['binomial'].mean() - dataframe['normal'].mean(), 3)
    
    #calculando a diferença da variancia
    variancia = np.around(dataframe['binomial'].var() - dataframe['normal'].var(), 3)
    
    #salvando a tupla
    tupla = (media, variancia)
    
    return tupla


# Para refletir:
# 
# * Você esperava valore dessa magnitude?
# * Qual o efeito de aumentar ou diminuir $n$ (atualmente 100) na distribuição da variável `binomial`?

# ## Parte 2

# ### _Setup_ da parte 2

# In[11]:


stars = pd.read_csv("pulsar_stars.csv")

stars.rename({old_name: new_name
              for (old_name, new_name)
              in zip(stars.columns,
                     ["mean_profile", "sd_profile", "kurt_profile", "skew_profile", "mean_curve", "sd_curve", "kurt_curve", "skew_curve", "target"])
             },
             axis=1, inplace=True)

stars.loc[:, "target"] = stars.target.astype(bool)


# ## Inicie sua análise da parte 2 a partir daqui

# In[12]:


# Sua análise da parte 2 começa aqui.
stars.head()


# In[13]:


#filtrando os resultados de mean_profile onde target == false em uma variavel auxiliar

aux = stars[stars['target'] == False]['mean_profile']

#criando a variavel padronizada 
false_pulsar_mean_profile_standardized = (aux - aux.mean())/aux.std()

#calculo da probabilidade associada aos quantis teoricos utilizando a CDF empririca
emp_pulsar = ECDF(false_pulsar_mean_profile_standardized)

#calculando os quantis teoricos
quantis_teoricos = sct.norm.ppf([0.80, 0.90, 0.95], loc=0, scale=1)


#calculo da probabilidade associada aos quantis teoricos utilizando a CDF empririca
emp_pulsar = ECDF(false_pulsar_mean_profile_standardized)(quantis_teoricos)

#formatando a tupla, arrendondando

tuple(np.around(emp_pulsar,3))


# In[14]:


#filtrando os resultados de mean_profile onde target == false em uma variavel auxiliar

aux = stars[stars['target'] == False]['mean_profile']

#criando a variavel padronizada 
false_pulsar_mean_profile_standardized = (aux - aux.mean())/aux.std()

#calculo dos percentis
percentil_pulsar = np.percentile(false_pulsar_mean_profile_standardized, [25, 50, 75])

#calculando os quantis teoricos
quantis_teoricos = sct.norm.ppf([0.25, 0.50, 0.75], loc=0, scale=1)

#formatando a tupla, arrendondando

tuple(np.around(percentil_pulsar-quantis_teoricos,3))


# In[21]:





# ## Questão 4
# 
# Considerando a variável `mean_profile` de `stars`:
# 
# 1. Filtre apenas os valores de `mean_profile` onde `target == 0` (ou seja, onde a estrela não é um pulsar).
# 2. Padronize a variável `mean_profile` filtrada anteriormente para ter média 0 e variância 1.
# 
# Chamaremos a variável resultante de `false_pulsar_mean_profile_standardized`.
# 
# Encontre os quantis teóricos para uma distribuição normal de média 0 e variância 1 para 0.80, 0.90 e 0.95 através da função `norm.ppf()` disponível em `scipy.stats`.
# 
# Quais as probabilidade associadas a esses quantis utilizando a CDF empírica da variável `false_pulsar_mean_profile_standardized`? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[15]:


def q4():
   #filtrando os resultados de mean_profile onde target == false em uma variavel auxiliar
    aux = stars[stars['target'] == False]['mean_profile']

    #criando a variavel padronizada 
    false_pulsar_mean_profile_standardized = (aux - aux.mean())/aux.std()

    #calculo da probabilidade associada aos quantis teoricos utilizando a CDF empririca
    emp_pulsar = ECDF(false_pulsar_mean_profile_standardized)

    #calculando os quantis teoricos
    quantis_teoricos = sct.norm.ppf([0.80, 0.90, 0.95], loc=0, scale=1)


    #calculo da probabilidade associada aos quantis teoricos utilizando a CDF empririca
    emp_pulsar = ECDF(false_pulsar_mean_profile_standardized)(quantis_teoricos)

    #formatando a tupla, arrendondando

    return tuple(np.around(emp_pulsar,3))
 


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?

# ## Questão 5
# 
# Qual a diferença entre os quantis Q1, Q2 e Q3 de `false_pulsar_mean_profile_standardized` e os mesmos quantis teóricos de uma distribuição normal de média 0 e variância 1? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[16]:


def q5():
    # Retorne aqui o resultado da questão 5.
    #filtrando os resultados de mean_profile onde target == false em uma variavel auxiliar

    aux = stars[stars['target'] == False]['mean_profile']
    
    #criando a variavel padronizada 
    false_pulsar_mean_profile_standardized = (aux - aux.mean())/aux.std()

    #calculo dos percentis
    percentil_pulsar = np.percentile(false_pulsar_mean_profile_standardized, [25, 50, 75])

    #calculando os quantis teoricos
    quantis_teoricos = sct.norm.ppf([0.25, 0.50, 0.75], loc=0, scale=1)

    #formatando a tupla, arrendondando

    return tuple(np.around(percentil_pulsar-quantis_teoricos,3))
    


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?
# * Curiosidade: alguns testes de hipóteses sobre normalidade dos dados utilizam essa mesma abordagem.
