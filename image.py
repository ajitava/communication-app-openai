"""
This module performs grammatical correction on image files. 
It currently supports png and jpeg formats.
"""

#Import libraries
import os
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import pytesseract
from langchain_openai import OpenAI

#Set the pytesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def user_input(image):

    """Takes user input as image and highlights grammatical errors and displays corrected text"""

    #Get OPENAI_API_KEY
    key = os.getenv("OPENAI_API_KEY")

    #Define the LLM
    llm = OpenAI(model="gpt-3.5-turbo-instruct", api_key=key)

    #Create the prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a english grammar specialist to check if there are any grammatical errors in the text generated by the image provided by the user. You have to display the original text generated by the image and highlight the grammatical errors in the original text and finally correct the grammatical errors and show the correct text. The highlighted errors should display the grammatical errors"),
        ("user", "{input}")
    ])

    #Parse the output
    output_parser = StrOutputParser()

    #Convert image to string
    image_text = pytesseract.image_to_string(image)

    #Creating lang chain
    chain = prompt | llm | output_parser

    #Calling invoke with a single input
    return chain.invoke({"input": image_text})
