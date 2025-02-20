import sys 
from bank_account import BankAccount 

def main():
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("usage: python main_0.py <command>:<amount>")
        print("commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None 

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount: .2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"withdrew: ${amount:.2f}")
        else:
            print("insufficient funds.")
    elif command == "display":
        account.display_balance()
    else: 
        print("invalid command.")

if __name__ =="__main__":
    main()