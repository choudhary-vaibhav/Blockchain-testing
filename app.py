import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="Awesome.", proof=100)


    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block


    @property
    def last_block(self):
 
        return self.chain[-1]


    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1


    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

def transaction(last_proof):
    global blockchain
    sender = input("Sender: ")
    recipient = input("Recipient: ")
    amount = input("Amount: ")

    blockchain.new_transaction(sender, recipient, amount)
    blockchain.new_block(last_proof+2)

    return last_proof+2


print("BLOCKTIV")

blockchain = Blockchain()

with open('chain.json', 'r') as f:
    json_data = json.load(f)
    blockchain.chain = json_data

    for dict in json_data:
        proof = dict['proof']

ans = 'Y'

while ans == 'Y' or ans == 'y':
    proof = transaction(proof)

    ans = input("Do you want to continue(Y/N):")

print("Genesis block: ", blockchain.chain)

json_object = json.dumps(blockchain.chain, indent = 4)

with open('chain.json', 'w') as f:
    f.write(json_object)
