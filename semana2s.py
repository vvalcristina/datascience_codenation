#Aplicação desenvolvida pelo professor durante a Semana 2

#Importações
import streamlit as st
import pandas as pd
#Para fazer Download (Desenvolvida pela comunidade do Streamlit)
import base64

#Função de download
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

def main():
    st.image('logo.png', width= 200)
    st.title('AceleraDev Data Science')
    st.subheader('Semana 2 - Pré-processamento de Dados em Python')
    st.image('https://media.giphy.com/media/KyBX9ektgXWve/giphy.gif', width=200)
    file  = st.file_uploader('Escolha a base de dados que deseja analisar (.csv)', type = 'csv')
    if file is not None:
        st.subheader('Analisando os dados')
        #Leitura dos arquivos
        df = pd.read_csv(file)

        #Shape: me retorna uma tupla
        st.markdown('**Número de linhas:**')
        st.markdown(df.shape[0])
        st.markdown('**Número de colunas:**')
        st.markdown(df.shape[1])
        st.markdown('**Visualizando o dataframe**')
        number = st.slider('Escolha o numero de colunas que deseja ver', min_value=1, max_value=20)
        st.dataframe(df.head(number))

        #Passando como lista o número das colunas
        st.markdown('**Nome das colunas:**')
        st.markdown(list(df.columns))

        #Cuidado ao passar os valores como índices: valores se modificam
        #Cria-se sempre um DataDrame auxiliar (exploração) para manipulação dos dados
        exploracao = pd.DataFrame({'nomes' : df.columns, 'tipos' : df.dtypes, 'NA #': df.isna().sum(), 'NA %' : (df.isna().sum() / df.shape[0]) * 100})

        st.markdown('**Contagem dos tipos de dados:**')
        st.write(exploracao.tipos.value_counts())

        #Filtra meu dataframe onde os colunas forem tipo int64 e me retorna uma lista na tela (nomes)
        st.markdown('**Nomes das colunas do tipo int64:**')
        st.markdown(list(exploracao[exploracao['tipos'] == 'int64']['nomes']))

        #Filtrando colunas tipo float e retorno tipo nomes
        st.markdown('**Nomes das colunas do tipo float64:**')
        st.markdown(list(exploracao[exploracao['tipos'] == 'float64']['nomes']))

        #Filtro colunas objects e retorno nomes
        st.markdown('**Nomes das colunas do tipo object:**')
        st.markdown(list(exploracao[exploracao['tipos'] == 'object']['nomes']))

        #Retorna o percentual de dados faltantes
        st.markdown('**Tabela com coluna e percentual de dados faltantes :**')
        st.table(exploracao[exploracao['NA #'] != 0][['tipos', 'NA %']])


        st.subheader('Inputaçao de dados númericos :')

        #Como eu tiver rodando o slider todos os valores abaixo serão retornados por essa lista de nomes
        percentual = st.slider('Escolha o limite de percentual faltante limite para as colunas vocë deseja inputar os dados', min_value=0, max_value=100)
        lista_colunas = list(exploracao[exploracao['NA %']  < percentual]['nomes'])

        #Seleciona o método
        select_method = st.radio('Escolha um metodo abaixo :', ('Média', 'Mediana'))
        st.markdown('Você selecionou : ' +str(select_method))

        if select_method == 'Média':
            #Cria um novo dataframe auxiliar(df_inputado)
            df_inputado = df[lista_colunas].fillna(df[lista_colunas].mean())
            exploracao_inputado = pd.DataFrame({'nomes': df_inputado.columns, 'tipos': df_inputado.dtypes, 'NA #': df_inputado.isna().sum(),
                                       'NA %': (df_inputado.isna().sum() / df_inputado.shape[0]) * 100})
            st.table(exploracao_inputado[exploracao_inputado['tipos'] != 'object']['NA %'])
            st.subheader('Dados Inputados faça download abaixo : ')
            #Download do Dataframe que foi inputado
            st.markdown(get_table_download_link(df_inputado), unsafe_allow_html=True)

         #Input de dados com a média
        if select_method == 'Mediana':
            df_inputado = df[lista_colunas].fillna(df[lista_colunas].mean())
            exploracao_inputado = pd.DataFrame({'nomes': df_inputado.columns, 'tipos': df_inputado.dtypes, 'NA #': df_inputado.isna().sum(),
                                       'NA %': (df_inputado.isna().sum() / df_inputado.shape[0]) * 100})
            st.table(exploracao_inputado[exploracao_inputado['tipos'] != 'object']['NA %'])
            st.subheader('Dados Inputados faça download abaixo : ')
            st.markdown(get_table_download_link(df_inputado), unsafe_allow_html=True)


if __name__ == '__main__':
	main()
