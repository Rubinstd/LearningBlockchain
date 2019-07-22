#####
# File: blockchain.py
# Description: First attempt at blockchain. Created following the guide at: https://www.ibm.com/developerworks/cloud/library/cl-develop-blockchain-app-in-python/index.html
#              While the code here is very similar to that of the tutorial, I'll add comments myself to learn the process.
# Author: Daniel Rubinstein
#
#####
from hashlib import sha256
import json

# Class for defining a single block in the chain.
class Block:
    # Constructor.
    def __init__(self, transactions, timestamp, previous_hash):
        self.index = []
        self.transations = transations
        self.timestamp = timestamp
        self.previous_hash = previous_hash
    
    # Compute the hash of a block. Used for chaining blocks together. By using a hash we create immutability (i.e. if a given block is changed, anything that was chained to it previously will no longer point to that changed block).
    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

# Class for defining the chain of blocks.        
class BlockChain:
    # Defines how difficult the POW algorithm is to compute.
    difficulty = 2

    # Constructor.
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_gen_block()
    
    # Manually generates the first block.
    def create_gen_block(self):
        gen_block = Block(0,[],"0")
        gen_block.hash = gen_block.compute_hash()
        self.chain.append(gen_block)
    
    # Get last block.
    @property
    def last_block(self):
        return self.chain[-1]

    # POW algorithm. Used to make recalculating block chains difficult. Essentially states that hte has has to start with X leading zeros (where X is difficulty above). Makes recalculating the chain non-trival.
    def proof_of_work(self, block):
        block.nonce = 0

        computed_hash = block.compute_hash()

        while not computed_hash.startswith('0' * BlockChain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        
        return computed_hash
    
    def add_block(self, block, proof):
        # Get the last blocks hash.
        previous_hash = self.last_block.hash

        # Check that the block being added points to the end of the chain.
        if previous_hash != block.previous_hash:
            return False
        # Check that the POW of the block is valid.
        if not self.is_valid_proof(block, proof):
            return False
        
        # Set the hash of the block being added.
        block.hash = proof
        # Add the block to the chain.
        self.chain.append(block)
        return True
    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * BlockChain.difficulty) and block_hash == block.compute_hash())