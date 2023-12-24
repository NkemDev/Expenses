# Expense Model Project
## Project Description
This project is about expense software to manage financial expenses. It is written in Python programming language. The program consists of two classes Expense and ExpenseDB. The Expense class has five attributes
* **id** - This uniquely identifies every expense object and it is generated by the Universal Unique Identifier (UUID) module. A UUID is a 128-bit value used to uniquely identify an object or entity on the internet.
* **title**: A string representing the title of the expense.
* **amount**: A float representing the amount of the expense.
* **created_at**: A timestamp indicating when the expense was created (UTC).
* **updated_at**: A timestamp indicating the last time the expense was updated (UTC)
  
It has three methods 
* **__init__**: Initializes all the attributes (title, amount,created_at and updated_at).
  ```
  def __init__(self,title,amount):
        self.id =str(uuid.uuid4())
        self.title =title
        self.amount =amount
        self.created_at =datetime.utcnow()
        self.updated_at =self.created_at
  ```
* **update**: Allows updating the title and/or amount, updating the updated_at timestamp.
  ```
  def update(self, title=None,amount=None):
        if self.title is not None:
            self.title =title
        if self.amount is not None:
            self.amount = amount
        self.updated_at =datetime.utcnow()
        print(f'The Expense has been updated successfully')
  ```
* **to_dict**: Returns a dictionary representation of the expense.
  ```
  def to_dict(self):
        return {
            'id':self.id,
            'Title':self.title,
            'Amount':self.amount,
            'Created_at':self.created_at,
            'Updated_at':self.updated_at
        }
  ```
  
For the ExpenseDB class, consists of one attribute **expenses**, which is an empty list. The methods for this class are;
* **__init__**: To initialize the attribute. In this class, there is only one attribute which is the expenses attribute and it is an empty list.
  ```
  def __init__(self):
        self.expenses=[] #Creates a list
  ```
* **add_expense**: This method allows you to add an item to the list
  ```
  def add_expense(self,expense):
        #function to add expense into the database
        self.expenses.append(expense)
        print(f'{expense} added successfully')
  ```
* **remove_expense**: This method allows you to remove an expense from the list via the expense_id which uniquely identifies each expense item.
  ```
  def remove_expense(self,expense_id):
        #method to remove expense via its id
        self.expenses =[expense for expense in self.expenses if expense.id !=expense_id ]
        print(f'Expense with id:{expense_id}has been removed')
  ```
* **get_expense_by _id**: This method returns an expense after searching using its id
  ```
  def get_expense_by_id(self,expense_id):
        expense =[expense for expense in self.expenses if expense.id == expense_id]
        if len(expense)==0:
            return None
        return expense[0]
  ```
* **get_expense_by_title**: This method returns a list of expense items of the same title using the title as its search method.
  ```
  def get_expense_by_title(self,expense_title):
        return[expense for expense in self.expenses if expense.title ==expense_title]
  ```
* **to_dict**: This method returns a list of dictionaries representing each expense in the database.
  ```
  def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
  ```