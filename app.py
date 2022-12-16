import streamlit as st
import httpx
import time


col1, col2 = st.columns(2)

def getCep(cep):
    api = "https://brasilapi.com.br/api/cep/v2/"
    result = httpx.get(api + cep)
    return result

def resultCep(cep):
    with col2:
        action = getCep(cep)
        with st.spinner(text='processando ...'):
            time.sleep(1)
            if action.status_code == 200:
                    st.success('Concluido')
            elif action.status_code == 404:
                    st.error('!Erro - CEP não encontrado')

        st.write(action)
        st.write(action.json())

with col1:
    with st.form(key='form'):
        cep = st.text_input('DIGITE O CEP:')
        st.form_submit_button('BUSCAR', on_click=resultCep(cep))

