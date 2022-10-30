# -*- coding: utf-8 -*-
"""dados2020.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18AgAwHt8vVNF2yo0sdXY8jAMoVy8v70T
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive/')

df = pd.read_csv('/content/drive/MyDrive/Dataset/microdados_ed_basica_2020.CSV' , delimiter=';' ,encoding="windows_1258")
df

"""# Nova seção"""

cols = ['NU_ANO_CENSO','NO_REGIAO','CO_REGIAO','NO_UF','SG_UF','CO_UF','NO_MUNICIPIO','CO_MUNICIPIO','NO_MICRORREGIAO','CO_MICRORREGIAO','TP_LOCALIZACAO','TP_SITUACAO_FUNCIONAMENTO','IN_ENERGIA_INEXISTENTE','IN_ESGOTO_INEXISTENTE','IN_BANHEIRO','IN_BIBLIOTECA','IN_COZINHA','IN_LABORATORIO_CIENCIAS','IN_LABORATORIO_INFORMATICA','IN_PARQUE_INFANTIL','IN_QUADRA_ESPORTES','IN_REFEITORIO','IN_ACESSIBILIDADE_INEXISTENTE','IN_COMPUTADOR','IN_DESKTOP_ALUNO','IN_COMP_PORTATIL_ALUNO','IN_TABLET_ALUNO','IN_INTERNET','IN_ACESSO_INTERNET_COMPUTADOR','IN_PROF_ADMINISTRATIVOS','IN_PROF_SERVICOS_GERAIS','IN_PROF_BIBLIOTECARIO','IN_PROF_SAUDE','IN_PROF_COORDENADOR','IN_PROF_FONAUDIOLOGO','IN_PROF_PSICOLOGO','IN_PROF_ALIMENTACAO','IN_PROF_PEDAGOGIA','IN_PROF_SECRETARIO','IN_PROF_SEGURANCA','IN_PROF_MONITORES','IN_ALIMENTACAO','IN_EXAME_SELECAO','IN_REDES_SOCIAIS','IN_ORGAO_ASS_PAIS','IN_ORGAO_CONSELHO_ESCOLAR','TP_AEE','TP_ATIVIDADE_COMPLEMENTAR','IN_MEDIACAO_PRESENCIAL','IN_MEDIACAO_SEMIPRESENCIAL','IN_MEDIACAO_EAD','IN_DIURNO','IN_NOTURNO','IN_EAD','IN_BAS','IN_INF','IN_FUND','IN_MED','QT_MAT_BAS']
df2020_limpo = df[cols]
df2020_limpo

df2020_limpo.isnull().sum().sort_values(ascending=True)[:46]

df2020_limpo.isnull().sum().sort_values(ascending=True)[46:]

print(df2020_limpo.IN_PROF_SECRETARIO.value_counts())
df2020_limpo.IN_PROF_SECRETARIO.fillna(1, inplace = True)

print(df2020_limpo.IN_PROF_SERVICOS_GERAIS.value_counts())
df2020_limpo.IN_PROF_SERVICOS_GERAIS.fillna(1, inplace = True)

print(df2020_limpo.IN_PROF_BIBLIOTECARIO.value_counts())
df2020_limpo.IN_PROF_BIBLIOTECARIO.fillna(0, inplace = True)

print(df2020_limpo.IN_PROF_SAUDE.value_counts())
df2020_limpo.IN_PROF_SAUDE.fillna(0, inplace = True)

print(df2020_limpo.IN_PROF_COORDENADOR.value_counts())
df2020_limpo.IN_PROF_COORDENADOR.fillna(0, inplace = True)

print(df2020_limpo.IN_PROF_FONAUDIOLOGO.value_counts())
df2020_limpo.IN_PROF_FONAUDIOLOGO.fillna(0, inplace = True)

print(df2020_limpo.IN_PROF_PSICOLOGO.value_counts())
df2020_limpo.IN_PROF_PSICOLOGO.fillna(0, inplace = True)

