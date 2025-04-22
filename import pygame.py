accounts_db = {
    "1234": {"pin": "0000", "balance": 1000.0},
    "5678": {"pin": "1234", "balance": 500.0},
}

class ATMLogic:
    def __init__(self, atm_ui):
        self.ui = atm_ui
        self.input = ""
        self.state = "ACCOUNT"  # ou PIN, MENU, WITHDRAW, DEPOSIT
        self.current_account = None

        self.setup_bindings()
        self.display("Bienvenue\nEntrez votre numéro de compte:")

    def display(self, text):
        self.ui.txtReceeipt.delete("1.0", "end")
        self.ui.txtReceeipt.insert("end", text)

    def setup_bindings(self):
        for i in range(10):
            btn = getattr(self.ui, f"btn{i}", None)
            if btn:
                btn_widget = self.ui.root.nametowidget(str(btn))
                btn_widget.configure(command=lambda d=i: self.press(str(d)))

        self.ui.root.nametowidget(str(self.ui.btnEnter)).configure(command=self.validate)
        self.ui.root.nametowidget(str(self.ui.btnC1)).configure(command=self.clear)
        self.ui.root.nametowidget(str(self.ui.btnCE)).configure(command=self.cancel)

    def press(self, value):
        self.input += value
        self.display(self.input)

    def clear(self):
        self.input = ""
        self.display("Champ effacé.")

    def cancel(self):
        self.input = ""
        self.current_account = None
        self.state = "ACCOUNT"
        self.display("Opération annulée.\nEntrez votre numéro de compte:")

    def validate(self):
        if self.state == "ACCOUNT":
            if self.input in accounts_db:
                self.current_account = self.input
                self.input = ""
                self.state = "PIN"
                self.display("Entrez le code PIN :")
            else:
                self.display("Compte invalide. Essayez encore :")
                self.input = ""

        elif self.state == "PIN":
            if self.input == accounts_db[self.current_account]["pin"]:
                self.state = "MENU"
                self.input = ""
                self.show_menu()
            else:
                self.display("PIN incorrect. Réessayez :")
                self.input = ""

        elif self.state == "MENU":
            if self.input == "1":
                solde = accounts_db[self.current_account]["balance"]
                self.display(f"Solde actuel : {solde:.2f} €")
            elif self.input == "2":
                self.state = "WITHDRAW"
                self.display("Montant à retirer :")
            elif self.input == "3":
                self.state = "DEPOSIT"
                self.display("Montant à déposer :")
            elif self.input == "4":
                self.cancel()
            else:
                self.display("Option invalide.")
            self.input = ""

        elif self.state == "WITHDRAW":
            try:
                amount = float(self.input)
                if amount <= accounts_db[self.current_account]["balance"]:
                    accounts_db[self.current_account]["balance"] -= amount
                    self.display(f"Retrait de {amount:.2f} € réussi.")
                else:
                    self.display("Fonds insuffisants.")
            except:
                self.display("Montant invalide.")
            self.input = ""
            self.state = "MENU"
            self.show_menu()

        elif self.state == "DEPOSIT":
            try:
                amount = float(self.input)
                accounts_db[self.current_account]["balance"] += amount
                self.display(f"Dépôt de {amount:.2f} € réussi.")
            except:
                self.display("Montant invalide.")
            self.input = ""
            self.state = "MENU"
            self.show_menu()

    def show_menu(self):
        self.display("Menu principal :\n1. Solde\n2. Retrait\n3. Dépôt\n4. Déconnexion")# --- Module logique : Fonctionnalité ATM dynamique ---

# Base de données simulée
accounts_db = {
    "1234": {"pin": "0000", "balance": 1000.0},
    "5678": {"pin": "1234", "balance": 500.0},
}

class ATMLogic:
    def __init__(self, atm_ui):
        self.ui = atm_ui
        self.input = ""
        self.state = "ACCOUNT"  # ou PIN, MENU, WITHDRAW, DEPOSIT
        self.current_account = None

        self.setup_bindings()
        self.display("Bienvenue\nEntrez votre numéro de compte:")

    def display(self, text):
        self.ui.txtReceeipt.delete("1.0", "end")
        self.ui.txtReceeipt.insert("end", text)

    def setup_bindings(self):
        for i in range(10):
            btn = getattr(self.ui, f"btn{i}", None)
            if btn:
                btn_widget = self.ui.root.nametowidget(str(btn))
                btn_widget.configure(command=lambda d=i: self.press(str(d)))

        self.ui.root.nametowidget(str(self.ui.btnEnter)).configure(command=self.validate)
        self.ui.root.nametowidget(str(self.ui.btnC1)).configure(command=self.clear)
        self.ui.root.nametowidget(str(self.ui.btnCE)).configure(command=self.cancel)

    def press(self, value):
        self.input += value
        self.display(self.input)

    def clear(self):
        self.input = ""
        self.display("Champ effacé.")

    def cancel(self):
        self.input = ""
        self.current_account = None
        self.state = "ACCOUNT"
        self.display("Opération annulée.\nEntrez votre numéro de compte:")

    def validate(self):
        if self.state == "ACCOUNT":
            if self.input in accounts_db:
                self.current_account = self.input
                self.input = ""
                self.state = "PIN"
                self.display("Entrez le code PIN :")
            else:
                self.display("Compte invalide. Essayez encore :")
                self.input = ""

        elif self.state == "PIN":
            if self.input == accounts_db[self.current_account]["pin"]:
                self.state = "MENU"
                self.input = ""
                self.show_menu()
            else:
                self.display("PIN incorrect. Réessayez :")
                self.input = ""

        elif self.state == "MENU":
            if self.input == "1":
                solde = accounts_db[self.current_account]["balance"]
                self.display(f"Solde actuel : {solde:.2f} €")
            elif self.input == "2":
                self.state = "WITHDRAW"
                self.display("Montant à retirer :")
            elif self.input == "3":
                self.state = "DEPOSIT"
                self.display("Montant à déposer :")
            elif self.input == "4":
                self.cancel()
            else:
                self.display("Option invalide.")
            self.input = ""

        elif self.state == "WITHDRAW":
            try:
                amount = float(self.input)
                if amount <= accounts_db[self.current_account]["balance"]:
                    accounts_db[self.current_account]["balance"] -= amount
                    self.display(f"Retrait de {amount:.2f} € réussi.")
                else:
                    self.display("Fonds insuffisants.")
            except:
                self.display("Montant invalide.")
            self.input = ""
            self.state = "MENU"
            self.show_menu()

        elif self.state == "DEPOSIT":
            try:
                amount = float(self.input)
                accounts_db[self.current_account]["balance"] += amount
                self.display(f"Dépôt de {amount:.2f} € réussi.")
            except:
                self.display("Montant invalide.")
            self.input = ""
            self.state = "MENU"
            self.show_menu()

    def show_menu(self):
        self.display("Menu principal :\n1. Solde\n2. Retrait\n3. Dépôt\n4. Déconnexion")
