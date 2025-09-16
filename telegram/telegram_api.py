import os 
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from agents.invoice_agent.invoice_agent import InvoiceAgent
import requests 

load_dotenv()
API_KEY = os.getenv("TELEGRAM_API_KEY")

async def message_handling(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    chat_id = update.message.chat_id

    response = requests.post("http://localhost:8000/invoice_agent", json={"query": message})

    try:
        InvoiceAgent._run(response.json())
    except Exception as e:
        print (f"Error processing the response: {e}")

    


