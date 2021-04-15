import datetime
import random


class Receipt:
    today = datetime.date.today().strftime('%d-%m-%Y')
    receipts = []

    def __init__(self, household_name, receipt_number=None, date=None):
        self.household = household_name
        if date is None:
            self.date = Receipt.today
        else:
            self.date = str(date)

        if receipt_number is None:
            self.receipt_number = str(random.randint(10, 100))
        else:
            self.receipt_number = str(receipt_number)

    def show(self):
        return self.household, self.receipt_number, self.date

