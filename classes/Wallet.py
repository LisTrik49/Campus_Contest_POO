import uuid
import json
import os

PATH_TO_WALLETS = "./content/wallets/"
EXT_JSON = ".json"


class Wallet:

    def __init__(self):
        # créer un unique_id
        self.unique_id = ""
        # créer un balance (c'est a dire le solde du wallet
        # il contient un nombre)
        self.balance = 100
        # créer un history (qui contient l'historique de toutes
        # les transactions)
        self.history = []

    def generate_unique_id(self):

        self.unique_id = str(uuid.uuid4())

        while (os.path.exists(PATH_TO_WALLETS + self.unique_id + EXT_JSON)):
            self.unique_id = str(uuid.uuid4())
        self.save()
        return self.unique_id

    def verify_wallet_exists(self):

        if (os.path.exists(PATH_TO_WALLETS + self.unique_id + EXT_JSON)):
            return True
        else:
            return False

    def add_balance(self, amount):

        if self.verify_wallet_exists():
            self.balance += amount
            self.send("Credit : " + str(amount))
            return self.balance

        # cette fonction ajoute un montant à l'attribut balance

    def sub_balance(self, amount):

        if self.balance >= amount and self.verify_wallet_exists():
            self.balance -= amount
            self.send("Debit : " + str(amount))
            return self.balance
        else:
            return False

        # cette fonction retire un montant à l'attribut balance

    def send(self, transaction):

        self.history.append(transaction)

        # cette fonction ajoute la transaction à l'attribut history

    def save(self):

        donnees = {"id": self.unique_id,
                   "balance": self.balance,
                   "history": self.history}
        with open(PATH_TO_WALLETS + self.unique_id + EXT_JSON, "w") as file:
            json.dump(donnees, file)

        # il faut enregistrer le wallet au format json dans
        # le dossier content/wallets avec pour nom l'id unique du wallet

    def load(self, wallet_id):

        if (os.path.exists(PATH_TO_WALLETS + self.unique_id + EXT_JSON)):
            with open(PATH_TO_WALLETS + wallet_id + EXT_JSON, "r") as read_file:
                data = json.load(read_file)
        else:
            data = "Ce portefeuille n'existe pas."
        return data

        # il faut ici pouvoir charger les informations
        # d'un wallet grâce à son id