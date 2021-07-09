import json
from classes.Wallet import Wallet
from classes.Chain import Chain

# wallet1 = Wallet()
# wallet2 = Wallet()
# id = wallet1.generate_unique_id()
# id2 = wallet2.generate_unique_id()
# print(id)
# print(id2)
# if wallet2.sub_balance(3) != False:
#     wallet1.add_balance(3)
# else:
#     print("Le portefeuille ne dispose pas des fonds nécessaires")

# if wallet1.sub_balance(24) != False:
#     wallet2.add_balance(24)
# else:
#     print("Le portefeuille ne dispose pas des fonds nécessaires")

# print(wallet1.load(id))
# print(wallet2.load(id2))

chain1 = Chain()
chain1.generate_hash()
