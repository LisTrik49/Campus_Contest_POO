from classes.Block import Block
import uuid
import hashlib
import json

class Chain:

    def __init__(self):
    
        #créer l'attribut blocks (liste des blocs au sein de la chaine)
        self.blocks = []
        #créer l'attribut last_transaction_number (dernier num de transaction enregistré)
        self.last_transaction_number = ""

    def generate_hash(self):

        hash = hashlib.sha256(self.blocks.encode()).hexdigest() #remplacer le a par la chaine
        return hash


    def verify_hash(self):

        hash = self.generate_hash()

        keys = json.loads("content/blocs/blocs.json")

        if hash in keys or hash[:4] != "0000":
            return "Le hash ne correspond pas aux critères."
        else:
            return hash

        #methode qui vérifie si un hash correspond aux critères de la chaine à savoir
        #le hash ne doit pas déja exister, et le hash doit commencer par 0000


    def add_block(self):

        

        pass

        #methode qui crée un block, une fois un hash trouvé, on utilise cette méthode
        #on enregistre alors le block dans la chaine grace à la méthode save créée
        #dans la classe block, il faut vérifier que le block n'existe pas déja


    def get_block(self):

        pass

        #On va juste récupérer un block en fonction de son hash

    
    def add_transaction(self):

        pass
        
        #On ajoute une transaction à un block


    def verify_wallet_exists(self):

        pass

        #Il faut vérifier que les wallets de l'émetteur et du récepteur existent

    
    def verify_wallet_has_enough(self):

        pass

        #Vérifie que le wallet a assez de fonds pour effectuer la transaction

    
    def verify_can_write_transaction_on_block(self):

        pass

        #Vérifie qu'on peut écrire la transaction sur un block


    def find_transaction(self):

        pass

        #Elle doit retourner l'objet Block dans lequel se trouve la transaction demandé en
        #paramètre

    
    def get_last_transaction_number(self):

        pass

        #Elle retourne la dernière transaction réalisée
        #Faire un système de last_insert_transaction