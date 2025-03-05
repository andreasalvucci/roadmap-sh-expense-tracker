class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

    def set_date(self, date):
        self.date = date
    def set_description(self,description):
        self.description = description
    def set_amount(self,amount):
        self.amount = amount

    def get_date(self):
        return self.date
    def get_description(self):
        return self.description
    def get_amount(self):
        return self.amount
    
    def serialize(self):
        json_obj = {
            "Date": self.date,
            "Description": self.description,
            "Amount": self.amount
        }
        return json_obj