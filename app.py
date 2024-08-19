import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from config import OPENAI_API_KEY

# Initialize the OpenAI model
llm = OpenAI(api_key=OPENAI_API_KEY)

# Define the prompt template for translation
prompt_template = PromptTemplate(
    input_variables=["text", "language"],
    template="Translate the following text to {language}: {text}",
)

# Create a chain using the prompt and LLM
translation_chain = LLMChain(llm=llm, prompt=prompt_template)

# Streamlit app
st.title("Language Translation Web App")
st.write("Enter text in the source language and select the target language for translation.")

# Text input from the user
source_text = st.text_area("Source Text", "Type your text here...")

# Target language selection
target_language = st.selectbox(
    "Select Target Language",
    ("Spanish", "French", "German", "Chinese", "Japanese", "Korean")
)

# Translate button
if st.button("Translate"):
    if source_text.strip() == "":
        st.error("Please enter some text to translate.")
    else:
        # Perform the translation using the LLMChain
        translation = translation_chain.run({"text": source_text, "language": target_language})

        # Display the translation
        st.success("Translation:")
        st.write(translation)

st.write("Powered by LangChain and OpenAI")
