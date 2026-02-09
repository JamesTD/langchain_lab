from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#https://huggingface.co/stepfun-ai/Step-3.5-Flash
#https://openrouter.ai/settings/keys?utm_source=signup-success

def llm_model(prompt_txt, params=None):

    default_params = {
        "max_tokens": 256,
        "temperature": 0.5,
    }

    if params:
        default_params.update(params)

    llm = ChatOpenAI(
        model="stepfun/step-3.5-flash:free",
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key="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",
        temperature=default_params["temperature"],
        max_tokens=default_params["max_tokens"],
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a pirate."),
        ("human", "{input}")
    ])

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"input": prompt_txt})
    return response
    

response = llm_model("Where is your buried treasure?")
print(response)

