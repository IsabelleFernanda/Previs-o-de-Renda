# Streamlit
import streamlit as st
from streamlit_option_menu import option_menu              # menu para sidebar do streamlit

# Análise de Dados
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go


### ### ### ### ### ###
# GRUPO DE FUNÇÕES
### ### ### ### ### ###

def gerar_grafico_univariada(df, column, max_bins=40):
    """
    Cria gráficos de barras para variáveis categóricas com personalização de cores, ordenação e exibição de valores.
    O número máximo de categorias (bins) pode ser ajustado com o parâmetro 'max_bins'.
    """
    # Contar a frequência de cada categoria
    categoria_counts = df[column].value_counts().reset_index()
    categoria_counts.columns = [column, 'Frequência']

    # Limitar o número de categorias (bins)
    categoria_counts = categoria_counts.head(max_bins)

    # Criar o gráfico com melhorias
    fig = px.bar(
        categoria_counts,
        x=column,
        y='Frequência',
        color=column,
        color_discrete_sequence=px.colors.qualitative.Set2,
        height=400,
        width=1000,
        text=None,  # Remove os rótulos das barras
        title=f'Distribuição de {column}'
    )
    fig.update_layout(width=600, height=400)
    fig.update_xaxes(categoryorder='total descending')

    # Retornar o gráfico para ser renderizado no Streamlit
    st.plotly_chart(fig)

######################################################################################

def gerar_grafico_bivariada(df, column):
    """Gera um gráfico de barras da renda média por uma variável categórica usando Plotly."""
    # Agrupa e ordena os dados
    agrupado = df.groupby(column)['renda'].mean().reset_index().sort_values(by='renda')

    # Cria o gráfico de barras com Plotly
    fig = px.bar(
        agrupado,
        x=column,
        y='renda',
        color=column,  
        text=None,
        title=f'Renda Média em função de {column}'
    )

    fig.update_layout(width=600, height=400)
    st.plotly_chart(fig)

##########################################################################################

def gerar_grafico_temporal(df, column):
    """
    Cria um gráfico de linha com sombra e cores personalizadas para mostrar 
    como os valores de 'column' mudam ao longo de 'data_ref'.
    """ 
    # Assegurando que 'data_ref' seja um datetime
    df['data_ref'] = pd.to_datetime(df['data_ref'])

    # Agrupando os dados e calculando média e desvio padrão
    agrupado = df.groupby(['data_ref', column])['renda'].agg(['mean', 'std']).reset_index()
    
    # Criando o gráfico de linhas principal
    fig = px.line(agrupado,
                  x="data_ref", 
                  y="mean", 
                  color=column, 
                  line_group=column,
                  line_shape="linear", 
                  markers=True,      
                  title=f'Evolução da {column} pela renda ao Longo dos Anos',
                  color_discrete_sequence=px.colors.sequential.Viridis  # Aplicando cores personalizadas
    )
    fig.update_layout(width=600, height=400)

    # Exibir no Streamlit
    st.plotly_chart(fig)


### ### ### ### ### ###
# CARREGAR OS ARQUIVOS
### ### ### ### ### ###

df = pd.read_csv('previsao_de_renda.csv')


#############
# FRONT-END #
#############



# Título-Subtítulo
st.set_page_config(
    page_title='Previsão de Renda',
    page_icon='📊',
    layout='wide'
)

# Customizando o estilo com CSS
st.markdown(
    """
    <style>
        /* Remover barras de rolagem e definir a altura da página */
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;  /* Remove a barra de rolagem */
        }

        /* Ajustar o conteúdo da página */
        .block-container {
            padding-top: 0;
            padding-bottom: 0;
            padding-left: 0;
            padding-right: 0;
            height: 100%;   
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        /* Ajustes para a sidebar */
        .sidebar .sidebar-content {
            width: 200px; /* Reduzindo a largura do sidebar */
        }

        /* Ajuste do layout principal */
        .main .block-container {
            padding-left: 220px;  /* Ajuste conforme necessário */
        }

        /* Remover a barra lateral */
        .css-1d391kg {
            display: none;  /* Esconde a barra lateral */
        }

    </style>
    """,
    unsafe_allow_html=True,
)



# Sidebar
st.sidebar.image('./ebac_icon.png', width=100)
st.sidebar.title('Análise Previsão de Renda')