print(df2020_limpo.IN_PROF_ALIMENTACAO.value_counts())
df2020_limpo.IN_PROF_ALIMENTACAO.fillna(1, inplace = True)

print(df2020_limpo.IN_PROF_PEDAGOGIA.value_counts())
df2020_limpo.IN_PROF_PEDAGOGIA.fillna(1, inplace = True)

print(df2020_limpo.IN_PROF_SEGURANCA.value_counts())
df2020_limpo.IN_PROF_SEGURANCA.fillna(0, inplace = True)

print(df2020_limpo.IN_ALIMENTACAO.value_counts())
df2020_limpo.IN_ALIMENTACAO.fillna(1, inplace = True)

print(df2020_limpo.IN_EXAME_SELECAO.value_counts())
df2020_limpo.IN_EXAME_SELECAO.fillna(0, inplace = True)

print(df2020_limpo.IN_REDES_SOCIAIS.value_counts())
df2020_limpo.IN_REDES_SOCIAIS.fillna(0, inplace = True)

print(df2020_limpo.IN_PROF_ADMINISTRATIVOS.value_counts())
df2020_limpo.IN_PROF_ADMINISTRATIVOS.fillna(1, inplace = True)

print(df2020_limpo.IN_ORGAO_CONSELHO_ESCOLAR.value_counts())
df2020_limpo.IN_ORGAO_CONSELHO_ESCOLAR.fillna(1, inplace = True)

print(df2020_limpo.TP_AEE.value_counts())
df2020_limpo.TP_AEE.fillna(0, inplace = True)

print(df2020_limpo.TP_ATIVIDADE_COMPLEMENTAR.value_counts())
df2020_limpo.TP_ATIVIDADE_COMPLEMENTAR.fillna(0, inplace = True)

print(df2020_limpo.IN_MEDIACAO_PRESENCIAL.value_counts())
df2020_limpo.IN_MEDIACAO_PRESENCIAL.fillna(1, inplace = True)

print(df2020_limpo.IN_MEDIACAO_SEMIPRESENCIAL.value_counts())
df2020_limpo.IN_MEDIACAO_SEMIPRESENCIAL.fillna(0, inplace = True)

print(df2020_limpo.IN_MEDIACAO_EAD.value_counts())
df2020_limpo.IN_MEDIACAO_EAD.fillna(0, inplace = True)

print(df2020_limpo.IN_PROF_MONITORES.value_counts())
df2020_limpo.IN_PROF_MONITORES.fillna(0, inplace = True)

print(df2020_limpo.IN_ORGAO_ASS_PAIS.value_counts())
df2020_limpo.IN_ORGAO_ASS_PAIS.fillna(0, inplace = True)

print(df2020_limpo.IN_ESGOTO_INEXISTENTE.value_counts())
df2020_limpo.IN_ESGOTO_INEXISTENTE.fillna(0, inplace = True)

print(df2020_limpo.IN_ACESSO_INTERNET_COMPUTADOR.value_counts())
df2020_limpo.IN_ACESSO_INTERNET_COMPUTADOR.fillna(0, inplace = True)

print(df2020_limpo.IN_ENERGIA_INEXISTENTE.value_counts())
df2020_limpo.IN_ENERGIA_INEXISTENTE.fillna(0, inplace = True)

print(df2020_limpo.IN_BANHEIRO.value_counts())
df2020_limpo.IN_BANHEIRO.fillna(1, inplace = True)

print(df2020_limpo.IN_BIBLIOTECA.value_counts())
df2020_limpo.IN_BIBLIOTECA.fillna(0, inplace = True)

print(df2020_limpo.IN_COZINHA.value_counts())
df2020_limpo.IN_COZINHA.fillna(1, inplace = True)

