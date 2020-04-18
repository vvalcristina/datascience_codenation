#Streamlit -> Primeiros passos
import streamlit as st

def main():

    #Titulo
    st.title("Hello World")

    #Criando um botão
    st.markdown('Botao')
    botao = st.button('Botao')
    if botao:
        st.markdown('Clicado')

    #Criando um checkbox
    check = st.checkbox('Checkbox')
    st.markdown(check)
    if check:
        st.markdown('Clicado')

    #Criando um radio
    st.markdown('Radio')
    radio = st.radio('Escolha as opções', ('Opt1', 'Opt2'))
    if radio == 'Opt1':
        st.markdown('Opt1')
    if radio == 'Opt2':
        st.markdown('Opt2')

    #Criando um SelectBox
    st.markdown('Selectbox')
    select = st.selectbox('Choose opt', ('Opt1', 'Opt2'))
    if select == 'Opt1':
        st.markdown('Opt1')
    if select == 'Opt2':
        st.markdown('Opt2')

    #Multiselect
    st.markdown('Multiselect')
    multi = st.multiselect('Choose opt', ('Opt1', 'Opt2'))
    if multi == 'Opt1':
        st.markdown('Opt1')
    if multi == 'Opt2':
        st.markdown('Opt2')

    #Fazendo Upload de Arquivo
    st.markdown('File Uploader')
    file = st.file_uploader('Choose your file', type = 'csv')
    if file is not None:
        st.markdown("Não está vazio")


if __name__ == '__main__':
    main()
