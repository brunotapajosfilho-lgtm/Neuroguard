from typing import Literal

import streamlit as st
import math
import streamlit.components.v1 as components 

st.set_page_config(page_title="NeuroGuard", page_icon="🧠", layout="centered")

try:
    st.image("assets/banner.png", use_container_width=True)
except:
    st.info("Adicione assets/banner.png")

st.title("🧠 NEUROGUARD")
st.caption("Sistema Inteligente para Análise de Biomarcadores")

id_amostra = st.text_input("Nome completo", placeholder="Nome completo")
gmail = st.text_input("Gmail", placeholder="Neuroguard@gmail.com")
cell = st.text_input("Celular", placeholder="(92) 99999-9999")
idade = st.number_input("Idade", 0, 120, 30)
sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])

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
pont_max = 26

indice_bucal = round((qualidade / pont_max) * 100)
indice_bucal = min(indice_bucal, 100)

observacoes = st.text_area("Observações")

st.write("")
st.divider()

st.subheader("Pesquisa de Biomarcadores")

biomarcador = st.radio("Biomarcador", ["LDH", "ALP"])

if biomarcador == "LDH":
    valor = st.number_input("Valor do LDH (U/L)", value=320.0)
else:
    valor = st.number_input("Valor da ALP (U/L)", value=95.0)


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

    pato = int(indice_bucal)
    periodontal = (((pato * 1.234) * 0.3) + (periodontal * 0.7))
    neuro = (((pato * 1.234) * 0.3) + (neuro * 0.7))
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Índice de Doenças Periodontais")
        st.progress(periodontal/100)
        st.metric("Probabilidade", f"{periodontal:.0f}%")
        try:
            st.image("assets/boca.png", use_container_width=True)
        except:
            st.info("Adicione assets/boca.png")

    with col2:
        st.subheader("Índice de Risco Neurodegenerativo")
        st.progress(neuro/100)
        st.metric("Probabilidade", f"{neuro:.0f}%")
        try:
            st.image("assets/cabeca.png", use_container_width=True)
        except:
            st.info("Adicione assets/cabeca.png")
    st.divider()


    rebec = ((81 - float(pato)) / 81) * 100
    rebec = max(0, min(100, rebec))

    raio = 90
    circ = 2 * math.pi * raio
    offset = circ * (1 - rebec / 100)

    components.html(f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>

    body {{
        margin:0;
        background:transparent;
        display:flex;
        justify-content:center;
        align-items:center;
        font-family:Arial, Helvetica, sans-serif;
    }}

    .container {{
        text-align:center;
    }}

    h2 {{
        color:white;
        margin-bottom:20px;
        font-size:32px;
    }}

    .porcentagem {{
        font-size:46px;
        font-weight:bold;
        fill:white;
    }}

    .sub {{
        font-size:18px;
        fill:#B388FF;
    }}

    </style>
    </head>

    <body>

    <div class="container">

    <h2>Relatório de Hábitos Bucais</h2>

    <svg width="240" height="240">

        <!-- Fundo -->
        <circle
            cx="120"
            cy="120"
            r="{raio}"
            stroke="#2D2D3A"
            stroke-width="16"
            fill="none"
        />

        <!-- Progresso -->
        <circle
            cx="120"
            cy="120"
            r="{raio}"
            stroke="#8B5CF6"
            stroke-width="16"
            fill="none"
            stroke-linecap="round"
            stroke-dasharray="{circ}"
            stroke-dashoffset="{offset}"
            transform="rotate(-90 120 120)"
            style="
                transition:stroke-dashoffset .8s ease;
            "
        />

        <text
            x="120"
            y="128"
            text-anchor="middle"
            class="porcentagem">
            {rebec:.0f}%
        </text>

    </svg>

    </div>

    </body>
    </html>
    """, height=320)

    if indice_bucal <= 20:

        st.success("🟢 Excelente Saúde Bucal")

        st.markdown("#### Possíveis hábitos identificados")

        st.write("• Excelente rotina de higiene bucal.")
        st.write("• Escovação frequente e eficiente.")
        st.write("• Uso regular do fio dental.")
        st.write("• Consultas odontológicas preventivas.")
        st.write("• Baixa probabilidade de inflamação gengival.")

        st.write("")

        st.markdown("#### Recomendações")

        st.write("• Continue mantendo os hábitos atuais.")
        st.write("• Realize consultas preventivas a cada seis meses.")
        st.write("• Mantenha a higiene bucal completa.")
        st.write("• Continue evitando fatores de risco, como o tabagismo.")

    elif indice_bucal <= 40:

        st.info("🟡 Boa Saúde Bucal")

        st.markdown("#### Possíveis hábitos identificados")

        st.write("• Higiene bucal geralmente adequada.")
        st.write("• Pequenas falhas podem ocorrer na rotina de limpeza.")
        st.write("• Possível acúmulo discreto de placa bacteriana.")

        st.write("")

        st.markdown("#### Recomendações")

        st.write("• Intensifique o uso diário do fio dental.")
        st.write("• Mantenha a escovação após as principais refeições.")
        st.write("• Realize acompanhamento odontológico preventivo.")
        st.write("• Reduza o consumo frequente de açúcar.")

    elif indice_bucal <= 60:

        st.warning("🟠 Saúde Bucal Moderada")

        st.markdown("#### Possíveis hábitos identificados")

        st.write("• Escovação insuficiente ou irregular.")
        st.write("• Uso pouco frequente do fio dental.")
        st.write("• Possíveis sinais iniciais de gengivite.")
        st.write("• Acúmulo moderado de placa bacteriana.")

        st.write("")

        st.markdown("#### Recomendações")

        st.write("• Melhorar a rotina diária de higiene bucal.")
        st.write("• Utilizar fio dental diariamente.")
        st.write("• Agendar uma avaliação odontológica.")
        st.write("• Realizar limpeza profissional quando indicada.")

    elif indice_bucal <= 80:

        st.warning("🔴 Saúde Bucal Ruim")

        st.markdown("#### Possíveis hábitos identificados")

        st.write("• Baixa frequência de escovação.")
        st.write("• Sangramento gengival recorrente.")
        st.write("• Acúmulo importante de placa bacteriana.")
        st.write("• Elevado risco para doenças periodontais.")

        st.write("")

        st.markdown("#### Recomendações")

        st.write("• Procurar atendimento odontológico o quanto antes.")
        st.write("• Corrigir imediatamente os hábitos de higiene.")
        st.write("• Realizar tratamento periodontal, caso necessário.")
        st.write("• Evitar fatores agravantes, como o tabagismo.")

    else:

        st.error("🔴 Condição Bucal Crítica")

        st.markdown("#### Possíveis hábitos identificados")

        st.write("• Alto risco para doença periodontal.")
        st.write("• Múltiplos fatores de risco presentes.")
        st.write("• Possível comprometimento dos tecidos de suporte dos dentes.")
        st.write("• Hábitos de higiene insuficientes.")

        st.write("")

        st.markdown("#### Recomendações")

        st.write("• Procurar avaliação odontológica especializada com urgência.")
        st.write("• Iniciar tratamento periodontal conforme orientação profissional.")
        st.write("• Reestruturar completamente a rotina de higiene bucal.")
        st.write("• Manter acompanhamento clínico periódico.")
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
# python -m streamlit run neuroguard.py