print(df2020_limpo.IN_LABORATORIO_INFORMATICA.value_counts())
df2020_limpo.IN_LABORATORIO_INFORMATICA.fillna(0, inplace = True)

print(df2020_limpo.IN_PARQUE_INFANTIL.value_counts())
df2020_limpo.IN_PARQUE_INFANTIL.fillna(0, inplace = True)

print(df2020_limpo.IN_QUADRA_ESPORTES.value_counts())
df2020_limpo.IN_QUADRA_ESPORTES.fillna(0, inplace = True)

print(df2020_limpo.IN_LABORATORIO_CIENCIAS.value_counts())
df2020_limpo.IN_LABORATORIO_CIENCIAS.fillna(0, inplace = True)

print(df2020_limpo.IN_ACESSIBILIDADE_INEXISTENTE.value_counts())
df2020_limpo.IN_ACESSIBILIDADE_INEXISTENTE.fillna(0, inplace = True)

print(df2020_limpo.IN_INTERNET.value_counts())
df2020_limpo.IN_INTERNET.fillna(1, inplace = True)

print(df2020_limpo.IN_REFEITORIO.value_counts())
df2020_limpo.IN_REFEITORIO.fillna(0, inplace = True)

print(df2020_limpo.IN_COMP_PORTATIL_ALUNO.value_counts())
df2020_limpo.IN_COMP_PORTATIL_ALUNO.fillna(0, inplace = True)

print(df2020_limpo.IN_DESKTOP_ALUNO.value_counts())
df2020_limpo.IN_DESKTOP_ALUNO.fillna(0, inplace = True)

print(df2020_limpo.IN_TABLET_ALUNO.value_counts())
df2020_limpo.IN_TABLET_ALUNO.fillna(0, inplace = True)

print(df2020_limpo.IN_COMPUTADOR.value_counts())
df2020_limpo.IN_COMPUTADOR.fillna(1, inplace = True)

print(df2020_limpo.IN_EAD.value_counts())
df2020_limpo.IN_EAD.fillna(0, inplace = True)

print(df2020_limpo.IN_NOTURNO.value_counts())
df2020_limpo.IN_NOTURNO.fillna(0, inplace = True)

print(df2020_limpo.IN_DIURNO.value_counts())
df2020_limpo.IN_DIURNO.fillna(1, inplace = True)

print(df2020_limpo.IN_FUND.value_counts())
df2020_limpo.IN_FUND.fillna(1, inplace = True)

print(df2020_limpo.IN_MED.value_counts())
df2020_limpo.IN_MED.fillna(0, inplace = True)

print(df2020_limpo.IN_INF.value_counts())
df2020_limpo.IN_INF.fillna(1, inplace = True)

print(df2020_limpo.IN_BAS.value_counts())
df2020_limpo.IN_BAS.fillna(1, inplace = True)

df2020_limpo.dropna(subset=['QT_MAT_BAS'], inplace = True)

df2020_limpo.isnull().sum().sort_values(ascending=True)[46:]

df2020_limpo

tab =df2020_limpo.groupby(by='SG_UF').agg({'QT_MAT_BAS':'mean'})
#ordenando a tabela
tab=tab.sort_values('SG_UF',ascending=True)
tab

