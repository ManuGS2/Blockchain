import time
import json

from flask import Flask, request
import requests
from Blockchain import Blockchain
from Block import Block

app = Flask(__name__)
peers = set()
blockchain = Blockchain()

@app.route("/new_transaction", methods=["POST"])
def new_transaction():
    txn_data = request.get_json()
    required_fields = ["author", "content"]

    if all(not txn_data.get(field) for field in required_fields):
        return "Invalid transaction data", 404

    txn_data["timestamp"] = time.time()
    blockchain.add_new_transaction(txn_data)

    return "Transaction added", 201


@app.route("/chain", methods=["GET"])
def get_chain():
    chain_data = [block.__dict__ for block in blockchain.chain]

    return json.dumps({"length": len(chain_data), "chain": chain_data}), 200

    
@app.route("/mine", methods=["GET"])
def mine_txns():
    result = blockchain.mine()
    
    if not result:
        return "Nothing to mine", 200
    
    return "Block #{} is being mined".format(result), 200


@app.route("/pending_txn", methods=["GET"])
def get_pending_txns():
    return json.dumps(blockchain.unconfirmed_transactions), 200


@app.route("/register_node", methods=["POST"])
def register_new_peer():
    node_address = request.get_json().get("node_address")

    if not node_address:
        return "Invalid node address", 404
    
    peers.add(node_address)
    return get_chain(), 200


@app.route("/register_with", methods=["POST"])
def register_with_existing_node():
    node_address = request.get_json().get("node_address")

    if not node_address:
        return "Invalid node address", 404

    data = {"node_address": request.host_url}
    headers = {'Content-Type': "application/json"}

    response = requests.post(
        node_address + "/register_node", 
        data=json.dumps(data), 
        headers=headers
    )

    if response.status_code == 200:
        global blockchain
        global peers
        
        chain_dump = response.json()['chain']
        blockchain = create_chain_from_dump(chain_dump)
        peers.update(response.json()['peers'])

        return "Registration successful", 200

    else:
        return response.content, response.status_code


def create_chain_from_dump(chain_dump):
    blockchain = Blockchain()
    for idx, block_data in enumerate(chain_dump):
        block = Block(
            block_data["index"],
            block_data["transactions"],
            block_data["timestamp"],
            block_data["previous_hash"]
        )
        proof = block_data['hash']
        if idx > 0:
            added = blockchain.add_block(block, proof)
            if not added:
                raise Exception("The chain dump is tampered!!")

        else:  # the block is a genesis block, no verification needed
            blockchain.chain.append(block)
            
        return blockchain



