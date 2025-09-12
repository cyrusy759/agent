from langchain.tools import Tool
from spanner import Spanner

def create_invoice_tool() -> Tool:
    def invoice_tool(invoice_text: str) -> str:
        spanner = Spanner(invoice_text)
        spanner.login()
        spanner.input_invoice(invoice_text)
        return "Invoice information has been successfully added to the spreadsheet."

    return Tool(
        name="InvoiceTool",
        func=invoice_tool,
        description="Use this tool to extract and input invoice information into a spreadsheet. "
                    "The input should be the text of the invoice.",
    )
