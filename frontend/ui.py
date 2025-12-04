import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from config.config import DB_CONFIG
from utils.helpers import init_database
from chains.response_chain import get_response

def render_chat_ui():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello! I'm a SQL assistant. Ask me anything about your database."),
        ]

    st.set_page_config(page_title='Chat with MySQL', page_icon=':speech_balloon:')
    st.title('Chat with your Database')

    with st.sidebar:
        st.text_input("Host", value=DB_CONFIG["host"], key="Host")
        st.text_input("Port", value=DB_CONFIG["port"], key="Port")
        st.text_input("User", value=DB_CONFIG["user"], key="User")
        st.text_input("Password", type="password", value=DB_CONFIG["password"], key="Password")
        st.text_input("Database", value=DB_CONFIG["database"], key="Database")

        if st.button("Connect"):
            with st.spinner("Connecting to database..."):
                db = init_database(
                    st.session_state["User"],
                    st.session_state["Password"],
                    st.session_state["Host"],
                    st.session_state["Port"],
                    st.session_state["Database"]
                )
                st.session_state.db = db
                st.success("Connected to database!")

    for message in st.session_state.chat_history:
        with st.chat_message("AI" if isinstance(message, AIMessage) else "Human"):
            st.markdown(message.content)

    user_query = st.chat_input("Type a message...")
    if user_query and user_query.strip() != "":
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        with st.chat_message("Human"):
            st.markdown(user_query)

        with st.chat_message("AI"):
            response = get_response(user_query, st.session_state.db, st.session_state.chat_history)
            st.markdown(response)
            st.session_state.chat_history.append(AIMessage(content=response))
