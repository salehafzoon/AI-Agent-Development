from duckduckgo_search import DDGS

def search_duckduckgo(query, max_results=5):
    """
    Performs a DuckDuckGo search and returns structured results.
    """
    results = DDGS().text(query, max_results=max_results)
    return [{"title": r["title"], "link": r["href"], "snippet": r.get("body", "")} for r in results]

# Test the function
if __name__ == "__main__":
    search_results = search_duckduckgo("LangChain")
    for idx, result in enumerate(search_results, 1):
        print(f"{idx}: {result['title']} - {result['link']}\n{result['snippet']}\n")
