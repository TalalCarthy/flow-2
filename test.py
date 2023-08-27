from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI()
res = llm.predict("Hello, world!")

print(res)

# ls__dd77a45f176d4f479b3d1b67266e78dd
# set LANGCHAIN_API_KEY="ls__dd77a45f176d4f479b3d1b67266e78dd"

# set LANGCHAIN_TRACING_V2=true
# set LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
# set LANGCHAIN_API_KEY="ls__dd77a45f176d4f479b3d1b67266e78dd"
# set LANGCHAIN_PROJECT="chat-over-docs-flow"