condicoes = [(df2020_limpo['SG_UF'] == 'AC'), 
             (df2020_limpo['SG_UF'] == 'AL'), 
             (df2020_limpo['SG_UF'] == 'AM'),
             (df2020_limpo['SG_UF'] == 'AP'),
             (df2020_limpo['SG_UF'] == 'BA'),
             (df2020_limpo['SG_UF'] == 'CE'),
             (df2020_limpo['SG_UF'] == 'DF'),
             (df2020_limpo['SG_UF'] == 'ES'),
             (df2020_limpo['SG_UF'] == 'GO'),
             (df2020_limpo['SG_UF'] == 'MA'),
             (df2020_limpo['SG_UF'] == 'MG'),
             (df2020_limpo['SG_UF'] == 'MS'),
             (df2020_limpo['SG_UF'] == 'MT'),
             (df2020_limpo['SG_UF'] == 'PA'),
             (df2020_limpo['SG_UF'] == 'PB'),
             (df2020_limpo['SG_UF'] == 'PE'),
             (df2020_limpo['SG_UF'] == 'PI'),
             (df2020_limpo['SG_UF'] == 'PR'),
             (df2020_limpo['SG_UF'] == 'RJ'),
             (df2020_limpo['SG_UF'] == 'RN'),
             (df2020_limpo['SG_UF'] == 'RO'),
             (df2020_limpo['SG_UF'] == 'RR'),
             (df2020_limpo['SG_UF'] == 'RS'),
             (df2020_limpo['SG_UF'] == 'SC'),
             (df2020_limpo['SG_UF'] == 'SE'),
             (df2020_limpo['SG_UF'] == 'SP'),
             (df2020_limpo['SG_UF'] == 'TO')]

opcoes = [166, 282, 218, 250, 209, 286, 537, 289, 315, 165, 272, 382, 315, 210, 197, 264, 196, 269, 311, 235, 328, 198, 227, 258, 256, 333, 246]

df2020_limpo['MEDIA_QT_MAT_BAS'] = np.select(condicoes, opcoes)

df2020_limpo['MEDIA_QT_MAT_BAS']

df2020_limpo['QT_MAT_BAS']

df2020_limpo['SALDO_MATRICULAS_POSITIVO_MEDIAUF'] = (df2020_limpo['QT_MAT_BAS'] >= df2020_limpo['MEDIA_QT_MAT_BAS'])

df2020_limpo['SALDO_MATRICULAS_POSITIVO_MEDIAUF']

"""Construção Arvore"""

X = df2020_limpo[['CO_REGIAO','CO_UF','CO_MUNICIPIO','CO_MICRORREGIAO','TP_LOCALIZACAO','TP_SITUACAO_FUNCIONAMENTO','IN_ENERGIA_INEXISTENTE','IN_ESGOTO_INEXISTENTE','IN_BANHEIRO','IN_BIBLIOTECA','IN_COZINHA','IN_LABORATORIO_CIENCIAS','IN_LABORATORIO_INFORMATICA','IN_PARQUE_INFANTIL','IN_QUADRA_ESPORTES','IN_REFEITORIO','IN_ACESSIBILIDADE_INEXISTENTE','IN_COMPUTADOR','IN_DESKTOP_ALUNO','IN_COMP_PORTATIL_ALUNO','IN_TABLET_ALUNO','IN_INTERNET','IN_ACESSO_INTERNET_COMPUTADOR','IN_PROF_ADMINISTRATIVOS','IN_PROF_SERVICOS_GERAIS','IN_PROF_BIBLIOTECARIO','IN_PROF_SAUDE','IN_PROF_COORDENADOR','IN_PROF_FONAUDIOLOGO','IN_PROF_PSICOLOGO','IN_PROF_ALIMENTACAO','IN_PROF_PEDAGOGIA','IN_PROF_SECRETARIO','IN_PROF_SEGURANCA','IN_PROF_MONITORES','IN_ALIMENTACAO','IN_EXAME_SELECAO','IN_REDES_SOCIAIS','IN_ORGAO_ASS_PAIS','IN_ORGAO_CONSELHO_ESCOLAR','TP_AEE','TP_ATIVIDADE_COMPLEMENTAR','IN_MEDIACAO_PRESENCIAL','IN_MEDIACAO_SEMIPRESENCIAL','IN_MEDIACAO_EAD','IN_DIURNO','IN_NOTURNO','IN_EAD','IN_BAS','IN_INF','IN_FUND','IN_MED','QT_MAT_BAS']]
y = df2020_limpo['SALDO_MATRICULAS_POSITIVO_MEDIAUF'] #saída Classificação

