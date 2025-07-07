# Phi Finance Agent

This project is a financial AI agent playground built on the Phi platform, leveraging the Groq large language model (LLM) for natural language queries.

## Features

- **Stock Price Retrieval:** Get real-time stock prices for companies.
- **Analyst Recommendations:** Summarize the latest analyst ratings and opinions.
- **Company News:** Fetch recent news articles related to companies.
- **Web Search Agent:** Search the web for additional information with source attribution.
- **Interactive Playground:** Provides an interface to interact with multiple AI agents simultaneously.

## Technologies Used

- [Phi AI platform](https://phidata.app)
- Groq LLM (`llama3-70b-8192` model)
- YFinance for financial data
- DuckDuckGo API for web searches
- FastAPI and Uvicorn for serving the playground app

## File Structure

- `financial_agent.py`: Defines the financial AI agent with relevant tools.
- `playground.py`: Combines agents and serves the interactive playground.
- `.env`: Environment variables including API keys.
- `requirements.txt`: Python dependencies for the project.
- `render.yaml`: Configuration file for deploying on Render.com

---

Created to demonstrate integration of LLMs with financial and web data APIs, designed for deployment as a web service.
