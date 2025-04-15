import os
import getpass

# Set the Anthropic API key
if not os.environ.get("ANTHROPIC_API_KEY"):
    os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Anthropic API Key: ")

# Load the LLM
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-3-7-sonnet-latest")

# Schema for structured output
from pydantic import BaseModel, Field


class SearchQuery(BaseModel):
    query: str = Field(description="Query that is optimized for web search")
    justification: str = Field(
        description="Why the query is relevant to the user's request"
    )


# Augment the LLM with schema for structured output
structured_llm = llm.with_structured_output(SearchQuery)

# Invoke the augmented LLM
output = structured_llm.invoke("How does Calcium CT score relate to high cholesterol?")

print(f"Query: {output.query}")
print(f"Justification: {output.justification}")
