from langchain_tavily import TavilySearch

from config import settings

search = TavilySearch(tavily_api_key=settings.tavily_api_key)