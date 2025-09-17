import os 
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from agents.invoice_agent.invoice_agent import InvoiceAgent
import requests 

load_dotenv()

class TelegramBot:
    def __init__(self):
        self.api_key = os.getenv("TELEGRAM_API_KEY")
        self.application = Application.builder().token(self.api_key).build()
        self.agent_url = "http://localhost:8000/invoice_agent"
        
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle incoming messages and send them to the invoice agent"""
        message = update.message.text
        chat_id = update.message.chat_id
        
        # Send message to the agent
        agent_response = self.send_to_agent(message)
        
        # Process the agent's response
        if agent_response:
            try:
                result = InvoiceAgent._run(agent_response)
                # You might want to send the result back to the user
                await update.message.reply_text(str(result))
            except Exception as e:
                error_msg = f"Error processing the response: {e}"
                print(error_msg)
                await update.message.reply_text("Sorry, I encountered an error processing your request.")
    
    def send_to_agent(self, message: str):
        """Send message to the invoice agent and return the response"""
        try:
            response = requests.post(
                self.agent_url, 
                json={"query": message},
                timeout=10  # Add timeout for better error handling
            )
            response.raise_for_status()  # Raise exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with agent: {e}")
            return None
        except ValueError as e:
            print(f"Error parsing JSON response: {e}")
            return None
    
    def setup_handlers(self):
        """Set up message handlers"""
        self.application.add_handler(CommandHandler("start", self.handle_message))
        self.application.add_handler(CommandHandler("help", self.handle_message))
        # Add more handlers as needed
    
    def run(self):
        """Start the bot"""
        self.setup_handlers()
        print("Bot is running...")
        self.application.run_polling()


