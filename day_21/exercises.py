## Day 21 - Exercises

# 1. Create a class that inherits methods from statistics module and overrides certain methods to produce the output specified in the document
import statistics

class Statistics:

    def __init__(self, list_in):
        self.list_in = list_in

    def count(self):
        return len(self.list_in)

    def sum(self):
        return sum(self.list_in)

    def min(self):
        return min(self.list_in)

    def max(self):
        return max(self.list_in)

    def range(self):
        return max(self.list_in) - min(self.list_in)

    def mean(self):
        return statistics.mean(self.list_in)

    def median(self):
        return statistics.median(self.list_in)

    def mode(self):
        return statistics.mode(self.list_in)

    def std(self):
        return statistics.stdev(self.list_in)

    def var(self):
        return statistics.variance(self.list_in)

    def freq_dist(self):

        counts = {}

        for num in self.list_in:
            counts[num] = counts.get(num, 0) + 1

        return counts.items()

# 2. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:

    def __init__(self, firstname, lastname, incomes, expenses):

        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        if (self.incomes is list):
            return sum(self.incomes)
        else:
            return self.incomes

    def total_expenses(self):
        if (self.expenses is list):
            return sum(self.expenses)
        else:
            return self.expenses

    def account_info(self):
        return dict(firstname=self.firstname, lastname=self.lastname, incomes=self.incomes, expenses=self.expenses)
    

    def add_income(self, add):
        return self.incomes.append(add)

    def add_expense(self, add):
        return self.expenses.append(add)

    def account_balance(self):
        return self.total_income() - self.total_expenses()

    

    
    