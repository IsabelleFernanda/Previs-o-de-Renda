import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

# Configuração da página
st.set_page_config(page_title="Previsão de Renda", page_icon="https://web-summit-avenger.imgix.net/production/logos/original/68de83f411416128ffe8c1a3789a99b5ba538a6f.png?ixlib=rb-3.2.1&auto=format&fit=fill&fill=solid&fill-color=white&w=600&h=600z")

# Carregar os dados
X = pd.read_csv('X.csv')
y = pd.read_csv('y.csv')

# Criar e treinar o modelo
modelo = DecisionTreeRegressor(random_state=42, max_depth=5, min_samples_leaf=4, min_samples_split=2)
modelo.fit(X, y)

# Função para prever a renda
def simulacao_renda(dados):
    dados = np.array(dados).reshape(1, -1)
    renda_prevista = modelo.predict(dados)
    return renda_prevista[0]

# Ajuste do espaçamento do título
st.markdown("""
    <style>
        .css-18e3th9 {
            padding-top: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Título do Formulário
st.title("Previsão de Renda de Clientes")
st.markdown("### Formulário de Informações")
st.text("Preencha o formulário com suas informações para prever qual será sua renda")

# Campos de Entrada com valores padrão ajustados para None
data_ref = st.date_input("Data de Referência", value=None)
posse_veiculo = st.selectbox("Possui Veículo?", ["Selecione", "Sim", "Não"], index=0)
posse_imovel = st.selectbox("Possui Imóvel?", ["Selecione", "Sim", "Não"], index=0)
qtd_filhos = st.number_input("Quantidade de Filhos", value=None)
idade = st.number_input("Idade", value=None)
tempo_emprego = st.number_input("Tempo de Emprego (em anos)", value=None)
qt_pessoas_residencia = st.number_input("Quantidade de Pessoas na Residência", value=None)
sexo = st.selectbox("Sexo", ["Selecione", "Feminino", "Masculino"], index=0)
tipo_renda = st.selectbox("Tipo de Renda", ["Selecione", "assalariado", "bolsista", "empresario", "pensionista", "servidor_publico"], index=0)
educacao = st.selectbox("Escolaridade", ["Selecione", "primario", "pos_graduacao", "secundario", "superior_completo", "superior_incompleto"], index=0)
estado_civil = st.selectbox("Estado Civil", ["Selecione", "casado", "separado", "solteiro", "uniao", "viuvo"], index=0)
tipo_residencia = st.selectbox("Tipo de Residência", ["Selecione", "aluguel", "casa", "com_os_pais", "comunitario", "estudio", "governamental"], index=0)

# Função para coletar e processar dados
def enviar_dados():
    dados = [
        1 if posse_veiculo == 'Sim' else 0,
        1 if posse_imovel == 'Sim' else 0,
        qtd_filhos,
        idade,
        tempo_emprego,
        qt_pessoas_residencia,
        1 if sexo == 'Feminino' else 0,
        1 if sexo == 'Masculino' else 0,
        1 if tipo_renda == 'assalariado' else 0,
        1 if tipo_renda == 'bolsista' else 0,
        1 if tipo_renda == 'empresario' else 0,
        1 if tipo_renda == 'pensionista' else 0,
        1 if tipo_renda == 'servidor_publico' else 0,
        1 if educacao == 'primario' else 0,
        1 if educacao == 'pos_graduacao' else 0,
        1 if educacao == 'secundario' else 0,
        1 if educacao == 'superior_completo' else 0,
        1 if educacao == 'superior_incompleto' else 0,
        1 if estado_civil == 'casado' else 0,
        1 if estado_civil == 'separado' else 0,
        1 if estado_civil == 'solteiro' else 0,
        1 if estado_civil == 'uniao' else 0,
        1 if estado_civil == 'viuvo' else 0,
        1 if tipo_residencia == 'aluguel' else 0,
        1 if tipo_residencia == 'casa' else 0,
        1 if tipo_residencia == 'com_os_pais' else 0,
        1 if tipo_residencia == 'comunitario' else 0,
        1 if tipo_residencia == 'estudio' else 0,
        1 if tipo_residencia == 'governamental' else 0
    ]

    # Verificar se o número de variáveis corresponde ao esperado
    if len(dados) != X.shape[1]:
        st.error(f"Erro: O número de variáveis ({len(dados)}) não corresponde ao esperado ({X.shape[1]}).")
        return

    # Previsão da renda
    renda_prevista = simulacao_renda(dados)

    # Exibir a renda prevista
    st.success(f"Renda prevista: R${renda_prevista:.2f}")

# Botão para Enviar e resetar os campos
if st.button("Enviar"):
    enviar_dados()

# Função para limpar o formulário
def limpar_formulario():
    st.session_state['data_ref'] = None
    st.session_state['posse_veiculo'] = ""
    st.session_state['posse_imovel'] = ""
    st.session_state['qtd_filhos'] = None
    st.session_state['idade'] = None
    st.session_state['tempo_emprego'] = None
    st.session_state['qt_pessoas_residencia'] = None
    st.session_state['sexo'] = ""
    st.session_state['tipo_renda'] = ""
    st.session_state['educacao'] = ""
    st.session_state['estado_civil'] = ""
    st.session_state['tipo_residencia'] = ""


# Botão para Limpar Formulário
if st.button("Limpar Formulário"):
    limpar_formulario()
