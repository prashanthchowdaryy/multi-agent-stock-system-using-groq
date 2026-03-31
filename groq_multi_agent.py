import time
import random
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# 🔐 Load API key
load_dotenv()

# 🧠 Company → Symbol lookup function
def lookup_company_symbol(company: str) -> str:
    symbols = {
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL"
    }
    return symbols.get(company, "Unknown")

# 📊 Stock Agent (handles stock data)
stock_agent = Agent(
    name="Stock Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True
        )
    ],
    instructions=[
        "Fetch stock price, fundamentals, and analyst recommendations using stock symbols."
    ],
    markdown=True
)

# 🔍 Company Lookup Agent
company_lookup_agent = Agent(
    name="Company Lookup Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[lookup_company_symbol],
    instructions=[
        "Given a company name, return its stock symbol."
    ],
    markdown=True
)

# 🤝 Finance Team Agent (MAIN BRAIN)
finance_team = Agent(
    name="Finance Team",
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[company_lookup_agent, stock_agent],
    instructions=[
        "Step 1: Use Company Lookup Agent to get stock symbols for companies.",
        "Step 2: Use Stock Agent to fetch stock data using those symbols.",
        "Step 3: Compare both companies clearly (price, fundamentals, recommendations).",
        "Always follow steps in order."
    ],
    markdown=True
)

# 🔁 Retry logic (simple + safe)
def run_with_retry(agent, query, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = agent.run(query)

            if response:
                return response

        except Exception as e:
            print(f"Error: {e}")

        wait_time = random.uniform(delay, delay + 3)
        print(f"Retrying in {wait_time:.2f} seconds...")
        time.sleep(wait_time)

    print("❌ Max retries reached.")
    return None

# ▶️ Run query
query = "Find stock symbols for Apple and Google, fetch their stock data, and compare them."

response = run_with_retry(finance_team, query)

if response:
    print("\n✅ FINAL RESPONSE:\n")
    print(response.content)
else:
    print("❌ Failed to get response.")