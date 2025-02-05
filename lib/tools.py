# from langchain_core.tools import tool
# from langchain_community.tools import DuckDuckGoSearchRun
# from langchain_community.docstore.wikipedia import Wikipedia
# from langchain.agents.react.base import DocstoreExplorer
# from langchain_community.tools.pubmed.tool import PubmedQueryRun
# from langchain_community.tools import YahooFinanceNewsTool
from langchain_community.agent_toolkits.load_tools import load_tools
from dotenv import load_dotenv

load_dotenv()

# docstore = DocstoreExplorer(Wikipedia())
# search = DuckDuckGoSearchRun()
# pubmed = PubmedQueryRun()
# yahoo_finance = YahooFinanceNewsTool()


# @tool
# def search_wikipedia(query: str) -> str:
#     """Search Wikipedia for a query."""
#     return docstore.search(query)


# @tool
# def lookup_wikipedia(query: str) -> str:
#     """Lookup Wikipedia for a query."""
#     return docstore.lookup(query)


# @tool
# def pubmed_query(query: str) -> str:
#     """Search PubMed for a query."""
#     return pubmed.run(query)


tools = load_tools(
    [
        "ddg-search",
        "wikipedia",
        "wolfram-alpha",
        "merriam-webster",
        "pubmed",
        "stackexchange",
        "google-finance",
        "google-trends",
        # "google-scholar",
        "arxiv",
    ]
)
