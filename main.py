from classes.Chain import Chain
from classes.Wallet import Wallet

chain = Chain()
wallet = Wallet()
wallet2 = Wallet()
amount = 3

id = wallet.generate_unique_id()
id2 = wallet2.generate_unique_id()

for i in range(5):
    block = chain.generate_hash()
    chain.add_block(block)
    block.add_transaction(block, amount, wallet, wallet2)
    print(block.hash)