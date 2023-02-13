class Bank:
	def __init__(self,ifsc_Code, bankName, branchName,loc):
		self.ifsc_Code=ifsc_Code
		self.bankName=bankName
		self.branchName= branchName
		self.loc=loc
	def show_bank_details(self):
		print("Bank details: ")
		print("")
		print("IFSC Code:", self.ifsc_Code)
		print("Bank Name:", self.bankName)
		print("Branch Name:", self.branchName)
		print("Location:", self.loc)
class Customer:
	def __init__(self, cust_ID, custName, address,contactDetails):
		self.cust_ID=cust_ID
		self.custName=custName
		self.address= address
		self.contactDetails=contactDetails
	def show_customer_details(self):
		print("Customer details: ")
		print("")
		print("Customer ID:", self.cust_ID)
		print("Customer Name:", self.custName)
		print("Address:", self.address)
		print("Contact details:", self.contactDetails)
class Account(Bank):
        def __init__(self, ifsc_Code, bankName, branchName,loc,cust_ID, custName, address,contactDetails, accountID):
                super().__init__(ifsc_Code, bankName, branchName,loc)
                self.cust_ID=cust_ID
                self.custName=custName
                self.address=address
                self.contactDetails=contactDetails
                self.accountID=accountID
                self.balance=0
        def getAccountInfo(self):
                print("Customer Account details: ")
                print("Account ID:", self.accountID)
                print("")
                obCustomer=Customer.show_customer_details(self)
        def deposit(self, amount):
                self.amount=amount
                self.balance=self.balance+self.amount
                print("Customer Account Balance has been updated after the deposit of amount Rs.",self.amount, "to :Rs.",self.balance)
        def withdraw(self, amount):
                self.amount=amount
                if self.amount>self.balance:
                    print("Insufficient funds|Available Balance: Rs.",self.balance)
                else:
                    self.balance=self.balance-self.amount 
                    print("Account Balance after withdrawal of amount Rs.",self.amount, "is :Rs.",self.balance)
        def getAccountBalance(self):
            print("Account Balance is :Rs.",self.balance)
class SavingsAccount(Account):
        def __init__(self, ifsc_Code, bankName, branchName,loc, cust_ID, custName, address,contactDetails, accountID,minbalance):
                super().__init__(ifsc_Code, bankName, branchName,loc,cust_ID, custName, address,contactDetails, accountID)
                self.cust_ID=cust_ID
                self.custName=custName
                self.address=address
                self.contactDetails=contactDetails
                self.minbalance=500
        def getSavingsAccountInfo(self):
                print("Customer Savings Account details: ")
                print("Account ID:", self.accountID)
                print("Minimum amount in a savings account should be: Rs.",self.minbalance)
                print("")
                obCustomer=Customer.show_customer_details(self)
        def depositToSavingsAccount(self, amount):
                self.amount=amount                
                self.balance=self.balance+self.amount
                print("Customer Savings Account Balance has been updated after the deposit of amount Rs.",self.amount, "to :Rs.",self.balance)
                if self.balance<self.minbalance:
                    print("Minimum amount in a Savings Account should be: Rs.",self.minbalance, "Please deposit the amount to maintain minimum balance :Rs.",self.minbalance-self.balance)
        def withdrawFromSavingsAccount(self, amount):
                self.amount=amount
                if self.amount>self.balance:
                    print("Insufficient funds|Available Balance: Rs.",self.balance)
                elif self.balance-self.amount>=self.minbalance:
                    self.balance=self.balance-self.amount 
                    print("Customer Savings Account Balance after withdrawal of amount Rs.",self.amount, "is :Rs.",self.balance)
                else:
                   print("The withdrawl cannot be made as the minimum amount in a Savings Account should be: Rs.",self.minbalance)
        def getSavingsAccountBalance(self):
                if self.balance<self.minbalance:
                    print("Minimum amount in a Savings Account should be: Rs.",self.minbalance)
                print("Savings Account Balance is :Rs.",self.balance)
