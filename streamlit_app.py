import openai
import streamlit as st

def assistant():
    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        
    st.title("Asesor de vestuario")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key

    prompt = "Como asesor de moda, debes sugerir combinaciones de ropa y accesorios en base a consultas específicas como '¿qué combina con un pantalón azul marino?'. Considera la ocasión, estación, comodidad, estilo personal y tendencias moda actuales. Ayuda al usuario a elegir outfits que sean atractivos, cómodos y seguros. Explica por qué ciertas elecciones son recomendables y cómo se alinean con las preferencias del usuario."
    
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

    user_input = st.text_area("Pregunte, p. ej., '¿Qué combina con un pantalón un pantalón verde?', o '¿Qué vestir para una fiesta de bodas?'", height=100)

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)

    if st.button("Consultar"):
        optimized_prompt = generate_optimized_prompt(prompt)
        st.session_state.messages.append({"role": "user", "content": optimized_prompt})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)

def generate_optimized_prompt(prompt):
    # Aquí puedes agregar tu lógica para generar el prompt optimizado
    optimized_prompt = prompt + " [Optimized]"
    return optimized_prompt

assistant()
