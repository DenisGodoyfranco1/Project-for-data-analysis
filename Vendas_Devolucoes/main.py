import pandas as pd
import os 
import plotly.express as px

tabela_total = pd.DataFrame()
lista_arquivos = os.listdir('C:\\Users\\mystc\\OneDrive\\Documentos\\Project_pandas\\Project_one\\Vendas_Devolucoes')

for arquivos in lista_arquivos:
    if 'Vendas' in arquivos:
        # print(arquivos)
        tabela = pd.read_csv(f'C:\\Users\\mystc\\OneDrive\\Documentos\\Project_pandas\\Project_one\\Vendas_Devolucoes\\{arquivos}')
        tabela_total = tabela_total._append(tabela)

tabela_de_produtos = tabela_total.groupby('Produto').sum()
tabela_de_produtos = tabela_de_produtos[['Quantidade Vendida','Preco Unitario']].sort_values(by='Quantidade Vendida',ascending=False)

#Produto mais vendido
print(tabela_de_produtos)

#Produto que mais faturou
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()

tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_faturamento)

#Loja/Cidade que mais vendeu
tabelas_das_lojas = tabela_total.groupby('Loja').sum()
tabelas_das_lojas = tabelas_das_lojas[['Faturamento']].sort_values(by='Faturamento',ascending=False)
print(tabelas_das_lojas)

#Grafico
grafico = px.bar(tabelas_das_lojas, x=tabelas_das_lojas.index,y='Faturamento')
grafico.show() 