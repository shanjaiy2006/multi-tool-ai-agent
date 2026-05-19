from langchain_core.messages import HumanMessage #high level framework that allows us to build AI applications.
from langchain_groq import ChatGroq #allows us to use Groq's within langchain and langgraph 
from langchain.tools import tool
from langchain.agents import create_agent #complex framework that allows us to build AI Agents
from dotenv import load_dotenv
import requests
import os
from tavily import TavilyClient
import smtplib
from email.message import EmailMessage
from googleapiclient.discovery import build
from pypdf import PdfReader

load_dotenv()
youtube = build('youtube', 'v3', developerKey=os.getenv("YOUTUBE_API_KEY"))

@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city"""
    print("WEATHER TOOL EXECUTED")
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        return f"The current temperature in {city} is {temp}°C."
    else:
        return f"Sorry, I couldn't fetch the weather for {city}."
    
@tool
def internet_search(query: str) -> str:
    """Perform an internet search for the given query and return the top result."""
    print("INTERNET SEARCH TOOL EXECUTED")
    api_key = os.getenv("TAVILY_API_KEY")
    client = TavilyClient(api_key)
    response = client.search(query)
    return str(response)

@tool
def send_email(to: str, subject: str,body: str) -> str:
    """Send an email to the specified recipient."""
    print("SEND EMAIL TOOL EXECUTED")
    sender_email = os.getenv("EMAIL_ADDRESS")
    email_app_password = os.getenv("EMAIL_APP_PASSWORD")

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(sender_email, email_app_password)
        smtp.send_message(msg)

    return "Email sent successfully to {to} with subject '{subject}'."

@tool
def youtube_search(query: str) -> str:
    """Search YouTube videos and return exactly 3 video links."""
    print("YOUTUBE SEARCH TOOL EXECUTED")
    request = youtube.search().list(
        q = query,
        part = 'snippet',
        maxResults = 3,
        type = 'video'
    )
    response = request.execute()
    results = []

    for item in response['items']:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        url = f"https://www.youtube.com/watch?v={video_id}"
        results.append(f"{title}: {url}")

    return str(results[:3]) #returning exactly 3 video links

@tool
def read_pdf(file_path: str) -> str:
    """Read a PDF file and return its content as text."""
    print("READ PDF TOOL EXECUTED")
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    return text[:3000] #returning only the first 3000 characters to avoid overwhelming the agent

@tool
def say_hello(name: str) -> str:
    """A simple tool that says hello to the user."""

    print("TOOL EXECUTED")

    return f"Hello, {name}!"

@tool
def multiply(a: int, b: int) -> str:
    """Multiply two numbers."""

    print("MULTIPLY TOOL EXECUTED")

    return f"{a} multiplied by {b} is {a*b}."

def main():
    model = ChatGroq(temperature=0,model_name="llama-3.3-70b-versatile",disable_streaming=True)

    tools = [say_hello,multiply,get_weather,internet_search,send_email,youtube_search,read_pdf] #tool is some external service that the agent can call to get information or perform actions. For example, a calculator tool that can perform mathematical calculations, or a web search tool that can fetch information from the internet.
    agent_executor =  create_agent(
        model = model,
        tools = tools
    )

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()
        if(user_input == "quit"):
            break

        response = agent_executor.invoke(
            {"messages": [HumanMessage(content=user_input)]}
        )

        print("Assistant:", response["messages"][-1].content)

        print()


if __name__ == "__main__":
    main()
        

