import uuid
import hashlib

class Chain:

    #créer l'attribut blocks (liste des blocs au sein de la chaine)
    #créer l'attribut last_transaction_number (dernier num de transaction enregistré)

    def generate_hash():

        hash = hashlib.sha256("a".encode()).hexdigest() #remplacer le a par la chaine


    def verify_hash():

        pass

        #methode qui vérifie si un hash correspond aux critères de la chaine à savoir
        # le hash ne doit pas déja exister, et le hash doit commencer par 0000


    def add_block():

        pass

        #methode qui crée un block, une fois un hash trouvé, on utilise cette méthode
        #on enregistre alors le block dans la chaine grace à la méthode save créée
        #dans la classe block, il faut vérifier que le block n'existe pas déja


    def get_block():

        pass

        #On va juste récupérer un block en fonction de son hash

    
    def add_transaction():

        pass
        
        #On ajoute une transaction à un block


    def verify_wallet_exists():

        pass

        #Il faut vérifier que les wallets de l'émetteur et du récepteur existent

    
    def verify_wallet_has_enough():

        pass

        #Vérifie que le wallet a assez de fonds pour effectuer la transaction

    
    def verify_can_write_transaction_on_block():

        pass

        #Vérifie qu'on peut écrire la transaction sur un block


    def find_transaction():

        pass

        #Elle doit retourner l'objet Block dans lequel se trouve la transaction demandé en
        #paramètre

    
    def get_last_transaction_number():

        pass

        #Elle retourne la dernière transaction réalisée
        #Faire un système de last_insert_transaction