from dotenv import load_dotenv

from pydantic import BaseModel

from langchain_community.chat_models import ChatOllama


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_openai_tools_agent, AgentExecutor 

from tools import save_to_txt, scrape_tool, search_tool, save_tool

load_dotenv()



class LeadResponse(BaseModel):
    company: str
    company_info: str
    email: str
    summary: str
    outreach_message: str
    tools_used: list[str]

class LeadResponseList(BaseModel):
    leads: list[LeadResponse]

# Determining which AI model we will use, in this case, Gemini-2.5-flash
llm = ChatOllama(
    model="llama3",
    temperature=0.3
)
# Tell Gemini how to format the response using the Pydantic schema
parser = PydanticOutputParser(pydantic_object=LeadResponseList)

# The main part here. This is our prompt and the instructions we give to Gemini
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a sales enablement assistant.
            1. Use the 'scrape' tool to find exactly 5 local medium ranged companies in Noida, Gurgoan, Delhi from a variety of industries, that might need IT services.
            2. For each company identified by the 'scrape_website' tool, use the 'google_search' tool to gather detailed information from Google.
            3. Analyze the searched website content to provide:
                - company: The company name
                - contact_info: Any available contact details
                - summary: A brief qualification based on the scraped website content, focusing on their potential IT needs even if they are not an IT company.
                - email addresses
                - outreach message
                - tools_used: List tools used        

            Do not include extra text beyond the formatted output and the save confirmation message.
            4. Return the output as a list of 5 entries in this format: {format_instructions}
            5. After formatting the list of 5 entries, use the 'save_to_txt' tool to send the json format to the text file or Return only structured JSON output. 
            6. If the 'save_to_txt' tool runs, say that you ran it. If you did not run the 'save_to_txt' tool, say that you could not run it.
            """,
        ),
        ("human", "{query}"),  # The actual user instruction
        ("placeholder", "{agent_scratchpad}"),  # Where the agent's internal reasoning goes
    ]
).partial(format_instructions=parser .get_format_instructions())

tools = [scrape_tool, search_tool, save_tool]
  
agent = create_openai_tools_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = "Find and qualify exactly 5 local leads in Noida, Gurgoan, Delhi for IT Services. No more than 5 small businesses."

raw_response = agent_executor.invoke({"query": query})
output_text = raw_response["output"]

# Save manually
save_to_txt(output_text)

print(output_text)

try:
    structured_response = parser.parse(raw_response["output"])
    print(structured_response)
except Exception as e:
    print("Error parsing response:", e, "Raw_response - ", raw_response)
