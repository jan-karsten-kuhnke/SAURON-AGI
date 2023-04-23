import streamlit as st

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from dotenv import find_dotenv, load_dotenv

llm = OpenAI(temperature=0)
tools = load_tools(["wikipedia"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

st.set_page_config(
    page_title="Wikipedia Langchain Bot",
    page_icon="👋",
)
st.subheader("Willkommen bei Haddocks :wave:")
st.title('Wikipedia Langchain KI Assistent 🦜 ')
st.write(
        "Durchforste Wikipedia mithilfe der KI von HADDOCK."
    )
st.write("[Sie möchten ein eigenes KI Projekt mit uns umsetzten? Kontaktieren Sie uns jetzt! >](https://pythonandvba.com)")


# Eingabebereich
st.header("Was möchtest du wissen?")
input = st.text_input("")

# Sidebar
st.sidebar.header("Langchain KI Assistent")
st.sidebar.success("Geben Sie Ihre Frage im Hauptbereich ein.")

# Ergebnisbereich
if input:
    st.header("Ergebnis:")
    text = agent.run(input)
    st.write(text)


 #st.text_area(text)
 
st.header("What I do")
st.write("##")
 
st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
 
st.write("---")
st.header("Get In Touch With Me!")
st.write("##")

 
 
contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Vor, Nachname" required>
        <input type="email" name="email" placeholder="Ihre Emailadresse hier...>
        <input type="firma name="firma" placeholder="In welcher Firma arbeiten Sie?" name="firma" placeholder="Ihre Emailadresse hier...>
        <input type="email" name="telefon" placeholder="Ihre Telefonnummer hier!>
        <textarea name="message" placeholder="Ihre Nachricht an uns" required></textarea>
        <button type="submit">Senden</button>
    </form>
    """
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
   
       
 
 
 
