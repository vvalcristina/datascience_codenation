# Aprendendo a utilizar o Pandas em conjunto com o Streamlit
import streamlit as st
import pandas as pd


def main():
    st.title('AceleraDev DataScience')
    st.image('logo.png')
    file = st.file_uploader('Upload your file', type = 'csv')
    if file is not None:
        slider = st.slider('Valores', 1,100)
        #importando Df
        df = pd.read_csv(file)
        st.dataframe(df.head(slider))

        st.markdown('Markdown')
        st.table(df.head(slider))

        #Retorna o nome das colunas
        st.write(df.columns)

        #Retorna a média
        st.table(df.groupby('species')['petal_width'].mean())


if __name__ == '__main__':
    main()
