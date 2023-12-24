import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self,title,amount):
        self.id =str(uuid.uuid4())
        self.title =title
        self.amount =amount
        self.created_at =datetime.utcnow()
        self.updated_at =self.created_at

    def update(self, title=None,amount=None):
        if self.title is not None:
            self.title =title
        if self.amount is not None:
            self.amount = amount
        self.updated_at =datetime.utcnow()
        print(f'The Expense has been updated successfully')

    def to_dict(self):
        return {
            'id':self.id,
            'Title':self.title,
            'Amount':self.amount,
            'Created_at':self.created_at,
            'Updated_at':self.updated_at
        }
    def __repr__(self)->str:
        return(f'{self.title} {self.amount}')
# expense =Expense("Stationary",600.23)
# print(expense.to_dict())
    
class ExpenseDatabase:
    def __init__(self):
        self.expenses=[]#Creating a list

    def add_expense(self,expense):
        #function to add expense into the database
        self.expenses.append(expense)
        print(f'{expense} added successfully')

    def remove_expense(self,expense_id):
        #method to remove expense via its id
        self.expenses =[expense for expense in self.expenses if expense.id !=expense_id ]
        print(f'Expense with id:{expense_id}has been removed')

    def get_expense_by_id(self,expense_id):
        expense =[expense for expense in self.expenses if expense.id ==expense_id]
        if len(expense)==0:
            return None
        return expense[0]
    
    def get_expense_by_title(self,expense_title):
        return[expense for expense in self.expenses if expense.title ==expense_title]
    
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
    






    
    

        
    
        