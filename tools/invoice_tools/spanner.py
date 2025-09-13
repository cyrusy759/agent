import gspread

class InvoiceSpanner:
    def __init__(self, invoice_text: str):
        self.product_name = ""
        self.quantity = 0
        self.fulfillment_period = date
        self.orderID = ""
        self.invoice_count = 1
        self.row_count = 0

    def login(self):
        gc = gspread.service_account(filename="path/to/credentials.json")
        return gc
    
    def confirm_login(self):
        gc = self.login()
        try:
            gc.open("TCBM...")
            return True
        except Exception as e:
            print(f"Login failed: {e}")
            return False

    def input_inovice(self, invoice_text: str):
        worksheet = gc.open("TCBM...").sheet1
        invoice_tab = worksheet.open(f"Invoice_{self.invoice_count}")
        
        if invoice_tab.row_count < 100:
            invoice_tab.append_row([self.product_name, self.quantity, self.fulfillment_period, self.orderID])
        else:
            self.invoice_count += 1
            new_tab = worksheet.add_worksheet(title=f"Invoice_{self.invoice_count}", rows="100", cols="20")
            new_tab.append_row([self.product_name, self.quantity, self.fulfillment_period, self.orderID])
    
    def delete_most_recent_invoice(self):
        worksheet = gc.open("TCBM...").sheet1
        invoice_tab = worksheet.worksheet(f"Invoice_{self.invoice_count}")
        invoice_tab.delete_row(invoice_tab.row_count)

        



    