import os
from dotenv import load_dotenv

import phi
import phi.api
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground

import uvicorn  # For Render deployment

load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

supported_model = "llama3-70b-8192"

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id=supported_model),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id=supported_model),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        ),
    ],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)

app = Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 7777))
    uvicorn.run("playground:app", host="0.0.0.0", port=port, reload=True)
