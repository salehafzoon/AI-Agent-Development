import os
import json
import boto3
from dotenv import load_dotenv
import sys

# Get the root directory of your project
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)

from tools.duckduckgo import search_duckduckgo

# Load environment variables from .env
load_dotenv()

# Retrieve AWS credentials
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "ap-southeast-2")  # Sydney Region

# Initialize AWS Bedrock client
bedrock_client = boto3.client(
    "bedrock-runtime",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Load prompt template from file
PROMPT_FILE = os.path.join(root_dir, "prompt/search_prompt.txt")

def load_prompt_template():
    """Loads the search prompt template from a file."""
    try:
        with open(PROMPT_FILE, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return """You are an AI assistant that summarizes search results concisely.
                  Given the following search results for the query '{query}', generate a brief and informative summary.

                  {search_text}

                  Summary:
               """

def call_titan(prompt, model_id="amazon.titan-text-express-v1"):
    try:
        response = bedrock_client.invoke_model(
            modelId=model_id,
            body=json.dumps({
                "inputText": prompt,  
                "textGenerationConfig": {
                    "maxTokenCount": 300,
                    "temperature": 0.7,  
                    "topP": 0.9          
                }
            }),
            contentType="application/json"
        )
        response_body = json.loads(response["body"].read())
        return response_body.get("results", [{}])[0].get("outputText", "").strip()
    except Exception as e:
        return f"Error calling Titan Text Express: {str(e)}"

def search_with_agent(query):
    """
    1. Uses DuckDuckGo search.
    2. Formats results into a structured prompt (loaded from prompt file).
    3. Calls AWS Bedrock (Titan Text Express) for summarization.
    4. Returns the AI-generated summary.
    """
    print(f"🔍 Searching DuckDuckGo for: {query}")
    
    # Perform web search
    search_results = search_duckduckgo(query)

    if not search_results:
        return "No relevant search results found."

    # Format search results into a readable summary prompt
    search_text = "\n".join(
        [f"{idx+1}. {r['title']} - {r['link']}\nSnippet: {r['snippet']}" for idx, r in enumerate(search_results)]
    )

    # Load dynamic prompt template
    prompt_template = load_prompt_template()
    prompt = prompt_template.format(query=query, search_text=search_text)

    print("🤖 Calling Titan Text AI for summarization...")
    
    # Get AI-generated summary
    summary = call_titan(prompt)
    return summary

# Test the agent
if __name__ == "__main__":
    query = "Latest AI advancements in 2025"
    print("\nAI-Generated Summary of Search Results:\n", search_with_agent(query))
