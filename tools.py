from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()

#search - готовый тулл поэтому @tool не нужен
search = TavilySearchResults(
    max_results = 3
)

