import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter import *

class ATM:
    def __init__(self, root):
        self.root = root
        self.valid_pin = False
        self.correct_pins = {"1234", "0000", "4321"}
        self.current_pin = None
        self.app_state = "PIN_ENTRY"
        self.current_option = 0
        self.language = "English"
        self.balance = 1000.0
        self.transactions = []  # list of (type, detail, amount)
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

        self.setup_ui()

    def setup_ui(self):
        self.root.title(" " * 110 + "ATM System")
        self.root.geometry("774x760+280+0")
        self.root.configure(background='gainsboro')

        # Main frames
        MainFrame = Frame(self.root, bd=20, width=784, height=700, relief=RIDGE)
        MainFrame.grid()
        self.TopFrame1 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        self.TopFrame1.grid(row=1, column=0, padx=12)
        TopFrame2 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame2.grid(row=0, column=0, padx=8)
        self.LeftFrame = Frame(TopFrame2, bd=7, width=190, height=300, relief=RIDGE)
        self.LeftFrame.grid(row=0, column=0, padx=3)
        MidFrame = Frame(TopFrame2, bd=7, width=200, height=300, relief=RIDGE)
        MidFrame.grid(row=0, column=1, padx=3)
        self.RightFrame = Frame(TopFrame2, bd=7, width=190, height=300, relief=RIDGE)
        self.RightFrame.grid(row=0, column=2, padx=3)

        # Message area and PIN entry
        self.msgArea = Text(MidFrame, height=10, width=42, bd=12, font=('arial', 9, 'bold'))
        self.msgArea.grid(row=0, column=0)
        self.msgArea.insert(END, "Please enter your PIN.\n")
        self.pinEntry = Entry(MidFrame, font=('arial', 18, 'bold'), bd=12,
                              width=25, justify='center', show='*')
        self.pinEntry.grid(row=1, column=0)

        # Arrow buttons
        self.img_arrow_left = PhotoImage(file="ATM_Icon/lArrow.png")
        self.img_arrow_right = PhotoImage(file="ATM_Icon/rArrow.png")
        for i, option in enumerate(self.options):
            frame = self.LeftFrame if i < 4 else self.RightFrame
            row = i if i < 4 else i - 4
            img = self.img_arrow_left if i < 4 else self.img_arrow_right
            btn = Button(frame, width=160, height=60, image=img,
                         command=lambda idx=i: self.select_option(idx))
            btn.grid(row=row, column=0, padx=2, pady=2)
            Label(frame, text=option, font=('arial', 12)).grid(row=row, column=1)

        # Numeric keypad and actions
        img_files = [
            "one", "two", "three", "cancel",
            "four", "five", "six", "clear",
            "seven", "eight", "nine", "enter",
            "empty", "zero", "empty", "empty"
        ]
        self.num_mapping = {name: str(i+1) for i, name in enumerate(img_files) if name.isalpha() and name != 'empty'}
        self.imgs = [PhotoImage(file=f"ATM_Icon/{img}.png") for img in img_files]
        for i, img in enumerate(self.imgs):
            row, col = divmod(i, 4)
            name = img_files[i]
            cmd = None
            if name == 'cancel': cmd = self.cancel
            elif name == 'clear': cmd = self.clear
            elif name == 'enter': cmd = self.enter_Pin
            elif name in self.num_mapping: cmd = lambda n=name: self.insert_num(n)
            if cmd:
                Button(self.TopFrame1, width=160, height=60, image=img,
                       command=cmd).grid(row=row+2, column=col, padx=6, pady=4)

    def insert_num(self, img_file):
        self.pinEntry.insert(END, self.num_mapping[img_file])

    def enter_Pin(self):
        pin = self.pinEntry.get().strip()
        if pin in self.correct_pins:
            self.valid_pin = True
            self.current_pin = pin
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
        self.clear()
        self.valid_pin = False
        self.app_state = "PIN_ENTRY"

    def show_options(self):
        self.msgArea.delete("1.0", END)
        self.msgArea.insert(END, "Select an option:\n\n")
        for opt in self.options:
            self.msgArea.insert(END, f"- {opt}\n")

    def select_option(self, idx):
        if not self.valid_pin: return
        name = self.options[idx].lower().replace(' ', '_')
        func = getattr(self, name, None)
        self.msgArea.delete("1.0", END)
        if func:
            func()
        else:
            self.msgArea.insert(END, "Option not implemented.\n")

    # Option methods below:
    def cash_withdrawal(self):
        amt = simpledialog.askfloat("Cash Withdrawal", "Enter amount to withdraw:")
        if amt is None: return
        if amt <= 0 or amt > self.balance:
            messagebox.showerror("Error", "Invalid or insufficient funds.")
            return
        self.balance -= amt
        self.transactions.append(('Withdrawal', '', amt))
        self.msgArea.insert(END, f"Withdrawal of ${amt:.2f} successful.\nNew balance: ${self.balance:.2f}\n")

    def deposit(self):
        amt = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
        if amt is None or amt <= 0: return
        self.balance += amt
        self.transactions.append(('Deposit', '', amt))
        self.msgArea.insert(END, f"Deposit of ${amt:.2f} successful.\nNew balance: ${self.balance:.2f}\n")

    def balance_inquiry(self):
        self.transactions.append(('Balance Inquiry', '', 0))
        self.msgArea.insert(END, f"Current balance: ${self.balance:.2f}\n")

    def funds_transfer(self):
        to_acc = simpledialog.askstring("Funds Transfer", "Enter destination account:")
        if not to_acc: return
        amt = simpledialog.askfloat("Funds Transfer", "Enter amount to transfer:")
        if amt is None or amt <= 0 or amt > self.balance:
            messagebox.showerror("Error", "Invalid amount or insufficient funds.")
            return
        confirm = messagebox.askyesno("Confirm Transfer",
            f"Transfer ${amt:.2f} to {to_acc}?" )
        if not confirm: return
        self.balance -= amt
        self.transactions.append(('Transfer', to_acc, amt))
        self.msgArea.insert(END, f"Transferred ${amt:.2f} to {to_acc}.\nRemaining balance: ${self.balance:.2f}\n")

    def bill_payment(self):
        bill = simpledialog.askstring("Bill Payment", "Enter bill type (e.g. electricity, water):")
        if not bill: return
        ref = simpledialog.askstring("Bill Payment", "Enter reference number:")
        if not ref: return
        amt = simpledialog.askfloat("Bill Payment", "Enter amount to pay:")
        if amt is None or amt <= 0 or amt > self.balance:
            messagebox.showerror("Error", "Invalid amount or insufficient funds.")
            return
        confirm = messagebox.askyesno("Confirm Payment",
            f"Pay {amt:.2f} for {bill} (ref: {ref})?")
        if not confirm: return
        self.balance -= amt
        self.transactions.append(('Bill Payment', bill+" #"+ref, amt))
        self.msgArea.insert(END, f"Bill '{bill}' paid: ${amt:.2f}.\nNew balance: ${self.balance:.2f}\n")

    def pin_change(self):
        new_pin = simpledialog.askstring("PIN Change", "Enter new PIN:", show='*')
        if not new_pin: return
        confirm_pin = simpledialog.askstring("PIN Change", "Confirm new PIN:", show='*')
        if new_pin != confirm_pin:
            messagebox.showerror("Error", "PINs do not match.")
            return
        # update set
        self.correct_pins.discard(self.current_pin)
        self.correct_pins.add(new_pin)
        self.current_pin = new_pin
        messagebox.showinfo("Success", "PIN changed successfully.")
        self.msgArea.insert(END, "PIN updated.\n")

    def statement_printing(self):
        if not self.transactions:
            self.msgArea.insert(END, "No transactions yet.\n")
            return
        self.msgArea.insert(END, "--- Statement ---\n")
        for t in self.transactions[-10:]:
            typ, detail, amt = t
            line = f"{typ} {detail} ${amt:.2f}\n" if amt else f"{typ}\n"
            self.msgArea.insert(END, line)

    def language_options(self):
        lang = simpledialog.askstring("Language Options",
            "Enter language (English/French/Arabic):")
        if lang and lang.lower() in ['english','french','arabic']:
            self.language = lang.title()
            self.msgArea.insert(END, f"Language set to {self.language}\n")
        else:
            messagebox.showerror("Error", "Unsupported language.")

# === Lancer l'application ===
if __name__ == "__main__":
    root = Tk()
    app = ATM(root)
    root.mainloop()
