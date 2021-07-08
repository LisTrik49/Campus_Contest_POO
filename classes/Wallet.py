import uuid
import hashlib

class Wallet:

    #créer un unique_id
    unique_id = ""
    #créer un balance (c'est a dire le solde du wallet, il contient un nombre)
    balance = 100
    #créer un history (qui contient l'historique de toutes les transactions)
    history = []

    def generate_unique_id(unique_id):

        unique_id = uuid.uuid4()

        #penser a faire une vérification comme quoi l'id n'existe pas déja


    def add_balance():

        pass

        #cette fonction ajoute un montant à l'attribut balance

    
    def sub_balance():

        pass

        #cette fonction retire un montant à l'attribut balance


    def send():

        pass

        #cette fonction ajoute la transaction à l'attribut history
        

    def save():

        pass

        #il faut enregistrer le wallet au format json dans le dossier content/wallets avec
        #pour nom l'id unique du wallet

    def load():

        pass

        #il faut ici pouvoir charger les informations d'un wallet grâce à son id