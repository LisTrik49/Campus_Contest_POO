import json
from classes.Wallet import Wallet

wallet1 = Wallet()
id = wallet1.generate_unique_id()
print(id)
wallet1.save()