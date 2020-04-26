#Imports
#Altair Docs: https://altair-viz.github.io/
import pandas as pd
import streamlit as st
import altair as alt

#Histograma: recebe coluna e Dataframe
#tooltip: mostra a coluna iterativa
def criar_histograma(coluna, df):
    chart = alt.Chart(df, width=600).mark_bar().encode(
        alt.X(coluna, bin=True),
        y='count()', tooltip=[coluna, 'count()']
    ).interactive()
    return chart

#Grafico de Barras
def criar_barras(coluna_num, coluna_cat, df):
    bars = alt.Chart(df, width=600).mark_bar().encode(
        x=alt.X(coluna_num, stack='zero'),
        y=alt.Y(coluna_cat),
        tooltip=[coluna_cat, coluna_num]
    ).interactive()
    return bars

#BoxPlot
def criar_boxplot(coluna_num, coluna_cat, df):
    boxplot = alt.Chart(df, width=600).mark_boxplot().encode(
        x=coluna_num,
        y=coluna_cat
    )
    return boxplot

def criar_scatterplot(x, y, color, df):
    scatter = alt.Chart(df, width=800, height=400).mark_circle().encode(
        alt.X(x),
        alt.Y(y),
        color = color,
        tooltip = [x,y]
    ).interactive()
    return scatter

def main():
    #st.image('logo.png', width=200)
    st.title('AcerelaDev Data Science')
    st.subheader('Semana 3 - Análise de dados exploratória')
    file = st.file_uploader('Escolha a base de dados que deseja analisar (.csv)', type='csv')
    if file is not None:
        st.subheader('Estatística descritiva univariada')
        df = pd.read_csv(file)
        aux = pd.DataFrame({"colunas": df.columns, 'tipos':df.dtypes})
        colunas_numericas = list(aux[aux['tipos'] != 'object']['colunas'])
        colunas_object = list(aux[aux['tipos'] == 'object']['colunas'])
        colunas = list(df.columns)
        col = st.selectbox('Selecione a coluna: ', colunas_numericas)
        if col is not None:
            st.markdown('Selecione o que deseja analisar: ')
            mean = st.checkbox('Média')
            if mean:
                st.markdown(df[col].mean())
            median = st.checkbox('Mediana')
            if median:
                st.markdown(df[col].median())
            desvio_pad = st.checkbox('Desvio Padrão')
            if desvio_pad:
                st.markdown(df[col].std())
            kurtosis = st.checkbox('Kurtosis')
            if kurtosis:
                st.markdown(df[col].kurtosis())
            skewness = st.checkbox('Skewness')
            if skewness:
                st.markdown(df[col].skew())
            describe = st.checkbox('Describe')
            if describe:
                st.table(df[colunas_numericas].describe().transpose())
        st.subheader('Visualização dos dados')
        st.markdown('Selecione a visualização')
        histograma = st.checkbox('Histograma')
        if histograma:
            col_num = st.selectbox('Selecione a Coluna Numérica', colunas_numericas, key='unique')
            st.markdown('Histograma da coluna: '+str(col_num))
            st.write(criar_histograma(col_num,df))
        barras = st.checkbox('Gráfico de Barras')
        if barras:
            col_num_barras = st.selectbox('Selecione a Coluna Numérica', colunas_numericas, key='unique')
            col_cat_barras = st.selectbox('Selecione uma Coluna Categórica', colunas_object, key='unique')
            st.markdown('Gráfico de Barras da Coluna' + str(colunas_numericas) + 'pela coluna ' +str(colunas_object))
            st.write(criar_barras(col_num_barras, col_cat_barras, df))
        boxplot = st.checkbox('Boxplot')
        if boxplot:
            col_num_barras = st.selectbox('Selecione a Coluna Numérica', colunas_numericas, key='unique')
            col_cat_barras = st.selectbox('Selecione a uma Coluna Categórica', colunas_object, key='unique')
            st.markdown('Gráfico de Barras da Coluna' + str(colunas_numericas) + 'pela coluna ' +str(colunas_object))
            st.write(criar_barras(col_num_barras, col_cat_barras, df))

if __name__ == '__main__':
    main()
