import time
# # bankname = "Zenith bank"
# # account_no = 216576890
# # balance = 3400.57
# # account_name = "Sam Loen"



user1 = dict()
user2 = dict()
user3 = dict()
user4 = dict()
user5 = dict()

user1["bankname"] = "Zenith Bank"
user1["account_name"] = "Lara Poe"
user1["balance"] = 6789
user1["account_no"] = '7383974664'


user2["bankname"] = "Monetary Bank"
user2["account_name"] = "Mor Zen"
user2["balance"] = 1000.3
user2["account_no"] = '3456788992'


user3["bankname"] = "First Bank"
user3["account_name"] = "Gabriel Paul"
user3["balance"] = 26543.6
user3["account_no"] = '5666778899'


user4["bankname"] = "GTG Bank"
user4["account_name"] = "Rich Bishop"
user4["balance"] = 26543.6
user4["account_no"] = '5363782829'


user5["bankname"] = "Wema Bank"
user5["account_name"] = "Bella Mike"
user5["balance"] = 1300.7
user5["account_no"] = '6372929207'

# Display individual details in account.

# Add account details to the main dict bankDB

bankDB = dict()
bankDB["user1"] = user1
bankDB["user2"] = user2
bankDB["user3"] = user3
bankDB["user4"] = user4
bankDB["user5"] = user5

# for key, value in bankDB.items():
#     print ({key: value})

# Listbout the total account details in each account
# for key, value in bankDB.items():
#     for item, sub in value.items():
#         print({key: {item: sub}})


# # for key, val in bankDB.items():
#     print({key: val})


#  Automating the Bank App system
while True:
    try:
        print("Welcome to TrustedCoin Bank")
        # Retreive account from bankDB
        accountNumber = input("Enter your account number: ")
        
        # Search the Bank DB to verify the account Existence
        for user, details in bankDB.items():
            if accountNumber in details["account_no"]:
                found_account = details
                print(found_account.items())
                break
            else:
                # print("Account not found, Try Again!!!")
                # print("stored account: ", details['account_no'])
                # print("input account: ", accountNumber)
                continue
        
        if found_account:
            response = int(input("""
            press 1 to deposit
            press 2 to withdraw
            press 3 to View your account details
            press 4 to Exit
            """))

            if response == 1:    
                deposit = float(input('How much do you want to deposit'))
                found_account['balance'] += deposit
                print(f"Your account has been credited with N{deposit:,}".format(deposit=deposit))
                print(f"Your account Balance is N{found_account['balance']:,}".format(found_account['balance']))

            elif response == 2:
                
                withdraw = float(input('How much do you want to withdraw from this account'))
                found_account['balance'] -= withdraw
                print(f"Your account has been debited with N{withdraw:,}".format(withdraw=withdraw))
                print(f"Your account Balance is N{found_account['balance']:,}".format(found_account['balance']))

            elif response == 3:
            # view account detials
                for key, val in found_account.items():
                    print({key: val})
                    
            elif response == 4:
                print("Thanks for using our services.")
                print("Shutting Down...")
                time.sleep(3)
                break
        
        elif not found_account:
            print("Account not found, PLEASE TRY AGAIN!!!!")  
            break
    except:
        print("ERROR:Account not found")
        continue
    











# class Bankaccount:
    
#     def __init__(self, initial_balance=0):
#         self.balance = initial_balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
            
#         else:
#             print("Insufficient funds!")


# #  Creating a bank account instance
# account = Bankaccount()

# # Number of transactions to perform
# num_transactions = 3

# for i in range(num_transactions):
#     print(f"Transaction {i + 1}:")
#     action = input("Enter 'd' for deposit or 'w' for withdrawal: ")

#     if action.lower() == 'd':
#         amount = float(input("Enter deposit amount: "))
#         account.deposit(amount)
#         print(f"${amount} deposited.")
#     elif action.lower() == 'w':
#         amount = float(input("Enter withdrawal amount: "))
#         account.withdraw(amount)
#         print(f"${amount} withdrawn.")
#     else:
#         print("Invalid action. Please enter 'd' or 'w'.")

#     print(f"Current Balance: ${account.balance}\n")
#     print(account.balance)

        
            
        
            
# for details in bankDB.values():
#     for item in details.values():
#         print(item)

# for number in bankDB.values():
#     print(number)