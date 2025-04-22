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
            self.msgArea.insert(END, f"Withdrawal successful. Your balance is: ${self.balance:.2f}\n")
        elif option == "Deposit":
            self.balance += 100  # simulate deposit
            self.msgArea.insert(END, "You have deposited $100.\n")
            self.msgArea.insert(END, f"New balance: ${self.balance:.2f}\n")
        elif option == "Balance Inquiry":
            self.msgArea.insert(END, f"Your current balance is: ${self.balance:.2f}\n")
        elif option == "Funds Transfer":
            
            self.balance -= 50  # simulate transfer
            self.msgArea.insert(END, "$50 has been transferred successfully.\n")
            self.msgArea.insert(END, f"Remaining balance: ${self.balance:.2f}\n")
        elif option == "Bill Payment":
            self.balance -= 30
            self.msgArea.insert(END, "Bill of $30 paid successfully.\n")
        elif option == "PIN Change":
            self.msgArea.insert(END, "Feature under construction: PIN Change\n")
        elif option == "Statement Printing":
            self.msgArea.insert(END, "Statement printed successfully.\n")
        elif option == "Language Options":
            self.language = "French" if self.language == "English" else "English"
            self.msgArea.insert(END, f"Language switched to: {self.language}\n")

# === Lancer l'application ===
if __name__ == "__main__":
    root = Tk()
    app = ATM(root)
    root.mainloop()
