import json

class Atm:

    def __init__(self, filename="Advance_atm_Class/atm.json"): # "Advance_atm_Class/atm.txt"

        self.filename = filename
        self.account = {}
        self.load_account()

    # .txt
    # def load_account(self):

    #     try:
    #         with open(self.filename, "r") as f:
    #             for line in f:
    #                 line = line.strip()
    #                 if not line:
    #                     continue
    #                 acc_no, name, balance, pin = line.split()
    #                 self.account[acc_no] = {
    #                     "name": name,
    #                     "balance": int(balance),
    #                     "pin": pin,
    #                     "history": []
    #                 }
    #     except FileNotFoundError:
    #         open(self.filename, "w").close()

    # def save_account(self):
    #     with open(self.filename, "w") as f:
    #         for acc_no, data in self.account.items():
    #             f.write(f"{acc_no} {data['name']} {data['balance']} {data['pin']}\n")

    # .josn
    def load_account (self):

        try:

            with open (self.filename , "r") as f:
                self.account = json.load(f)

        except FileNotFoundError:
            self.account = {}

    def save_account (self):
        with open (self.filename , "w") as f:
            json.dump(self.account , f , indent=4)      

    def creat_account(self):
        acc_no = input("Enter 10-digit account number: ").strip()

        if not acc_no.isdigit() or len(acc_no) != 10:
            print("Account number must be 10 digits.")
            return

        if acc_no in self.account:
            print("Account already exist.")
            return

        name = input("Enter your name: ").strip()

        try:
            balance = int(input("Enter starting amount: "))
        except ValueError:
            print("Invalid amount type.")
            return

        if balance <= 0:
            print("Amount must be greater than 0.")
            return

        pin = input("Enter 4-digit pin: ")
        if not pin.isdigit() or len(pin) != 4:
            print("Invalid pin.")
            return

        self.account[acc_no] = {
            "name": name,
            "balance": balance,
            "pin": pin,
            "history": []
        }

        self.save_account()
        print("Your account has been created successfully.")

    def login(self):
        acc_no = input("Enter 10-digit account number: ").strip()

        if acc_no not in self.account:
            print("Account does not exist.")
            return None

        for attempts in range(3):
            pin = input("Enter 4-digit pin: ")
            if pin == self.account[acc_no]["pin"]:
                print("Login successful")
                return acc_no
            else:
                print(f"Invalid pin. Remaining attempts: {2 - attempts}")

        print("Too many attempts! You ran out of attempts.")
        return None

    def Exit(self):
        print("Thank you for using ATM.")

    def depostie(self, acc_no):
        try:
            amount = int(input("Enter an amount for deposit: "))
        except ValueError:
            print("Invalid amount type.")
            return

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        self.account[acc_no]["balance"] += amount
        self.account[acc_no]["history"].append(f"+{amount} deposited")
        self.save_account()
        print("Amount deposited successfully.")

    def withdraw(self, acc_no):
        try:
            amount = int(input("Enter an amount for withdrawn: "))
        except ValueError:
            print("Invalid amount type.")
            return

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > self.account[acc_no]["balance"]:
            print("Insufficient balance")
            return

        self.account[acc_no]["balance"] -= amount
        self.account[acc_no]["history"].append(f"-{amount} withdrawn")
        self.save_account()
        print("Amount withdrawn successfully.")

    def transfer(self, acc_no):
        receiver = input("Enter receiver account number: ").strip()

        if receiver not in self.account:
            print("Account does not exist.")
            return

        if receiver == acc_no:
            print("You cannot transfer to yourself!")
            return

        try:
            amount = int(input("Enter an amount for transfer: "))
        except ValueError:
            print("Invalid amount type.")
            return

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > self.account[acc_no]["balance"]:
            print("Insufficient balance")
            return

        self.account[acc_no]["balance"] -= amount
        self.account[receiver]["balance"] += amount

        self.account[acc_no]["history"].append(f"-{amount} sent to {receiver}")
        self.account[receiver]["history"].append(f"+{amount} received from {acc_no}")

        self.save_account()
        print("Transfer successful.")

    def check_balance(self, acc_no):
        balance = self.account[acc_no]["balance"]
        print(f"Current balance: {balance}")

    def view_history(self, acc_no):
        history = self.account[acc_no]["history"]

        if not history:
            print("No transactions yet.")
            return

        print("\n--- Last Transactions ---")
        for record in history[-5:][::-1]:
            print(record)

    def Logut(self):
        print("Logged out.")

    def session_menu(self, acc_no):
        while True:
            print("\n--- ATM MENU ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Logout")

            try:
                choice = int(input("Choose an option: "))
            except ValueError:
                print("Choice must be a number.")
                continue

            if choice == 1:
                self.depostie(acc_no)
            elif choice == 2:
                self.withdraw(acc_no)
            elif choice == 3:
                self.transfer(acc_no)
            elif choice == 4:
                self.check_balance(acc_no)
            elif choice == 5:
                self.view_history(acc_no)
            elif choice == 6:
                self.Logut(acc_no)
                break
            else:
                print("Invalid option!")

    def main_menu(self):
        while True:
            print("\n--- MAIN MENU ---")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")

            try:
                choice = int(input("Choose an option: "))
            except ValueError:
                print("Choice must be a number.")
                continue

            if choice == 1:
                self.creat_account()
            elif choice == 2:
                user = self.login()
                if user:
                    self.session_menu(user)
            elif choice == 3:
                print("Thank you for using ATM.")
                break
            else:
                print("Invalid option!")


if __name__ == "__main__":
    a = Atm()
    a.main_menu()
