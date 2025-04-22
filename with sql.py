import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

class ATM:
    def __init__(self, root):
        self.root = root
        self.valid_pin = False
        self.correct_pins = {"1234", "0000", "4321"}
        self.app_state = "PIN_ENTRY"
        self.current_option = 0
        self.language = "English"
        self.balance = 1000.0
        self.options = [
            "Cash Withdrawal",
            "Deposit",
            "Balance Inquiry",
            "Funds Transfer",
            "Bill Payment",
            "PIN Change",
            "Statement Printing",
            "Language Options"
        ]

        self.root.title(" " * 110 + "ATM System")
        self.root.geometry("774x760+280+0")
        self.root.configure(background='gainsboro')

        MainFrame = Frame(self.root, bd=20, width=784, height=700, relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame1.grid(row=1, column=0, padx=12)
        TopFrame2 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame2.grid(row=0, column=0, padx=8)

        TopFrame2Left = Frame(TopFrame2, bd=7, width=190, height=300, relief=RIDGE)
        TopFrame2Left.grid(row=0, column=0, padx=3)
        TopFrame2Mid = Frame(TopFrame2, bd=7, width=200, height=300, relief=RIDGE)
        TopFrame2Mid.grid(row=0, column=1, padx=3)
        TopFrame2Right = Frame(TopFrame2, bd=7, width=190, height=300, relief=RIDGE)
        TopFrame2Right.grid(row=0, column=2, padx=3)

        self.msgArea = Text(TopFrame2Mid, height=10, width=42, bd=12, font=('arial', 9, 'bold'))
        self.msgArea.grid(row=0, column=0)
        self.msgArea.insert(END, "Please enter your PIN.\n")

        self.pinEntry = Entry(TopFrame2Mid, font=('arial', 18, 'bold'), bd=12, width=25, justify='center', show='*')
        self.pinEntry.grid(row=1, column=0)

        self.img_arrow_left = PhotoImage(file="ATM_Icon/lArrow.png")
        self.img_arrow_right = PhotoImage(file="ATM_Icon/rArrow.png")

        self.arrow_buttons = []
        self.option_labels = []

        for i in range(8):
            if i < 4:
                btn = Button(TopFrame2Left, width=160, height=60, state=NORMAL, image=self.img_arrow_left,
                             command=lambda idx=i: self.select_option(idx))
                btn.grid(row=i, column=0, padx=2, pady=2)
                label = Label(TopFrame2Left, text=self.options[i], font=('arial', 12))
                label.grid(row=i, column=1)
            else:
                btn = Button(TopFrame2Right, width=160, height=60, state=NORMAL, image=self.img_arrow_right,
                             command=lambda idx=i: self.select_option(idx))
                btn.grid(row=i - 4, column=0, padx=2, pady=2)
                label = Label(TopFrame2Right, text=self.options[i], font=('arial', 12))
                label.grid(row=i - 4, column=1)

            self.arrow_buttons.append(btn)
            self.option_labels.append(label)

        img_files = [
            "one", "two", "three", "cancel",
            "four", "five", "six", "clear",
            "seven", "eight", "nine", "enter",
            "empty", "zero", "empty", "empty"
        ]

        self.num_mapping = {
            "one": "1", "two": "2", "three": "3",
            "four": "4", "five": "5", "six": "6",
            "seven": "7", "eight": "8", "nine": "9",
            "zero": "0"
        }

        self.imgs = [PhotoImage(file=f"ATM_Icon/{img}.png") for img in img_files]

        for i, img in enumerate(self.imgs):
            row, col = divmod(i, 4)
            img_name = img_files[i]
            if img_name == "cancel":
                Button(TopFrame1, width=160, height=60, image=img, command=self.cancel).grid(row=row + 2, column=col, padx=6, pady=4)
            elif img_name == "clear":
                Button(TopFrame1, width=160, height=60, image=img, command=self.clear).grid(row=row + 2, column=col, padx=6, pady=4)
            elif img_name == "enter":
                Button(TopFrame1, width=160, height=60, image=img, command=self.enter_Pin).grid(row=row + 2, column=col, padx=6, pady=4)
            elif img_name in self.num_mapping:
                Button(TopFrame1, width=160, height=60, image=img, command=lambda num=img_name: self.insert_num(num)).grid(row=row + 2, column=col, padx=6, pady=4)

    def insert_num(self, img_file):
        if img_file in self.num_mapping:
            self.pinEntry.insert(END, self.num_mapping[img_file])

    def enter_Pin(self):
        pin = self.pinEntry.get().strip()
        if pin in self.correct_pins:
            self.valid_pin = True
            self.app_state = "MAIN_MENU"
            self.msgArea.delete("1.0", END)
            self.msgArea.insert(END, "\t\tWelcome to iBank ATM\n\n")
            self.show_options()
        else:
            self.msgArea.delete("1.0", END)
            self.msgArea.insert(END, "Invalid PIN. Try again.\n")

    def clear(self):
        self.pinEntry.delete(0, END)
        self.msgArea.delete("1.0", END)
        self.msgArea.insert(END, "Please enter your PIN.\n")

    def cancel(self):
        self.pinEntry.delete(0, END)
        self.msgArea.delete("1.0", END)
        self.msgArea.insert(END, "Operation cancelled. Please enter your PIN again.\n")
        self.valid_pin = False
        self.app_state = "PIN_ENTRY"

    def show_options(self):
        self.msgArea.delete("1.0", END)
        self.msgArea.insert(END, "Please use arrow buttons to navigate:\n\n")
        for option in self.options:
            self.msgArea.insert(END, f"- {option}\n")

    def select_option(self, idx):
        if not self.valid_pin:
            return
        self.current_option = idx
        option = self.options[idx]
        self.msgArea.delete("1.0", END)

        if option == "Cash Withdrawal":
            self.cash_withdrawal()
        elif option == "Deposit":
            self.deposit()
        elif option == "Balance Inquiry":
            self.balance_inquiry()
        elif option == "Funds Transfer":
            self.funds_transfer()
        elif option == "Bill Payment":
            self.bill_payment()
        elif option == "PIN Change":
            self.pin_change()
        elif option == "Statement Printing":
            self.statement_printing()
        elif option == "Language Options":
            self.language_options()

    def cash_withdrawal(self):
        amount = simpledialog.askfloat("Cash Withdrawal", "Enter amount to withdraw:")
        if amount is not None:
            if amount <= self.balance:
                self.balance -= amount
                self.msgArea.insert(END, f"Withdrawal successful. Your balance is: ${self.balance:.2f}\n")
            else:
                self.msgArea.insert(END, "Insufficient balance.\n")
                self.show_options()
        else:
            self.msgArea.insert(END, "Withdrawal cancelled.\n")
            self.show_options()


    def deposit(self):
        self.msgArea.insert(END, "Select account:\n")
        account = self.get_account_selection()
        if account:
            amount = self.get_amount_input("Enter amount to deposit: ")
            if amount:
                self.balance += amount
                self.msgArea.insert(END, f"Deposit successful. New balance: ${self.balance:.2f}\n")

    def balance_inquiry(self):
        self.msgArea.insert(END, f"Your current balance is: ${self.balance:.2f}\n")

    def funds_transfer(self):
        self.msgArea.insert(END, "Select account to transfer from:\n")
        from_account = self.get_account_selection()
        if from_account:
            to_account = self.get_account_input("Enter recipient account number: ")
            amount = self.get_amount_input("Enter amount to transfer: ")
            if amount and amount <= self.balance:
                self.balance -= amount
                self.msgArea.insert(END, f"${amount} has been transferred successfully.\n")
                self.msgArea.insert(END, f"Remaining balance: ${self.balance:.2f}\n")
            else:
                self.msgArea.insert(END, "Insufficient balance or invalid amount.\n")

    def bill_payment(self):
        self.msgArea.insert(END, "Select bill type:\n")
        bill_type = self.get_bill_type_selection()
        if bill_type:
            amount = self.get_amount_input("Enter amount to pay: ")
            if amount and amount <= self.balance:
                self.balance -= amount
                self.msgArea.insert(END, f"Bill of ${amount} paid successfully.\n")
            else:
                self.msgArea.insert(END, "Insufficient balance or invalid amount.\n")

    def pin_change(self):
        old_pin = self.get_pin_input("Enter old PIN: ")
        if old_pin in self.correct_pins:
            new_pin = self.get_pin_input("Enter new PIN: ")
            if new_pin:
                self.correct_pins.add(new_pin)
                self.correct_pins.remove(old_pin)
                self.msgArea.insert(END, "PIN changed successfully.\n")
            else:
                self.msgArea.insert(END, "PIN change failed.\n")
        else:
            self.msgArea.insert(END, "Invalid old PIN.\n")

    def statement_printing(self):
        self.msgArea.insert(END, "Select account:\n")
        account = self.get_account_selection()
        if account:
            self.msgArea.insert(END, "Statement printed successfully.\n")

    def language_options(self):
        self.language = "French" if self.language == "English" else "English"
        self.msgArea.insert(END, f"Language switched to: {self.language}\n")

    def get_account_selection(self):
        # Simulate account selection
        self.msgArea.insert(END, "Account selected: Checking\n")
        return "Checking"

    def get_amount_input(self, prompt):
        # Simulate amount input
        self.msgArea.insert(END, prompt)
        return 100  # Simulated amount

    def get_account_input(self, prompt):
        # Simulate account input
        self.msgArea.insert(END, prompt)
        return "123456789"  # Simulated account number

    def get_bill_type_selection(self):
        # Simulate bill type selection
        self.msgArea.insert(END, "Bill type selected: Electricity\n")
        return "Electricity"

    def get_pin_input(self, prompt):
        # Simulate PIN input
        self.msgArea.insert(END, prompt)
        return "4321"  # Simulated PIN

# === Lancer l'application ===
if __name__ == "__main__":
    root = Tk()
    app = ATM(root)
    root.mainloop()
