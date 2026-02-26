from tabulate import tabulate

class Budget: 
    def __init__(self):
        self.income = 0
        self.expenses = []

    def total_expense(self, name, amount):
        self.expenses.append([name, float(amount)])

        total = 0
        for expense in self.expenses:
            total += expense[1] #takes the expenses and adds them all together
        return total

    def balance(self, income, expenses):
        total_budget = float(income) - float(expenses)
        return total_budget 
    
def display_menu(): #displays the tabulate menu when called

    data = [   #data columns separated by comma
    ["Update Income", 1],
    ["Add Expense", 2],
    ["Edit Expense", 3],
    ["Display Balance", 4]
        ]

    headers = [  #headers separated by comma
        "Menu", "Select Option" 
        ]

    print(tabulate(data, headers=headers, tablefmt="grid"))
    

def main():
    budget = Budget() #create an object from the budget class

    print(" ")
    print("Welcome to the terminal budget calculator!")

    display_menu()
    
    try:
        user_selection = input("Select from the menu to proceed: ") #outside try except block is if user enters non numeric input
        
        if user_selection == "1": #UPDATE INCOME these are the sections that are based on user selections 
            try: 
                budget.income = float(input("What is your income?")) 
                display_menu()
                user_selection = input("Income updated. Select from the menu to proceed: ")
            except ValueError:
                print("Invalid input, just enter numeric value.")
                budget.income = float(input("What is your income?")) 
                display_menu()
                user_selection = input("Income updated. Select from the menu to proceed: ")

        if user_selection == "2": #ADD EXPENSE 
            while True:
                name = input("What is the expense name? (type x to exit no more expenses)")
                if name == "x": 
                    break
                amount = float(input("What is the expense amount?"))
                total_expenses = budget.total_expense(name, amount)
                budget.balance(budget.income, total_expenses)
            display_menu()
            user_selection = input("Expense updated. Select from the menu to proceed: ")

        if user_selection == "4": #DISPLAY BALANCE
            print("Balance: ", budget.balance(budget.income, total_expenses))

    except ValueError:
        print("Please enter a valid selection from the menu")

    


if __name__ == "__main__":
    main()

#testing better comments extension
# TODO: oh cool
#! importante
#* highlighted