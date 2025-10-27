from openai import OpenAI
import os
from typing import TypedDict, List
from langchain_core.messages import HumanMessage


class AgentState(TypedDict):
    messages : List[HumanMessage]



OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="" + OPEN_AI_KEY,
)

def call_agent(message_content):
    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="x-ai/grok-code-fast-1",
    messages=[
        {
        "role": "user",
        "content": message_content
        }
    ]
    )
    return completion.choices[0].message.content