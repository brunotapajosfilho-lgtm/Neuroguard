from typing import Literal

import streamlit as st

st.set_page_config(page_title="NeuroGuard", page_icon="🧠", layout="centered")

st.title("🧠 NEUROGUARD")
st.caption("Sistema Inteligente para Análise de Biomarcadores")

id_amostra = st.text_input("Nome completo", placeholder="Nome completo")
gmail = st.text_input("Gmail", placeholder="Neuroguard@gmail.com")
cell = st.text_input("Celular", placeholder="(92) 99999-9999")
idade = st.number_input("Idade", 0, 120, 30)
sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])

biomarcador = st.radio("Biomarcador", ["LDH", "ALP"])

if biomarcador == "LDH":
    valor = st.number_input("Valor do LDH (U/L)", value=320.0)
else:
    valor = st.number_input("Valor da ALP (U/L)", value=95.0)

st.write('')

st.write('')

st.write('')

st.subheader("Questionário de hábitos:")
st.caption("Responda as perguntas:")

st.write('')

fuma = st.radio("1) Você tem o costume de fumar?", ["Sim", "Não"])

sang = st.radio("2) Você já teve sangramento gengival?", ["Sim", "Não"])

conh = st.radio("3) Você já foi diagnosticado com doenças periodontais?", [
                "Sim", "Não"])

fiod = st.radio("4) Você costuma usar fio dental no cotidiano?", [
                "Sim", "Não"])

sens = st.radio("5) Você sente sensibilidade na gengiva?", ['Sim', "Não"])

dent = st.radio("6) Quantas vezes você costuma ir para o dentista no ano?", [
                "Nenhuma", "1-2", "3+"])

esco = st.radio("7) Quantas vezes você costuma escovar o dente no dia?", [
                "Nenhuma", "1", "2", "3+"])

mole = st.radio("8) Algum dente seu apresenta mobilidade?",
                ["Não", "1", "2+", ])

hali = st.radio("9) Você sente mal hálito com frequencia?", [
                "Não", "Às vezes", "Frequentemente", "Sempre"])

sens = st.radio("10) Você percebe acúmulo de tártaro com frequência?", [
                'Não', "Pouco", "Moderado", "Muito"])

qualidade = 0
if fuma == "Sim":
    qualidade = qualidade + 2
if sang == "Sim":
    qualidade = qualidade + 2
if conh == "Sim":
    qualidade = qualidade + 3
if fiod == "Não":
    qualidade = qualidade + 1
if sens == "Sim":
    qualidade = qualidade + 2
if dent == "Nenhuma":
    qualidade = qualidade + 3
if dent == "1-2":
    qualidade = qualidade + 2
if esco == "Nenhuma":
    qualidade = qualidade + 4
if esco == "1":
    qualidade = qualidade + 3
if esco == "2":
    qualidade = qualidade + 2
if mole == "+2":
    qualidade = qualidade + 3
if mole == "1":
    qualidade = qualidade + 2
if hali == "Sempre":
    qualidade = qualidade + 3
if hali == "Frequentemente":
    qualidade = qualidade + 2
if sens == "Muito":
    qualidade = qualidade + 3
if sens == "Moderado":
    qualidade = qualidade + 2

observacoes = st.text_area("Observações")

imagem = st.file_uploader("Imagem da Amostra", type=["png", "jpg", "jpeg"])

if imagem:
    st.image(imagem, use_container_width=True)

if st.button("🔬 Analisar Amostra", use_container_width=True):
    if biomarcador == "LDH":
        if valor <= 280:
            interpretacao = 'Dentro da faixa de referência.'
            periodontal, neuro = 18, 10
        elif valor <= 330:
            interpretacao = 'Levemente elevado.'
            periodontal, neuro = 45, 28
        elif valor <= 400:
            interpretacao = 'Elevado.'
            periodontal, neuro = 72, 41
        else:
            interpretacao = 'Muito elevado.'
            periodontal, neuro = 91, 76
    else:
        if valor <= 120:
            interpretacao = 'Dentro da faixa de referência.'
            periodontal, neuro = 15, 9
        elif valor <= 160:
            interpretacao = 'Levemente elevado.'
            periodontal, neuro = 42, 24
        elif valor <= 220:
            interpretacao = 'Elevado.'
            periodontal, neuro = 67, 38
        else:
            interpretacao = 'Muito elevado.'
            periodontal, neuro = 88, 71

    st.header("Resultado da Análise")
    st.write(f"**ID da Amostra:** {id_amostra}")
    st.write(f"**Gmail:** {gmail}")
    st.write(f"**Celular:** {cell}")
    st.write(f"**Idade:** {idade} anos")
    st.write(f"**Sexo:** {sexo}")
    st.write(f"**{biomarcador}:** {valor} U/L")
    st.write(f"**Interpretação:** {interpretacao}")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Índice de Doenças Periodontais")
        st.progress(periodontal/100)
        st.metric("Probabilidade", f"{periodontal}%")
        try:
            st.image("assets/boca.png", use_container_width=True)
        except:
            st.info("Adicione assets/boca.png")

    with col2:
        st.subheader("Índice de Risco Neurodegenerativo")
        st.progress(neuro/100)
        st.metric("Probabilidade", f"{neuro}%")
        try:
            st.image("assets/cabeca.png", use_container_width=True)
        except:
            st.info("Adicione assets/cabeca.png")
    st.divider()

    st.subheader("Qualidade dos Hábitos")
    st.write(
        f"A qualidade dos seus hábitos de higiene bucal são {qualidade} porcento de qualidade!")

    st.write('')
    st.write('')
    st.write('')

    st.subheader("Principais Áreas Cerebrais Relacionadas")
    try:
        st.image("assets/cerebro.png", use_container_width=True)
    except:
        st.info("Adicione assets/cerebro.png")

    st.subheader("Observações")
    st.info("Protótipo para demonstração. Os resultados são simulados.")
