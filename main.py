
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
    


def main():
    budget = Budget() #create an object from the budget class
    
    try: 
        budget.income = float(input("What is your income?")) 
    except ValueError:
        print("Invalid input, just enter numeric value.")
        budget.income = float(input("What is your income?")) 

    while True:
        name = input("What is the expense name? (type x to exit no more expenses)")
        if name == "x": 
                break
        amount = float(input("What is the expense amount?"))
        total_expenses = budget.total_expense(name, amount) 

    print("Balance: ", budget.balance(budget.income, total_expenses))

if __name__ == "__main__":
    main()

#GET user input of menu option
#DISPLAY confirmation of selection to UI - add error handling for invalid input?
#IF user selects 1 THEN call expense()
#IF user selects 2 THEN call expense()
#IF user selects 3 THEN call income()
#IF user selects 4 THEN call method()

#IF expense() method is called AND selection 1, super().add() within expense subclass
#LOAD new .csv file
#GET user input for name and amount
#SAVE .csv file
#DISPLAY budget UI

#IF expense() method is called AND selection 2, super().edit() within expense subclass
#GET user input of which expense to edit
#LOAD previous .csv file
#GET user input for expense and amount
#SAVE .csv file
#DISPLAY budget UI

#IF income() method is called AND selection 3, super().edit() within income subclass
#LOAD previous .csv file
#GET user input for name and amount
#SAVE .csv file
#DISPLAY budget UI

# _____
#IF user selects 'changes for income'
#GET user selection from menu for income
#CALL function for that menu input selection
#GET user input for method called
#UPDATE ledger
#SAVE .csv file
#DISPLAY budget UI

#IF user selects 'changes for income'
#AND selects new/edit income
#GET user input for state of residence
#CALCULATE net income after taxes using value of variable
#UPDATE ledger
#SAVE .csv file
#DISPLAY budget UI


 

#testing better comments extension
# TODO: oh cool
#! importante
#* highlighted