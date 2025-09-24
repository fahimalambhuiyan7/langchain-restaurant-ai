import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain import LLMChain
from langchain.chains import SequentialChain

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.6,
    google_api_key=GOOGLE_API_KEY
)
print("Key from env:", os.getenv("GOOGLE_API_KEY"))

def generate_resturant(cuisine):
    prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = "I want to open a resturant for {cuisine} food . Suggest one random fancy name for the resturant."
    )
    name_chain = LLMChain(llm=llm,prompt=prompt_template_name,output_key="resturant_names")

    prompt_template_items = PromptTemplate(
        input_variables = ['resturant_names'],
        template = "Provide Some Menu Items For {resturant_names} provide it as comma seperated values"
    )
    food_item_chain = LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu_items")
    
    
    chain  = SequentialChain(
    chains = [name_chain,food_item_chain],
    input_variables = ['cuisine'],
    output_variables = ["resturant_names","menu_items"]
    )
    
    response = chain({'cuisine':cuisine})
    
    return response


