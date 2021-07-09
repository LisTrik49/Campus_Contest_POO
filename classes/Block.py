import json
import os
import hashlib
from classes.Wallet import Wallet

PATH_TO_BLOCS = "./content/blocs/"
EXT_JSON = ".json"

class Block:

    #Un block doit contenir un nom, une taille inférieure a 256Ko, un parent et une
    #liste de transactions
    def __init__(self):
        
        self.base_hash = ""
        self.hash = "00"
        self.parent_hash = "00"
        self.transactions = []
        self.size = ""

    #Les attributs à mettre en place sont la base_hash, le hash, le parent_hash, les transactions

    def check_hash(self,hash,base_hash):

        self.base_hash = base_hash
        self.hash = hash

        if "0000" + hashlib.sha256(base_hash.encode()).hexdigest() == hash:
            return True
        else:
            return False

        #vérifie que le hash est correct en fonction du base_hash


    def add_transaction(self,block,amount,receiver,transmitter):

        donnees = {"Emetteur": transmitter.unique_id,
                   "Receveur": receiver.unique_id,
                   "Montant": amount}

        self.transactions.append(donnees)
        block.transactions = donnees
        self.save(block.hash)

        if transmitter.sub_balance(amount) == False:
            print("Le portefeuille ne pas effectuer cette transaction")
            transmitter.save()
            receiver.save()
        else:
            transmitter.balance = transmitter.sub_balance(amount)
            transmitter.save()
            receiver.balance = receiver.add_balance(amount)
            receiver.save()


        #Methode qui ajoute une transaction au block, la transaction concerne un wallet
        #emetteur et un wallet récepteur et doit contenir un montant


    def get_weight(self, block_id):

        if (os.path.exists(PATH_TO_BLOCS + block_id + EXT_JSON)):
            self.size = str(os.path.getsize(PATH_TO_BLOCS + block_id + EXT_JSON) / 1024) + " Ko"
            return self.size

        #Cette méthode récupère le poids total du bloc

    
    def save(self,hash):

        donnees = {"hash": hash,
                   "base_hash": self.base_hash,
                   "parent_hash": self.parent_hash,
                   "transactions": self.transactions,
                   "size": self.size}
        with open(PATH_TO_BLOCS + self.hash + EXT_JSON, "w") as file:
            json.dump(donnees, file)

        #il faut enregistrer le block au format json dans le dossier content/blocs avec
        #pour nom l'id unique du block

    
    def load(self, block_id):

        if (os.path.exists(PATH_TO_BLOCS + block_id + EXT_JSON)):
            with open(PATH_TO_BLOCS + block_id + EXT_JSON, "r") as read_file:
                data = json.load(read_file)
        else:
            data = "Ce block n'existe pas."
        return data

        #il faut ici pouvoir charger les informations d'un block grâce à son id