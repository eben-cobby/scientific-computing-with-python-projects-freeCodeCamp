class Category:
    # initialize the category object with a name and empty ledger
    def __init__(self, category: str):
        self.category = category
        self.ledger = []
    
    # add a deposit to the ledger with an optional description
    def deposit(self, amount: float, description: str = ""):
        self.ledger.append({"amount": amount, "description": description})
    
    # attempt to withdraw from the ledger if enough funds are available
    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    # calculate the balance by summing the amounts in the ledger
    def get_balance(self):
        balance = sum(entry["amount"] for entry in self.ledger)
        return balance
    
    # transfer an amount to another category's ledger
    def transfer(self, amount: float, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.category}")
            other_category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False
    
    # check if enough funds are available for a given amount
    def check_funds(self, amount: float):
        return amount <= self.get_balance()
    
    # create a string representation of the ledger with a title and balance
    def __str__(self):
        category_length = len(self.category)
        start_asterisk = "*" * ((30 - category_length) // 2)
        end_asterisk = "*" * (30 - category_length - len(start_asterisk))
        title_line = f"{start_asterisk}{self.category}{end_asterisk}"

        ledger_items = ""
        for item in self.ledger:
            amount = "{:.2f}".format(item['amount'])[:7]
            description = item["description"][:23]
            ledger_items += "{:<23s}{:>7s}\n".format(description, amount)

        report = f"{title_line}\n{ledger_items.rstrip()}\nTotal: {self.get_balance():.2f}"

        return report

# Create a spend chart from a list of categories
def create_spend_chart(categories):
    withdrawals = []
    total_withdrawals = 0

    # Calculate the total withdrawals for each category
    for category in categories:
        category_withdrawals = sum(item["amount"] for item in category.ledger if item["amount"] < 0)
        withdrawals.append(category_withdrawals)

    # Calculate the percentage spent for each category
    total_withdrawals = sum(withdrawals)
    percentages = [round(withdrawal / total_withdrawals * 100) for withdrawal in withdrawals]

    # create a chart with percentages and category names
    chart = "Percentage spent by category\n"

    for i in range(100, -10, -10):
        chart += "{:>3d}|".format(i)
        for percentage in percentages:
            if percentage >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    chart += "    " + "---" * len(categories) + "-\n"

    category_names = [name.category for name in categories]
    max_name_length = max(len(name) for name in category_names)

    for i in range(max_name_length):
        chart += "    "
        for name in category_names:
            if i < len(name):
                chart += " " + name[i] + " "
            else:
                chart += "   "
        chart += " \n"
    
    return chart.rstrip("\n")