X.to_csv("DadosTestes2020.csv")

from sklearn.model_selection import train_test_split
#Aqui se divide o dataset em treinamento e teste.
#30% dos dados serão para testes e o restante para treinamento.
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3) # 70% training
#X_train - dados de entrada para treinamento
#X_test dados de entrada para o teste
#y train classificações para treinamento
#y test classificações para teste

#importações
from sklearn import tree
from sklearn.tree import export_text
#cria um objeto classificador
arvore = tree.DecisionTreeClassifier()
#Realiza o treinamento - X é o conjunto de entrada e Y é a respectiva classificação.
classificador = arvore.fit(X_treino, y_treino)

#imprime a arovre no formato texto
caracteristicas = list(X.columns)
r = export_text(classificador, feature_names=caracteristicas)
print(r)

import matplotlib.pyplot as plt
plt.figure(figsize=(30, 14), dpi=200)
tree.plot_tree(classificador, fontsize=10, filled=True,
feature_names=caracteristicas,class_names=["Maior Probabilidade Evasão", "Menor Probabilidade Evasão"], max_depth=3)
plt.show()

#Usa a arvore para classificar o dataset de test.
#['CO_REGIAO','CO_UF','CO_MUNICIPIO','CO_MICRORREGIAO','TP_LOCALIZACAO','TP_SITUACAO_FUNCIONAMENTO','IN_ENERGIA_INEXISTENTE','IN_ESGOTO_INEXISTENTE','IN_BANHEIRO','IN_BIBLIOTECA','IN_COZINHA','IN_LABORATORIO_CIENCIAS','IN_LABORATORIO_INFORMATICA','IN_PARQUE_INFANTIL','IN_QUADRA_ESPORTES','IN_REFEITORIO','IN_ACESSIBILIDADE_INEXISTENTE','IN_COMPUTADOR','IN_DESKTOP_ALUNO','IN_COMP_PORTATIL_ALUNO','IN_TABLET_ALUNO','IN_INTERNET','IN_ACESSO_INTERNET_COMPUTADOR','IN_PROF_ADMINISTRATIVOS','IN_PROF_SERVICOS_GERAIS','IN_PROF_BIBLIOTECARIO','IN_PROF_SAUDE','IN_PROF_COORDENADOR','IN_PROF_FONAUDIOLOGO','IN_PROF_PSICOLOGO','IN_PROF_ALIMENTACAO','IN_PROF_PEDAGOGIA','IN_PROF_SECRETARIO','IN_PROF_SEGURANCA','IN_PROF_MONITORES','IN_ALIMENTACAO','IN_EXAME_SELECAO','IN_REDES_SOCIAIS','IN_ORGAO_ASS_PAIS','IN_ORGAO_CONSELHO_ESCOLAR','TP_AEE','TP_ATIVIDADE_COMPLEMENTAR','IN_MEDIACAO_PRESENCIAL','IN_MEDIACAO_SEMIPRESENCIAL','IN_MEDIACAO_EAD','IN_DIURNO','IN_NOTURNO','IN_EAD','IN_BAS','IN_INF','IN_FUND','IN_MED','QT_MAT_BAS']
ex_a = [1,11,1100015,11006,2,1,0.0,1.0,1.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0,0.0,1.0,0.0,0.0,1.0,0.0,0.0,1.0,0.0,1.0,0.0,7.0]
ex_b = [1,11,1100130,11003,2,1,0.0,0.0,1.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,1.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,1.0,0.0,0.0,1.0,1.0,1.0,0.0,24.0]
entrada = [ex_a, ex_b]
previsao = classificador.predict(entrada)
previsao

#Usa a arvore para classificar o dataset de test.
y_previsao = classificador.predict(X_teste)
y_previsao

#compara as classificações calculadas pela árvore y_pred com a classificações original do d
from sklearn import metrics
print("Precisão:",metrics.accuracy_score(y_teste, y_previsao))