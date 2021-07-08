import uuid
import json
import os

class Wallet:

    def __init__(self):    
        #créer un unique_id
        self.unique_id = "tr23EHFH"
        #créer un balance (c'est a dire le solde du wallet, il contient un nombre)
        self.balance = 100
        #créer un history (qui contient l'historique de toutes les transactions)
        self.history = []

    def generate_unique_id(self):

        self.unique_id = str(uuid.uuid4())

        while (os.path.exists("./content/wallets/" + self.unique_id + ".json")):
            self.unique_id = str(uuid.uuid4())
        return self.unique_id


    def add_balance(self,amount):

        self.balance += amount
        self.send("Le portefeuille d'id " + self.unique_id + " a recu un montant de " + amount)

        #cette fonction ajoute un montant à l'attribut balance

    
    def sub_balance(self,amount):

        if self.balance >= amount:
            self.balance -= amount
            self.send("Le portefeuille d'id " + self.unique_id + " a été débité d'un montant de " + amount)
        else:
            return "Le portefeuille ne dispose pas des fonds nécessaires à la transaction."

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

    #def load(self):

    #    pass

        #il faut ici pouvoir charger les informations d'un wallet grâce à son id