import os 
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()
API_KEY = os.getenv("TELEGRAM_API_KEY")

