import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# ==================== CONFIGURACIÓN MQTT ==================== #
def on_publish(client, userdata, result):
    print("✨ Señal transmitida al cosmos...\n")

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.toast(f"🛰️ Mensaje recibido: {message_received}", icon="💫")

broker = "157.230.214.127"
port = 1883
client1 = paho.Client("GIT-HUB")
client1.on_message = on_message


# ==================== ESTILO GALÁCTICO ==================== #
galaxy_css = """
<style>
/* Fondo galáctico animado */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 20% 30%, #0b002d, #000010 80%);
    color: white;
    position: relative;
    overflow: hidden;
}
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: -100px;
    left: -100px;
    width: 300%;
    height: 300%;
    background: url('https://cdn.pixabay.com/photo/2016/11/18/22/23/star-1837306_1280.png') repeat;
    background-size: 700px 700px;
    opacity: 0.25;
    animation: moveStars 180s linear infinite;
    z-index: 0;
}
@keyframes moveStars {
    from { transform: translateY(0px); }
    to { transform: translateY(-900px); }
}

/* Títulos y textos */
h1, h2, h3, h4, label, p, span {
    color: #d9b3ff !important;
    text-shadow: 0 0 8px rgba(180, 120, 255, 0.7);
    position: relative;
    z-index: 2;
}

/* Botones con efecto holográfico */
.stButton>button {
    background: linear-gradient(135deg, rgba(100,0,255,0.8), rgba(200,100,255,0.9));
    border: 2px solid rgba(200,180,255,0.4);
    border-radius: 20px;
    color: #fff;
    font-weight: 700;
    padding: 0.8em 2em;
    text-shadow: 0px 0px 8px rgba(255,255,255,0.8);
    box-shadow: 0 0 25px rgba(140,80,255,0.7);
    transition: all 0.3s ease;
    z-index: 2;
}
.stButton>button:hover {
    transform: scale(1.08) rotate(-1deg);
    background: linear-gradient(135deg, rgba(200,100,255,1), rgba(100,0,255,0.9));
    box-shadow: 0 0 35px rgba(190,120,255,1);
}

/* Slider (barra de energía) */
.stSlider>div>div>div>div {
    background: linear-gradient(90deg, #9b5cff, #4e00b8);
    height: 10px;
    border-radius: 10px;
}

/* Caja lateral */
[data-testid="stSidebar"] {
    background: rgba(10, 0, 40, 0.7);
    backdrop-filter: blur(10px);
    border-right: 2px solid rgba(180,100,255,0.3);
    box-shadow: 0 0 20px rgba(120,80,255,0.3);
    color: white;
}
</style>
"""
st.markdown(galaxy_css, unsafe_allow_html=True)

# ==================== INTERFAZ GALÁCTICA ==================== #
st.title("🚀 Panel de Control Galáctico MQTT")
st.subheader("🪐 Transmisión de energía a módulos espaciales")
st.caption(f"Versión de Python: {platform.python_version()}")

st.markdown("---")
st.markdown("### ⚙️ Módulos principales de energía")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌟 Encender Núcleo"):
        act1 = "ON"
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        client1.publish("cmqtt_s", message)
        st.success("⚡ Núcleo activado. Energía fluyendo al sistema estelar.")

with col2:
    if st.button("🌑 Apagar Núcleo"):
        act1 = "OFF"
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        client1.publish("cmqtt_s", message)
        st.warning("🔕 Núcleo en reposo. Flujos suspendidos.")

with col3:
    if st.button("💫 Reiniciar Sistema"):
        st.toast("Reiniciando protocolo cósmico...", icon="🌀")
        time.sleep(1.5)
        st.balloons()
        st.success("🪩 Sistema galáctico reiniciado con éxito.")

st.markdown("---")
st.markdown("### 🌠 Ajuste de Potencia de Transmisión")
values = st.slider("Nivel de energía cuántica", 0.0, 100.0, 42.0)
st.write(f"🔋 Energía configurada al **{values}%** del máximo estelar.")

if st.button("🚀 Transmitir señal"):
    client1 = paho.Client("GIT-HUB")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Analog": float(values)})
    client1.publish("cmqtt_a", message)
    st.snow()
    st.success("🌌 Señal cuántica enviada a la red interplanetaria.")

st.markdown("---")

# ==================== PANEL LATERAL ==================== #
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/57/StarfieldSimulation.gif", use_container_width=True)
    st.markdown("### 🛰️ Estado del Sistema Galáctico")
    st.metric(label="Energía actual", value=f"{values} %", delta="estable")
    st.metric(label="Conexión MQTT", value="🟢 Activa")
    st.metric(label="Canal de control", value="cmqtt_s")
    st.markdown("---")
    st.write("✨ Panel desarrollado por **CataTech Galactic Labs™**")
    st.caption("Interfaz holográfica impulsada por la energía de las estrellas 🌠")
