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