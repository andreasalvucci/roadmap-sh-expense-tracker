import argparse
import json
import datetime
from Expense import Expense

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument("--description", type=str)
    parser.add_argument("--amount", type=int)
    parser.add_argument("--id", type=int)
    parser.add_argument("--month", type=int)
    args = parser.parse_args()
    if args.command:
        match args.command:
            case "list":
                list_expenses()
            case "add":
                if not args.description:
                    print("Please provide a description for the expense")
                    exit()
                if not args.amount:
                    print("Please provide an amount for the expense")
                    exit()
                date = datetime.datetime.now().strftime("%d/%m/%Y")
                amount = int(args.amount)
                description = args.description
                new_expense = Expense(date,description,amount)
                add_expense(new_expense)

            case "delete":
                if not args.id:
                    print("Please provide an ID for the expense to delete!")
                    exit()
                id_to_delete = args.id
                if id_to_delete <=0:
                    print("The expense to delete does not exist!")
                    exit()
                else:
                    found = delete_expense(id_to_delete)
                    if not found: 
                        print("An expense with that ID could not be found!")
                    else:
                        print("Expense deleted successfully!")
            case "summary":
                if not args.month:
                    show_summary()
                if args.month:
                    month = args.month
                    if month<1 or month>12:
                        print("Incorrect month!")
                        exit()
                    else:
                        show_summary(month=month)
            case "update":
                if not args.id:
                    print("Please provide the id for the expense to update!")
                    exit()



        


def show_summary(month=0):
    file = json.load(open("expenses.json"))
    expenses_list = file["transactions"]
    total = 0
    current_year = datetime.datetime.now().year
    if month == 0:
        for expense in expenses_list:
            total+=expense["Amount"]
    else:
        for expense in expenses_list:
            date_of_expense = datetime.datetime.strptime(expense["Date"],"%d/%m/%Y")
            if date_of_expense.year == current_year and date_of_expense.month == month:
                total+=expense["Amount"]
    print("# Total expenses: € {0}".format(total))

def delete_expense(id_to_delete):
    file_json = json.load(open("expenses.json"))
    expenses = file_json["transactions"]
    found = False
    for expense in expenses:
        if id_to_delete == expense["ID"]:
            expenses.remove(expense)
            file_json["transactions"] = expenses
            json.dump(file_json,open("expenses.json","w"))
            found = True

    return found

def list_expenses():
    expenses_dict = json.load(open("expenses.json"))
    print("#\tID\tDate\tDescription\tAmount")
    #print(expenses_dict["transactions"])
    for expense in expenses_dict["transactions"]:
        print("#\t{0}\t{1}\t{2}\t{3}".format(expense["ID"],expense["Date"],expense["Description"],expense["Amount"]))


def add_expense(expense):
    if expense.get_amount() <= 0:
        print("Impossible to add an expense with amount zero or negative")
    else:
        file_json = json.load(open("expenses.json"))
        transactions = file_json["transactions"]
        for transaction in transactions:
            id = transaction["ID"]
        id_to_add = id + 1
        print(id_to_add)
        new_expense = {
            "ID" : id_to_add,
            "Date": expense.get_date(),
            "Description": expense.get_description(),
            "Amount": expense.get_amount()
        }
        transactions+=[new_expense]
        file_json["transactions"] = transactions
        print(type(transactions))
        json.dump(file_json,open("expenses.json","w"))

# Using the special variable 
# __name__
if __name__=="__main__":
    main()