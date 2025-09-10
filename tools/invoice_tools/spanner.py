import gspread

class InvoiceSpanner:
    def __init__(self, invoice_text: str):
        self.product_name = ""
        self.quantity = 0
        self.fulfillment_period = date
        self.orderID = ""
        self.invoice_count = 1

    def input_inovice(self, invoice_text: str):
        worksheet = gc.open("TCBM...").sheet1
        invoice_tab = worksheet.open(f"Invoice_{self.invoice_count}")
        
        if invoice_tab.row_count < 100:
            invoice_tab.append_row([self.product_name, self.quantity, self.fulfillment_period, self.orderID])
        else:
            self.invoice_count += 1
            new_tab = worksheet.add_worksheet(title=f"Invoice_{self.invoice_count}", rows="100", cols="20")
            new_tab.append_row([self.product_name, self.quantity, self.fulfillment_period, self.orderID])

        



    