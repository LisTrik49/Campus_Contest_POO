import uuid
import json
import os

class Wallet:

    def __init__(self):    
        #créer un unique_id
        self.unique_id = ""
        #créer un balance (c'est a dire le solde du wallet, il contient un nombre)
        self.balance = 100
        #créer un history (qui contient l'historique de toutes les transactions)
        self.history = []

    def generate_unique_id(self):

        self.unique_id = str(uuid.uuid4())

        while (os.path.exists("./content/wallets/" + self.unique_id + ".json")):
            self.unique_id = str(uuid.uuid4())
        self.save()
        return self.unique_id


    def add_balance(self,amount):

        self.balance += amount
        self.send("Credit : " + str(amount))
        self.save()

        #cette fonction ajoute un montant à l'attribut balance

    
    def sub_balance(self,amount):

        if self.balance >= amount:
            self.balance -= amount
            self.send("Debit : " + str(amount))
            self.save()
        else:
            return False

        #cette fonction retire un montant à l'attribut balance


    def send(self,transaction):

        self.history.append(transaction)

        #cette fonction ajoute la transaction à l'attribut history
        

    def save(self):

        donnees = {"id": self.unique_id,
                   "balance": self.balance,
                   "history": self.history
                    }
        with open("content/wallets/" + self.unique_id + ".json", "w") as file:
            json.dump(donnees, file)

        #il faut enregistrer le wallet au format json dans le dossier content/wallets avec
        #pour nom l'id unique du wallet

    def load(self, wallet_id):

        if (os.path.exists("./content/wallets/" + self.unique_id + ".json")):
            with open("content/wallets/" + wallet_id + ".json", "r") as read_file:
                data = json.load(read_file)
        else:
            data = "Ce portefeuille n'existe pas."
        return data

        #il faut ici pouvoir charger les informations d'un wallet grâce à son id