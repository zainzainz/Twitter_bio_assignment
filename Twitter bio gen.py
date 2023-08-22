from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv("KEYS.env")
import os
os.environ['OPENAI_API_KEY'] = os.getenv("api_key")

llm = OpenAI(temperature = 1)

pname = PromptTemplate(
    input_variables = ['bio'],
    template = "Give me a Twitter bio about {bio}, make it fun, doesn't containg hashtags, and 160 characters or less"
)
prompt = input("Enter bio topic/s: ")
chain = LLMChain(llm = llm,prompt = pname)
print(chain.run(prompt))