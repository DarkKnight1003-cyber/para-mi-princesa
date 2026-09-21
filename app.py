import streamlit as st

st.set_page_config(page_title="Para mi princesa", page_icon="🌻", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #FFF0F5 0%, #F8C8DC 100%);
    }
    header[data-testid="stHeader"] {
        background: transparent;
    }
    .stApp h1, .stApp h2 {
        text-align: center;
        color: #9B3D62;
        animation: aparecer 2s;
    }
    .sobre {
        text-align: center;
        font-size: 150px;
        margin-top: 60px;
    }
    .aviso {
        text-align: center;
        color: #9B3D62;
        font-size: 24px;
        margin-bottom: 20px;
    }
    .jardin {
        display: flex;
        justify-content: center;
        align-items: flex-end;
        gap: 10px;
        margin-top: 20px;
    }
    .planta {
        transform-origin: bottom center;
        animation: balanceo 4s ease-in-out infinite;
    }
    .corazon-fondo {
        position: fixed;
        opacity: 0.3;
        filter: blur(2px);
        pointer-events: none;
        animation: flotar 6s ease-in-out infinite;
    }
    @keyframes aparecer {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes balanceo {
        0%, 100% { transform: rotate(-3deg); }
        50% { transform: rotate(3deg); }
    }
    @keyframes flotar {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def dibujar_flor(ancho, retraso):
    petalos = ""
    for i in range(12):
        petalos += f'<ellipse cx="0" cy="-45" rx="13" ry="32" fill="#FFD43B" stroke="#F5B700" stroke-width="2" transform="rotate({i * 30})"/>'

    tallo = '<rect x="95" y="100" width="10" height="260" rx="5" fill="#43A047"/>'
    hoja_izq = '<ellipse cx="65" cy="265" rx="40" ry="15" fill="#66BB6A" transform="rotate(40 65 265)"/>'
    hoja_der = '<ellipse cx="135" cy="210" rx="40" ry="15" fill="#66BB6A" transform="rotate(-40 135 210)"/>'
    cabeza = f'<g transform="translate(100,100)">{petalos}</g><circle cx="100" cy="100" r="22" fill="#8B5A2B"/>'

    return f'<div class="planta" style="animation-delay:{retraso}s;"><svg viewBox="0 0 200 360" style="width:{ancho};">{tallo}{hoja_izq}{hoja_der}{cabeza}</svg></div>'


def dibujar_corazon(tamano, lado, distancia, arriba, color, retraso):
    forma = "M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"
    return f'<div class="corazon-fondo" style="{lado}:{distancia}%; top:{arriba}%; animation-delay:{retraso}s;"><svg viewBox="0 0 24 24" width="{tamano}" height="{tamano}"><path d="{forma}" fill="{color}"/></svg></div>'


if "abierta" not in st.session_state:
    st.session_state.abierta = False

if not st.session_state.abierta:
    st.markdown('<div class="sobre">💌</div>', unsafe_allow_html=True)
    st.markdown('<div class="aviso">Tienes una carta para ti</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("Abrir carta", use_container_width=True):
            st.session_state.abierta = True
            st.rerun()
else:
    st.title("Mi novia nunca será espectadora")
    st.header("😍Feliz día mi princesa😍")
    st.header("💙Te amo demasiado💙")

    jardin = ""
    jardin += dibujar_flor("min(12vw, 120px)", -1)
    jardin += dibujar_flor("min(18vw, 170px)", -2)
    jardin += dibujar_flor("min(26vw, 240px)", 0)
    jardin += dibujar_flor("min(18vw, 170px)", -3)
    jardin += dibujar_flor("min(12vw, 120px)", -1.5)
    st.markdown(f'<div class="jardin">{jardin}</div>', unsafe_allow_html=True)

    corazones = ""
    corazones += dibujar_corazon(220, "left", 3, 12, "#E75480", 0)
    corazones += dibujar_corazon(140, "left", 10, 55, "#F06292", -2)
    corazones += dibujar_corazon(100, "left", 2, 78, "#E75480", -4)
    corazones += dibujar_corazon(200, "right", 4, 20, "#F06292", -1)
    corazones += dibujar_corazon(260, "right", 2, 55, "#E75480", -3)
    corazones += dibujar_corazon(120, "right", 12, 8, "#F06292", -5)
    st.markdown(corazones, unsafe_allow_html=True)