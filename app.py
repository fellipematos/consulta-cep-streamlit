import streamlit as st
import httpx
import time

#layout da pagina
col1, col2 = st.columns(2)

def getCep(cep):
    #consulta api
    api = "https://brasilapi.com.br/api/cep/v2/"
    result = httpx.get(api + cep)
    return result

def resultCep(cep):
    #processa o resultado
    with col2:
        action = getCep(cep)
        with st.spinner(text='buscando cep ...'):
            time.sleep(1)
            if action.status_code == 200:
                    st.success('Concluido')
            elif action.status_code == 404:
                    st.error('!Erro - CEP não encontrado')

        st.write(action)#print response
        st.write(action.json())#print informacoes

#formulario
with col1:
    st.markdown("## Digite o CEP")
    cep = st.text_input("")
    st.markdown("*00000-000 ou 00000000*")
    if cep == "":
        cep = "01311000"
    st.button('BUSCAR', on_click=resultCep(cep))
