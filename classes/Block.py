class Block:

    #Un block doit contenir un nom, une taille inférieure a 256Ko, un parent et une
    #liste de transactions

    #Les attributs à mettre en place sont la base_hash, le hash, le parent_hash, les transactions

    def check_hash():

        pass

        #vérifie que le hash est correct en fonction du base_hash


    def add_transaction():

        pass

        #Methode qui ajoute une transaction au block, la transaction concerne un wallet
        #emetteur et un wallet récepteur et doit contenir un montant


    def get_transaction():

        pass

        #Cette méthode récupère une transaction par rapport à son numéro


    def get_weight():

        pass

        #Cette méthode récupère le poids total du bloc

    
    def save():

        pass

        #il faut enregistrer le block au format json dans le dossier content/blocs avec
        #pour nom l'id unique du block

    
    def load():

        pass

        #il faut ici pouvoir charger les informations d'un block grâce à son id