import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Produtos",
    layout="wide"
)

st.title("Dashboard de Análise de Produtos")

arquivo = st.file_uploader("Envie um arquivo CSV", type="csv")

if arquivo:

    dados = pd.read_csv(arquivo)
    dados["produto"] = dados["produto"].str.strip()

    st.sidebar.header("Filtros")

    produto = st.sidebar.selectbox(
        "Escolha um produto",
        ["Todos"] + list(dados["produto"].unique())
    )

    if produto != "Todos":
        dados = dados[dados["produto"] == produto]

    total_registros = len(dados)
    total_quantidade = dados["quantidade"].sum()
    media_quantidade = dados["quantidade"].mean()
    produto_top = dados.groupby("produto")["quantidade"].sum().idxmax()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Registros", total_registros)
    col2.metric("Quantidade total", total_quantidade)
    col3.metric("Média", round(media_quantidade, 2))
    col4.metric("Produto mais vendido", produto_top)

    st.divider()

    st.subheader("Dados")
    st.dataframe(dados, use_container_width=True)

    st.divider()

    resumo = dados.groupby("produto")["quantidade"].sum().reset_index()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Quantidade por Produto")

        fig_bar = px.bar(
            resumo,
            x="produto",
            y="quantidade",
            color="produto",
            text="quantidade",
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig_bar.update_traces(textposition="outside")

        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:

        st.subheader("🥧 Distribuição dos Produtos")

        fig_pie = px.pie(
            resumo,
            names="produto",
            values="quantidade",
            color="produto",
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        st.plotly_chart(fig_pie, use_container_width=True)

    st.divider()

    st.subheader("Evolução das Quantidades")

    fig_line = px.line(
        dados,
        x=dados.index,
        y="quantidade",
        markers=True
    )

    st.plotly_chart(fig_line, use_container_width=True)

    st.divider()

    st.subheader("Ranking de Produtos")

    ranking = resumo.sort_values("quantidade", ascending=False)

    st.dataframe(ranking, use_container_width=True)

    csv = dados.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Baixar dados filtrados",
        csv,
        "dados_filtrados.csv",
        "text/csv"
    )