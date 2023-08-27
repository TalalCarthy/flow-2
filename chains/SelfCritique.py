# Imports
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.constitutional_ai.base import ConstitutionalChain
from langchain.chains.constitutional_ai.models import ConstitutionalPrinciple

os.environ['OPENAI_API_KEY'] = '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'


qa_prompt = PromptTemplate(
    template="""You are a very helpful assistant and must answer questions.
Context: {context}
Question: {question}

Helpful answer:""",
    input_variables=["question", 'context'],
)

llm = OpenAI(temperature=0)

qa_chain = LLMChain(llm=llm, prompt=qa_prompt)

quality_principle = ConstitutionalPrinciple(
    name="Quality Principle",
    critique_request="The model should only return answers from/related to the given context.",
    revision_request="Rewrite the model's output to utilize the context and return high quality answers from the given context.",
)


# principles = ConstitutionalChain.get_principles(["illegal"])
principles = [quality_principle]
constitutional_chain = ConstitutionalChain.from_llm(
    chain=qa_chain,
    constitutional_principles=principles,
    llm=llm,
    verbose=True,
)

context = """
    The New Social Contract for the next 75 years of Israel 

V6 

23.6.2023 

 

Executive Summary  

Mazal tov to the State of Israel for reaching its 75th anniversary! The nagging question is 

what is the likelihood that our grandchildren will be able to congratulate the country on its 

next 75th milestone? This document argues that under the “business as usual” scenario within 

the current political system there is a non-trivial probability that Israel may cease to exist as a 

Jewish country well before its next 75th anniversary. We offer a structural change in the 

Israeli political system that may actually make such a future birthday party possible.  


"""

response = constitutional_chain.run(
    question="What is the context about??", context=context)

print(response)