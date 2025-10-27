from langgraph.graph import StateGraph, END, START  
from typing import TypedDict, List
from langchain_core.messages import HumanMessage, SystemMessage
from openai import OpenAI
import os 
from scraper import fetch_repo_code

OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="" + OPEN_AI_KEY,
)

def call_summarization_agent(message_content):
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
        "content": summary_extraction_prompt + " \n" + message_content
        }
    ]
    )
    return completion.choices[0].message.content


summary_extraction_prompt = """
You are an intelligent code summarizer that extracts the most relevant information from a given source code file.

I will provide you with the **full content of a single file** from a GitHub repository.

Your task is to analyze the file carefully and return **only the information that would be useful for generating a README.md** for the overall project.

Focus on identifying and summarizing:
1. **File Purpose:** Explain what this file does or what its main responsibility is.
2. **Key Functions or Classes:** List important functions/classes with a one-line description each.
3. **Dependencies/Imports:** Mention any key libraries, frameworks, or internal modules it depends on.
4. **Inputs and Outputs:** Describe what kind of data it takes in and what it returns or produces.
5. **Core Logic or Algorithms:** Summarize any special or unique logic, algorithms, or workflows implemented.
6. **Connections:** Describe how this file interacts with other modules, APIs, or external systems.
7. **Configurations or Constants:** Note any critical parameters, environment variables, or constant definitions.
8. **Entry Point:** If it can be executed directly (like `main()` or similar), explain how execution begins.

Return your answer strictly in the following **JSON format**:
{
    "file_name": "",
    "purpose": "",
    "key_components": [],
    "dependencies": [],
    "inputs_outputs": "",
    "important_logic": "",
    "connections": "",
    "configurations": "",
    "entry_point": ""
}

Here is the file content:
<insert file content here>
"""


class AgentState(TypedDict):
    repo_url : str
    file_summaries : List[SystemMessage]
    file_count : int
    i : int
    files : List[dict]
    current_summarizing_file : str
    

def intialization(state: AgentState) -> AgentState:
    state['files'] = fetch_repo_code(state['repo_url'])
    state['file_count'] = len(state['files'])
    state['i'] = 0
    return state



def summarize_the_current_file(state: AgentState):
    current_file = state['files'][state['i']]
    file_name = current_file.get("path", "unknown_file")
    file_content = current_file.get("content", "")

    # Combine the filename and content into the prompt
    message_content = f"File name: {file_name}\n\n{file_content}"

    summarized_file = call_summarization_agent(message_content)
    print(summarized_file)

    # (Optional) store the summary for later use
    if "file_summaries" not in state:
        state["file_summaries"] = []
    state["file_summaries"].append(summarized_file)

    # Move to next file
    state['i'] += 1
    return state


def should_continue(state: AgentState) -> AgentState:
    """Weather to continue the loop or not"""
    if state['i'] < state['file_count']:
        return "loop"
    else :
        return "exit"


def export_readme(state: AgentState):
    """
    This function takes all the summarized information of files in the repository
    and generates a professional README.md file using the LLM.
    """

    # Combine all summaries from the agent
    summaries_text = "\n\n".join(state.get("file_summaries", []))

    # Prompt to instruct the model to generate a README
    readme_generation_prompt = f"""
    You are an intelligent documentation generator.
    I will provide you with structured summaries of all files from a GitHub repository.

    Your task is to analyze all the provided information and generate a clean, well-formatted,
    and professional **README.md** for the repository.

    ### The README should include:
    1. **Project Title and Overview:** Describe what the project is about.
    2. **Key Features:** List important functionalities or modules.
    3. **Tech Stack:** Mention main technologies, frameworks, and libraries used.
    4. **Project Structure:** Summarize what each major file or folder does (based on summaries provided).
    5. **Setup Instructions:** (If any dependencies or setup steps are mentioned in summaries)
    6. **Usage:** Describe how to run or use the project.
    7. **Contributing (Optional):** Add if it seems relevant.
    8. **License (Optional):** Add if license info appears.
    
    Be concise, professional, and well-structured.
    Use Markdown formatting properly (headings, code blocks, bullet points, etc.).

    Here are the summarized file details:
    {summaries_text}
    """

    # Call the model
    completion = client.chat.completions.create(
        model="x-ai/grok-code-fast-1",
        messages=[{"role": "user", "content": readme_generation_prompt}]
    )

    readme_content = completion.choices[0].message.content

    # Export to README.md
    with open("GENERATED_README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("\n✅ README.md file generated successfully as 'GENERATED_README.md'")
    return state


graph = StateGraph(AgentState)

graph.add_node("Initialization", intialization)
graph.add_edge(START, "Initialization")
graph.add_node("summarize", summarize_the_current_file)
graph.add_edge("Initialization", "summarize")
graph.add_conditional_edges(
    "summarize", 
    should_continue, 
    {
        "loop" : "summarize", 
        "exit" : "Export_README"
    }
)
graph.add_node("Export_README", export_readme)
graph.add_edge("summarize", "Export_README")
graph.add_edge("Export_README", END)
app = graph.compile()


app.invoke({"repo_url" : "https://github.com/rivindu-ashinsa/Doc-Drafter"})