st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            width: 300px;
        }
        .main .block-container {
            padding-left: 320px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Customizando o Sidebar
with st.sidebar:

    # Menu de seleção
    selected = option_menu(

        # Título
        'Menu',

        # Opções de Navegação
        ['Análise Univariada', 'Análise Bivariada','Análise Temporal'],
        # Icones para o menu das opções
        icons=['bar-chart-fill', 'bar-chart-fill', 'bar-chart-fill'],

        # icone do menu principal
        menu_icon='cast',

        # Seleção padrão
        default_index=0,

        # Estilos
        styles={
            'menu-title' : {'font-size' : '18px'}, # Diminui o tamanho da fonte do título
            'menu-icon': {'display': 'none'},  # Remove o ícone do título
            'icon': {'font-size': '12px'},  # Estilo dos ícones
            'nav-link': {
                'font-size': '15px',  # Tamanho da fonte dos itens do menu
                '--hover-color': '#6052d9',  # Cor de fundo ao passar o mouse
            },
            'nav-link-selected': {'background-color': '#157806'},  # Cor de fundo do item selecionado
        }

    )


# Navegação das Páginas

if selected == 'Análise Univariada':
    # Título da página
    st.markdown("<h1 style='font-size: 2em;'>Análise Univariada</h1>", unsafe_allow_html=True) 
    st.markdown('Contagem das Variáveis presentes em Nosso dataset')


    # Filtros para selecionar a variável
    var = [
        'posse_de_veiculo',
        'posse_de_imovel',
        'qtd_filhos',
        'idade',
        'tempo_emprego',
        'qt_pessoas_residencia',
        'sexo',
        'tipo_renda',
        'educacao',
        'estado_civil',
        'tipo_residencia'
    ]

    # Selectbox para o usuário escolher a variável
    coluna_selecionada = st.selectbox('Selecione a variável', var)

    # Chamando a função para renderizar o gráfico com a coluna selecionada
    gerar_grafico_univariada(df, coluna_selecionada)

 

elif selected == 'Análise Bivariada':
    # Título da página
    st.markdown("<h1 style='font-size: 2em;'>Análise Bivariada</h1>", unsafe_allow_html=True) 
    st.markdown('Distribuição da Renda de acordo com as demais Variáveis')

    # Filtros para escolher a variável
    var1 = [
        'data_ref',
        'posse_de_veiculo',
        'posse_de_imovel',
        'qtd_filhos',
        'idade',
        'qt_pessoas_residencia',
        'sexo',
        'tipo_renda',
        'educacao',
        'estado_civil',
        'tipo_residencia'
    ]

    var2 = ['renda']

    # Divisão caixas de seleção
    col1, col2 = st.columns(2)

    with col1:
        # Selectbox para o usuário escolher a variável
        coluna_selecionada = st.selectbox('Selecione a variável', var1)

    with col2:
        selecione_var2 = st.selectbox('Selecione a variável', var2)

    # Chamando a função para renderizar o gráfico com a coluna selecionada
    gerar_grafico_bivariada(df, coluna_selecionada)

   


elif selected == 'Análise Temporal':
    # Título da página
    st.markdown("<h1 style='font-size: 2em;'>Análise da Renda ao Longo do Tempo</h1>", unsafe_allow_html=True)


    # Filtros para selecionar as variáveis
    var3 = [
        'posse_de_veiculo',
        'posse_de_imovel',
        'qtd_filhos',
        'idade',
        'tempo_emprego',
        'qt_pessoas_residencia',
        'sexo',
        'tipo_renda',
        'educacao',
        'estado_civil',
        'tipo_residencia'
    ]

    # Selectbox para o usuário escolher a variável
    coluna_selecionada = st.selectbox('Selecione a variável', var3)

    # Chamando a função para renderizar o gráfico com a coluna selecionada
    gerar_grafico_temporal(df, coluna_selecionada)

    # rodapé 
    st.markdown(
        '''
            <hr style='border: 1px solid #d3d3d3;'/>
            <p style='text-align: center; color: gray;'>
            Dashboard de Previsão de Renda | Desenvolvido por Isabelle Fernanda da Silva | © 2025
            </p>
        ''',
        unsafe_allow_html=True)


else:
    pass



    