class Block:

    #Un block doit contenir un nom, une taille inférieure a 256Ko, un parent et une
    #liste de transactions
    def __init__(self):
        
        self.base_hash = ""
        self.hash = ""
        self.parent_hash = ""
        self.transactions = ""


    #Les attributs à mettre en place sont la base_hash, le hash, le parent_hash, les transactions

    def check_hash(self):

        pass

        #vérifie que le hash est correct en fonction du base_hash


    def add_transaction(self):

        pass

        #Methode qui ajoute une transaction au block, la transaction concerne un wallet
        #emetteur et un wallet récepteur et doit contenir un montant


    def get_transaction(self):

        pass

        #Cette méthode récupère une transaction par rapport à son numéro


    def get_weight(self):

        pass

        #Cette méthode récupère le poids total du bloc

    
    def save(self):

        pass

        #il faut enregistrer le block au format json dans le dossier content/blocs avec
        #pour nom l'id unique du block

    
    def load(self):

        pass

        #il faut ici pouvoir charger les informations d'un block grâce à son id