import tkinter as tk
from tkinter import *

class ATM:
    def __init__(self, root):
        self.root = root
        self.valid_pin = False
        self.correct_pins = {"1234", "0000", "4321"}
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
        
        self.root.title("ATM System")
        self.root.geometry("774x760+280+0")
        self.root.configure(background='gainsboro')
        self.create_widgets()

    def create_widgets(self):
        # Création des widgets (comme dans votre code précédent)
        # ...

     def show_language_options(self):
        self.msgArea.delete("1.0", tk.END)
        self.msgArea.insert(tk.END, "Select a language:\n")
        self.msgArea.insert(tk.END, "1: English\n")
        self.msgArea.insert(tk.END, "2: French\n")
        self.msgArea.insert(tk.END, "3: Arabic\n")

    def select_language(self, option):
        languages = {
            "1": "English",
            "2": "French",
            "3": "Arabic"
        }
        
        if option in languages:
            self.language = languages[option]
            self.msgArea.insert(tk.END, f"Language switched to: {self.language}\n")
        else:
            self.msgArea.insert(tk.END, "Invalid option. Please select a valid language.\n")

    def select_option(self, idx):
        if not self.valid_pin:
            return
        option = self.options[idx]
        self.msgArea.delete("1.0", tk.END)

        if option == "Language Options":
            self.show_language_options()
        elif option == "Cash Withdrawal":
            amount = 100
            self.withdraw(amount)
        elif option == "Deposit":
            amount = 100
            self.deposit(amount)
        # Ajoutez d'autres options ici

# Exécutez l'application
if __name__ == "__main__":
    root = Tk()
    app = ATM(root)
    root.mainloop()