# Previsão de Renda

![Logo do Projeto](ebac_icon.png)  

Este repositório contém um projeto de **previsão de renda** desenvolvido com base em dados de clientes. O projeto inclui a criação de um modelo preditivo para estimar a renda e a implementação de duas aplicações interativas utilizando **Streamlit**. Este é o **segundo projeto** concluído no curso **Profissão Cientista de Dados** da EBAC, focando na aplicação prática de técnicas de análise de dados e machine learning.

## Descrição do Projeto

O objetivo deste projeto é criar um modelo preditivo para estimar a renda de clientes com base em várias características demográficas e socioeconômicas. O modelo é baseado em um algoritmo de regressão e utiliza as variáveis de entrada para gerar previsões precisas de renda.

As aplicações Streamlit permitem que os usuários interajam com o modelo e explorem os dados por meio de gráficos e visualizações.

## Tecnologias Utilizadas

- **Python 3.x**
- **Streamlit**
- **pandas**
- **numpy**
- **matplotlib**
- **seaborn**
- **statsmodels**
- **plotly**
- scikit-learn


## Estrutura do Repositório

- **notebook_projeto.ipynb**: Contém o código do projeto de previsão de renda, incluindo a análise de dados e o treinamento do modelo preditivo.
- **simulador_previsao_renda.py**: Aplicação Streamlit que permite aos usuários preencher um formulário com suas informações e obter a previsão da renda com base nos dados fornecidos.
- **streamlit_projeto_2.py**: Aplicação Streamlit que exibe análises gráficas, incluindo:
  - Análises univariadas e bivariadas das variáveis.
  - Visualizações da renda por variável ao longo do tempo.

## Como rodar as aplicações
Sim, você tem razão! Em vez de mencionar apenas o arquivo `requirements.txt`, seria interessante verificar se o **Git** e o **Streamlit** estão instalados no computador, pois essas ferramentas são essenciais para rodar o projeto corretamente.

Aqui está uma versão ajustada da seção no seu `README.md`, levando isso em consideração:

---

### Como Rodar as Aplicações

1. **Verifique se o Git está instalado**:
   Abra o terminal (CMD ou PowerShell) e execute o seguinte comando:
   ```bash
   git --version
   ```
   Se o Git não estiver instalado, você pode baixá-lo e instalá-lo a partir de [https://git-scm.com/downloads](https://git-scm.com/downloads).

2. **Verifique se o Streamlit está instalado**:
   Execute o comando abaixo para verificar se o Streamlit está instalado:
   ```bash
   streamlit --version
   ```
   Se o Streamlit não estiver instalado, você pode instalá-lo com o seguinte comando:
   ```bash
   pip install streamlit
   ```

3. **Clone o repositório**:
   Se o Git estiver instalado corretamente, clone o repositório utilizando o seguinte comando:
   ```bash
   git clone https://github.com/IsabelleFernanda/Previsao-Renda.git
   cd Previsao-Renda
   ```

4. **Instale as dependências necessárias**:
   Use o comando abaixo para instalar as dependências:
   ```bash
   pip install streamlit pandas scikit-learn matplotlib numpy
   ```
   Caso não tenha esse arquivo, apenas certifique-se de ter as dependências essenciais como **Streamlit** instaladas.

5. **Rodando as Aplicações**:
   Após instalar as dependências, você pode rodar uma das aplicações com o seguinte comando:
   ```bash
   streamlit run simulador_previsao_renda.py
   ```
   ou
   ```bash
   streamlit run streamlit_projeto_2.py
   ```


## Vídeos das Aplicações



- **Análises Gráficas**:
  


https://github.com/user-attachments/assets/a7fe8303-6d26-4809-bb56-cea23bb87d1f




- **Simulador de Previsão de Renda**:
  


https://github.com/user-attachments/assets/185f6da6-b92a-4f2c-8ced-b76695f42acb



