from langchain_community.tools import DuckDuckGoSearchRun
from serpapi import GoogleSearch


from langchain_core.tools import Tool

from datetime import datetime 
import requests

from bs4 import BeautifulSoup 
import re

def google_search(query):
    params = {
        "q": query,
        "openai_api_key":"OPENAI_API_KEY",
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Extract links
    links = []
    for result in results.get("organic_results", []):
        links.append(result.get("link"))

    return links

def save_to_txt(data : str, filename : str = "leads_output.txt" ):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Leads Output---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open (filename, "a", encoding= "utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"

# Scrape raw text from a website
def scrape_website(url: str) -> str:
    try:
        # Send GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad HTTP codes

        # Parse and clean up the raw HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
        text = re.sub(r'\s+', ' ', text)  # Normalize whitespace

        # Limit to 5000 characters for performance and API limits
        return text[:2000]
    except Exception as e:
        return f"Error scraping website: {e}"

def generate_queries():
    return [
        "small IT companies in Noida contact details",
        "IT service providers in Gurgaon India",
        "software companies in Delhi NCR website",
        "managed IT services Noida small business",
    ]
# Generate search queries to look for IT services related to a company
def generate_search_queries(company_name: str) -> list[str]:
    keywords = ["IT Services", "managed IT", "technology solutions"]
    return [f"{company_name} {keyword}" for keyword in keywords]

# Combined search and scrape operation for a company
def search_and_scrape(company_name: str) -> str:
    queries = generate_search_queries(company_name)
    results = []

    for query in queries:
        links = google_search(query)

        for link in links[:2]:   # limit for safety
            data = scrape_website(link)
            results.append(data)

    return " ".join(results)

def extract_emails(text):
    return re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)



# DuckDuckGo search tool
search = DuckDuckGoSearchRun()

# Defining all the tools that we created above

search_tool = Tool(
    name="google_search",
    func=google_search,
    description="Search Google for Indian companies and websites"
)

scrape_tool = Tool(
    name="scrape_website",
    func=search_and_scrape,
    description="Scrape website content and gather business insights",
)

save_tool = Tool(
    name="save_to_txt",
    func=save_to_txt,
    description="Save structured lead data into a text file",
)
