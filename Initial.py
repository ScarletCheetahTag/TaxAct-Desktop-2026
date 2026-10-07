from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Expense:
    title: str
    category: str
    amount: float


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add(self, title, category, amount):
        self.expenses.append(Expense(title, category, amount))

    def total(self):
        return sum(expense.amount for expense in self.expenses)

    def by_category(self):
        result = defaultdict(float)

        for expense in self.expenses:
            result[expense.category] += expense.amount

        return dict(result)

    def show_report(self):
        print("Expense Tracker")
        print("===============")

        for index, expense in enumerate(self.expenses, 1):
            print(
                f"{index}. {expense.title} | "
                f"{expense.category} | "
                f"${expense.amount:.2f}"
            )

        print()
        print(f"Total: ${self.total():.2f}")
        print()
        print("By Category")
        print("-----------")

        for category, amount in sorted(
            self.by_category().items(),
            key=lambda item: item[1],
            reverse=True
        ):
            print(f"{category}: ${amount:.2f}")


tracker = ExpenseTracker()

tracker.add("Laptop", "Technology", 1200)
tracker.add("Coffee", "Food", 5.50)
tracker.add("Internet", "Services", 45)
tracker.add("Headphones", "Technology", 180)
tracker.add("Dinner", "Food", 32.75)
tracker.add("Cloud Storage", "Services", 12)

tracker.show_report()