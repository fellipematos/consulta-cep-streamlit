## Consulta CEP

Aplicação web para consultar endereço a partir do CEP. Tem como resposta estado, cidade, bairro, logradouro, latitude e longitude.

**Desenvolvido em Python**

**Bibliotecas utilizadas:** Streamlit e HTTPX

**API Utilizada no projeto:** https://brasilapi.com.br/

![Screenshot](img/screenshot.JPG?raw=true)
<HR>

**Como executar:**
Crie um ambiente virtual e clone o repositório

    python -m virtualenv .venv
    source .venv/Script/activate #windows
    source .venv/bin/activate #linux
    git clone 

Instale as bibliotecas

    python -m pip install -r requirements

Inicie o Streamlit

    python -m streamlit run app.py

<HR>

![Streamlit](img/streamlit.JPG?raw=true)
![BrasilAPI](img/brasilapi.JPG?raw=true)
