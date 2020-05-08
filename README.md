# Blockchain
This is blockchain-based application within a distributed peer-to-peer network.

## Purpose
Main purpose of this *dapp* is to allow users whithin the network to communicate each others by posting messages. These messages are processed as transactions and mined in order to add them to the blockchain.

## Pow algorithm
The proof of work for this blockchain is based on the hash of each Block that might contain one or more transactions. Each transaction is defined by the next info:
* Author
* Content
* Timestamp

Each block is defined by the next:
* Index
* Transactions
* Timestamp
* Previous block (defined by its hash)

Algorithm consists in look for such a *Nonce* value that when calculating hash function for that block, result begin with "00".


## Consensus algorithm
The consensus for this blockchain is as simple as just select the larger chain as the valid chain

## Runing
For running this *Dapp* (Descentralized Application) just clone this repo with next command

`git clone https://github.com/ManuGS2/Blockchain.git`

Then change to this repo´s directory

`cd Blockchain`

And finally run the next script

`sh run.sh`

Application will be running on http://localhost:5000/