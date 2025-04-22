import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

class ATM:
    def __init__(self, root):
        self.root = root
        self.valid_pin = False
        self.correct_pins = { "0000", "4321"}
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

        self.translations = {
            "English": {
                "welcome": "Welcome to iBank ATM",
                "enter_pin": "Please enter your PIN.",
                "invalid_pin": "Invalid PIN. Try again.",
                "select_option": "Please use arrow buttons to navigate:",
                "withdraw_success": "Withdrawal successful.",
                "deposit_success": "Deposit successful.",
                "insufficient_balance": "Insufficient balance.",
                "invalid_amount": "Invalid amount.",
                "current_balance": "Your current balance is:",
                "remaining_balance": "Remaining balance:",
                "enter_amount": "Enter amount:",
                "select_language": "Select language:\n1. English\n2. Arabic\n3. French",
                "language_switched": "Language switched to:",
                "invalid_selection": "Invalid selection.",
                "enter_account": "Enter recipient account number:",
                "transfer_success": "Transfer successful.",
                "bill_paid": "Bill paid successfully.",
                "select_bill": "Select bill to pay:\n1. Electricity\n2. Water\n3. Internet",
                "operation_cancelled": "Operation cancelled. Please enter your PIN again.",
                "statement_printed": "Statement printed successfully.",
                "pin_change_feature": "Feature under construction: PIN Change",
                "summary_withdrawal": "You withdrew",
                "summary_deposit": "You deposited",
                "summary_transfer": "You transferred",
                "summary_bill_payment": "You paid a bill for",
                "options": [
                    "Cash Withdrawal",
                    "Deposit",
                    "Balance Inquiry",
                    "Funds Transfer",
                    "Bill Payment",
                    "PIN Change",
                    "Statement Printing",
                    "Language Options"
                ]
            },
            "Arabic": {
                "welcome": "مرحبًا بك في أتم آي بنك",
                "enter_pin": "الرجاء إدخال الرقم السري الخاص بك.",
                "invalid_pin": "رقم سري خاطئ. حاول مرة أخرى.",
                "select_option": "الرجاء استخدام أزرار السهم للتنقل:",
                "withdraw_success": "تمت عملية السحب بنجاح.",
                "deposit_success": "تمت عملية الإيداع بنجاح.",
                "insufficient_balance": "رصيد غير كافٍ.",
                "invalid_amount": "مبلغ غير صالح.",
                "current_balance": "رصيدك الحالي هو:",
                "remaining_balance": "الرصيد المتبقي:",
                "enter_amount": "أدخل المبلغ:",
                "select_language": "اختر اللغة:\n1. الإنجليزية\n2. العربية\n3. الفرنسية",
                "language_switched": "تم تغيير اللغة إلى:",
                "invalid_selection": "اختيار غير صالح.",
                "enter_account": "أدخل رقم الحساب المستلم:",
                "transfer_success": "تمت عملية التحويل بنجاح.",
                "bill_paid": "تم دفع الفاتورة بنجاح.",
                "select_bill": "اختر الفاتورة للدفع:\n1. الكهرباء\n2. الماء\n3. الإنترنت",
                "operation_cancelled": "تم إلغاء العملية. الرجاء إدخال الرقم السري مرة أخرى.",
                "statement_printed": "تم طباعة الكشف بنجاح.",
                "pin_change_feature": "الميزة قيد الإنشاء: تغيير الرقم السري",
                "summary_withdrawal": "لقد سحبت",
                "summary_deposit": "لقد ودعت",
                "summary_transfer": "لقد حولت",
                "summary_bill_payment": "لقد دفعت فاتورة بقيمة",
                "options": [
                    "سحب نقدي",
                    "إيداع",
                    "استعلام رصيد",
                    "تحويل أموال",
                    "دفع فاتورة",
                    "تغيير الرقم السري",
                    "طباعة كشف حساب",
                    "خيارات اللغة"
                ]
            },
            "French": {
                "welcome": "Bienvenue à iBank ATM",
                "enter_pin": "Veuillez entrer votre PIN.",
                "invalid_pin": "PIN invalide. Réessayez.",
                "select_option": "Veuillez utiliser les boutons fléchés pour naviguer:",
                "withdraw_success": "Retrait réussi.",
                "deposit_success": "Dépôt réussi.",
                "insufficient_balance": "Solde insuffisant.",
                "invalid_amount": "Montant invalide.",
                "current_balance": "Votre solde actuel est:",
                "remaining_balance": "Solde restant:",
                "enter_amount": "Entrez le montant:",
                "select_language": "Sélectionnez la langue:\n1. Anglais\n2. Arabe\n3. Français",
                "language_switched": "Langue changée pour:",
                "invalid_selection": "Sélection invalide.",
                "enter_account": "Entrez le numéro de compte du destinataire:",
                "transfer_success": "Transfert réussi.",
                "bill_paid": "Facture payée avec succès.",
                "select_bill": "Sélectionnez la facture à payer:\n1. Électricité\n2. Eau\n3. Internet",
                "operation_cancelled": "Opération annulée. Veuillez entrer à nouveau votre PIN.",
                "statement_printed": "Relevé imprimé avec succès.",
                "pin_change_feature": "Fonctionnalité en construction: Changement de PIN",
                "summary_withdrawal": "Vous avez retiré",
                "summary_deposit": "Vous avez déposé",
                "summary_transfer": "Vous avez transféré",
                "summary_bill_payment": "Vous avez payé une facture de",
                "options": [
                    "Retrait d'espèces",
                    "Dépôt",
                    "Solde",
                    "Transfert de fonds",
                    "Paiement de facture",
                    "Changement de PIN",
                    "Impression de relevé",
                    "Options de langue"
                ]
            }
        }

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
        self.msgArea.insert(END, self.translations[self.language]["enter_pin"] + "\n")

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
                label = Label(TopFrame2Left, text=self.translations[self.language]["options"][i], font=('arial', 12))
                label.grid(row=i, column=1)
            else:
                btn = Button(TopFrame2Right, width=160, height=60, state=NORMAL, image=self.img_arrow_right,
                             command=lambda idx=i: self.select_option(idx))
                btn.grid(row=i - 4, column=0, padx=2, pady=2)
                label = Label(TopFrame2Right, text=self.translations[self.language]["options"][i], font=('arial', 12))
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
                Button(TopFrame1, width=160, height=60, image=img, command=self.enter).grid(row=row + 2, column=col, padx=6, pady=4)
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
            self.msgArea.insert(END, "\t\t" + self.translations[self.language]["welcome"] + "\n\n")
            self.show_options()
        else:
            self.msgArea.delete("1.0", END)
            self.msgArea.insert(END, self.translations[self.language]["invalid_pin"] + "\n")

    def enter(self):
        if self.app_state == "PIN_ENTRY":
            self.enter_Pin()
        elif self.app_state in ["WITHDRAWAL_AMOUNT", "DEPOSIT_AMOUNT", "TRANSFER_AMOUNT", "BILL_PAYMENT_AMOUNT"]:
            self.process_amount_entry()
        elif self.app_state == "LANGUAGE_SELECTION":
            self.process_language_selection()
        elif self.app_state == "TRANSFER_ACCOUNT":
            self.process_transfer_account()
        elif self.app_state == "BILL_PAYMENT":
            self.process_bill_payment()

    def clear(self):
        self.pinEntry.delete(0, END)
        if self.app_state == "PIN_ENTRY":
            self.msgArea.delete("1.0", END)
            self.msgArea.insert(END, self.translations[self.language]["enter_pin"] + "\n")

    def cancel(self):
        self.pinEntry.delete(0, END)
        self.msgArea.delete("1.0", END)
        self.msgArea.insert(END, self.translations[self.language]["operation_cancelled"] + "\n")
        self.valid_pin = False
        self.app_state = "PIN_ENTRY"
        self.pinEntry.config(show='*')

    def show_options(self):
        self.msgArea.delete("1.0", END)
        self.msgArea.insert(END, self.translations[self.language]["select_option"] + "\n\n")
        for option in self.translations[self.language]["options"]:
            self.msgArea.insert(END, f"- {option}\n")

    def select_option(self, idx):
        if not self.valid_pin:
            return
        self.current_option = idx
        option = self.translations[self.language]["options"][idx]
        self.msgArea.delete("1.0", END)

        if option == self.translations[self.language]["options"][0]:
            self.cash_withdrawal()
        elif option == self.translations[self.language]["options"][1]:
            self.deposit()
        elif option == self.translations[self.language]["options"][2]:
            self.balance_inquiry()
        elif option == self.translations[self.language]["options"][3]:
            self.funds_transfer()
        elif option == self.translations[self.language]["options"][4]:
            self.bill_payment()
        elif option == self.translations[self.language]["options"][5]:
            self.pin_change()
        elif option == self.translations[self.language]["options"][6]:
            self.statement_printing()
        elif option == self.translations[self.language]["options"][7]:
            self.language_options()

    def cash_withdrawal(self):
        self.msgArea.delete("1.0", END)
        self.msgArea.insert(END, self.translations[self.language]["enter_amount"] + "\n")
        self.pinEntry.delete(0, END)
        self.pinEntry.config(show='')
        self.app_state = "WITHDRAWAL_AMOUNT"

    def process_amount_entry(self):
        amount_str = self.pinEntry.get().strip()
        if self.app_state == "WITHDRAWAL_AMOUNT":
            self.process_withdrawal(amount_str)
        elif self.app_state == "DEPOSIT_AMOUNT":
            self.process_deposit(amount_str)
        elif self.app_state == "TRANSFER_AMOUNT":
            self.process_transfer_amount(amount_str)
        elif self.app_state == "BILL_PAYMENT_AMOUNT":
            self.process_bill_payment_amount(amount_str)

    def process_withdrawal(self, amount_str):
        if amount_str.isdigit():
            amount = float(amount_str)
            if amount <= self.balance:
                self.balance -= amount
                self.msgArea.insert(END, f"{self.translations[self.language]['withdraw_success']} {amount}\n")
                self.msgArea.insert(END, f"{self.translations[self.language]['remaining_balance']} ${self.balance:.2f}\n")
                self.msgArea.insert(END, f"{self.translations[self.language]['summary_withdrawal']} ${amount}. {self.translations[self.language]['current_balance']} ${self.balance:.2f}\n")
            else:
                self.msgArea.insert(END, self.translations[self.language]["insufficient_balance"] + "\n")
        else:
            self.msgArea.insert(END, self.translations[self.language]["invalid_amount"] + "\n")
        self.show_options()
        self.app_state = "MAIN_MENU"
        self.pinEntry.config(show='*')

    def deposit(self):
        self.msgArea.delete("1.0", END)
        self.msgArea.insert(END, self.translations[self.language]["enter_amount"] + "\n")
        self.pinEntry.delete(0, END)
        self.pinEntry.config(show='')
        self.app_state = "DEPOSIT_AMOUNT"

    def process_deposit(self, amount_str):
        if amount_str.isdigit():
            amount = float(amount_str)
            self.balance += amount
            self.msgArea.insert(END, f"{self.translations[self.language]['deposit_success']} {amount}\n")
            self.msgArea.insert(END, f"{self.translations[self.language]['current_balance']} ${self.balance:.2f}\n")
            self.msgArea.insert(END, f"{self.translations[self.language]['summary_deposit']} ${amount}. {self.translations[self.language]['current_balance']} ${self.balance:.2f}\n")
        else:
            self.msgArea.insert(END, self.translations[self.language]["invalid_amount"] + "\n")
        self.show_options()
        self.app_state = "MAIN_MENU"
        self.pinEntry.config(show='*')

    def balance_inquiry(self):
        self.msgArea.insert(END, f"{self.translations[self.language]['current_balance']} ${self.balance:.2f}\n")
        self.show_options()

    def funds_transfer(self):
        self.msgArea.delete("1.0", END)
        self.msgArea.insert(END, self.translations[self.language]["enter_account"] + "\n")
        self.pinEntry.delete(0, END)
        self.pinEntry.config(show='')
        self.app_state = "TRANSFER_ACCOUNT"

    def process_transfer_account(self):
        account = self.pinEntry.get().strip()
        if account:
            self.msgArea.delete("1.0", END)
            self.msgArea.insert(END, f"{self.translations[self.language]['enter_amount']} {account}:\n")
            self.pinEntry.delete(0, END)
            self.app_state = "TRANSFER_AMOUNT"
        else:
            self.msgArea.insert(END, self.translations[self.language]["invalid_amount"] + "\n")
            self.show_options()
            self.app_state = "MAIN_MENU"
            self.pinEntry.config(show='*')

    def process_transfer_amount(self, amount_str):
        if amount_str.isdigit():
            amount = float(amount_str)
            if amount <= self.balance:
                self.balance -= amount
                self.msgArea.insert(END, f"{self.translations[self.language]['transfer_success']} {amount}\n")
                self.msgArea.insert(END, f"{self.translations[self.language]['remaining_balance']} ${self.balance:.2f}\n")
                self.msgArea.insert(END, f"{self.translations[self.language]['summary_transfer']} ${amount}. {self.translations[self.language]['current_balance']} ${self.balance:.2f}\n")
            else:
                self.msgArea.insert(END, self.translations[self.language]["insufficient_balance"] + "\n")
        else:
            self.msgArea.insert(END, self.translations[self.language]["invalid_amount"] + "\n")
        self.show_options()
        self.app_state = "MAIN_MENU"
        self.pinEntry.config(show='*')

    def bill_payment(self):
        self.msgArea.delete("1.0", END)
        self.msgArea.insert(END, self.translations[self.language]["select_bill"] + "\n")
        self.pinEntry.delete(0, END)
        self.pinEntry.config(show='')
        self.app_state = "BILL_PAYMENT"

    def process_bill_payment(self):
        bill_str = self.pinEntry.get().strip()
        if bill_str.isdigit() and 1 <= int(bill_str) <= 3:
            self.msgArea.delete("1.0", END)
            self.msgArea.insert(END, self.translations[self.language]["enter_amount"] + "\n")
            self.pinEntry.delete(0, END)
            self.app_state = "BILL_PAYMENT_AMOUNT"
        else:
            self.msgArea.insert(END, self.translations[self.language]["invalid_selection"] + "\n")
            self.show_options()
            self.app_state = "MAIN_MENU"
            self.pinEntry.config(show='*')

    def process_bill_payment_amount(self, amount_str):
        if amount_str.isdigit():
            amount = float(amount_str)
            if amount <= self.balance:
                self.balance -= amount
                self.msgArea.insert(END, f"{self.translations[self.language]['bill_paid']} {amount}\n")
                self.msgArea.insert(END, f"{self.translations[self.language]['remaining_balance']} ${self.balance:.2f}\n")
                self.msgArea.insert(END, f"{self.translations[self.language]['summary_bill_payment']} ${amount}. {self.translations[self.language]['current_balance']} ${self.balance:.2f}\n")
            else:
                self.msgArea.insert(END, self.translations[self.language]["insufficient_balance"] + "\n")
        else:
            self.msgArea.insert(END, self.translations[self.language]["invalid_amount"] + "\n")
        self.show_options()
        self.app_state = "MAIN_MENU"
        self.pinEntry.config(show='*')

    def change_pin_option(self):
        self.msgArea.delete("1.0", END)
        self.msgArea.insert(END, self.translations[self.language]["enter_pin"] + "\n")
        self.pinEntry.delete(0, END)
        self.pinEntry.config(show='')
        self.app_state = "PIN_CHANGE"

    def change_pin(self):
        new_pin = self.pinEntry.get().strip()
        if len(new_pin) == 4 and new_pin.isdigit():
            self.correct_pins.add(new_pin)
            self.msgArea.insert(END, "PIN changed successfully.\n")
        else:
            self.msgArea.insert(END, "Invalid PIN. Please enter a 4-digit PIN.\n")
        self.show_options()
        self.app_state = "MAIN_MENU"
        self.pinEntry.config(show='*')

    def statement_printing(self):
        self.msgArea.insert(END, self.translations[self.language]["statement_printed"] + "\n")
        self.show_options()
    def print_statement(self):
        # Placeholder for actual statement printing logic
        self.msgArea.insert(END, "Printing your statement...\n")
        self.show_options()
        self.app_state = "MAIN_MENU"

    def language_options(self):
        self.msgArea.delete("1.0", END)
        self.msgArea.insert(END, self.translations[self.language]["select_language"] + "\n")
        self.pinEntry.delete(0, END)
        self.pinEntry.config(show='')
        self.app_state = "LANGUAGE_SELECTION"

    def process_language_selection(self):
        lang_str = self.pinEntry.get().strip()
        if lang_str == "1":
            self.language = "English"
        elif lang_str == "2":
            self.language = "Arabic"
        elif lang_str == "3":
            self.language = "French"
        else:
            self.msgArea.insert(END, self.translations[self.language]["invalid_selection"] + "\n")
            self.language_options()
            return
        self.msgArea.insert(END, f"{self.translations[self.language]['language_switched']} {self.language}\n")
        self.show_options()
        self.app_state = "MAIN_MENU"
        self.pinEntry.config(show='*')

# === Lancer l'application ===
if __name__ == "__main__":
    root = Tk()
    app = ATM(root)
    root.mainloop()
