from agents.invoice_agent.invoice_agent import Agent as InvoiceAgent
from telegram_agent.telegram_api import TelegramBot

class Workflow:
    def __init__(self):
        self.telgram_bot = TelegramBot()
        self.invoice_agent = InvoiceAgent()

    async def workflow_run(self, message):

         




        response = await self.invoice_agent.generate_agent().run(message)
        return response
