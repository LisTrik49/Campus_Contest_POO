import json
from classes.Wallet import Wallet

wallet1 = Wallet()
id = wallet1.generate_unique_id()
print(id)
wallet1.add_balance(10)
print(wallet1.balance, wallet1.history)