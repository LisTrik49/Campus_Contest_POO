import hashlib
import json
import random
import os
from classes.Block import Block

PATH_TO_BLOCS = "./content/blocs/"
PATH_TO_WALLETS = "./content/wallets/"
EXT_JSON = ".json"

class Chain:

    def __init__(self):
    
        block1 = Block()
        block1.save(block1.hash)
        #créer l'attribut blocks (liste des blocs au sein de la chaine)
        self.blocks = [block1]
        #créer l'attribut last_transaction_number (dernier num de transaction enregistré)
        self.last_transaction_number = ""

    def create_string(self):

        string = random.randint(0,1000000000000000000000000000000000)
        return str(string)


    def generate_hash(self):

        string = self.create_string()
        hash = hashlib.sha256(string.encode()).hexdigest()

        while not(self.verify_hash(hash)):
            string = self.create_string()
            hash = hashlib.sha256(string.encode()).hexdigest() #remplacer le a par la chaine
            print(hash)
        
        block = Block()
        block.base_hash = string
        block.hash = hash

        return block


    def verify_hash(self,hash):

        if (os.path.exists(PATH_TO_BLOCS + hash + EXT_JSON)) or hash[:4] != "0000":
            return False
        else:
            return True

        #methode qui vérifie si un hash correspond aux critères de la chaine à savoir
        #le hash ne doit pas déja exister, et le hash doit commencer par 0000


    def get_parent_hash(self,block):

        block.parent_hash = self.blocks[-1].hash
        return block.parent_hash

    def add_block(self, block):

        block.parent_hash = self.get_parent_hash(block)
        block.save(block.hash)
        self.blocks.append(block)

        #methode qui crée un block, une fois un hash trouvé, on utilise cette méthode
        #on enregistre alors le block dans la chaine grace à la méthode save créée
        #dans la classe block, il faut vérifier que le block n'existe pas déja


    def get_block(self, hash):

        if (os.path.exists(PATH_TO_BLOCS + hash + EXT_JSON)):
            with open(PATH_TO_BLOCS + hash + EXT_JSON, "r") as read_file:
                data = json.load(read_file)
        else:
            data = "Ce block n'existe pas."
        return data

        # On va juste récupérer un block en fonction de son hash