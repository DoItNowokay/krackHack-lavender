# Python program to create Blockchain

# For timestamp
import datetime

# Calculating the hash
# in order to add digital
# fingerprints to the blocks
import hashlib

# To store data
# in our blockchain
import json

# Flask is for creating the web
# app and jsonify is for
# displaying the blockchain
# from flask import Flask, jsonify
import json

# Define the filename
filename = "simroop/data.json"

class Blockchain:

	# This function is created
	# to create the very first
	# block and set its hash to "0"
	def __init__(self):
		# with open(filename, 'r') as file:
	    #     self.chain = json.load(file)
		with open(filename,'r') as file:
			self.chain=json.load(file)
		# self.create_block(proof=1, previous_hash='0')

	# This function is created
	# to add further blocks
	# into the chain
		
	def create_block(self,proof,previous_hash,donor=None,doctor=None,recipient=None):
		block = {'index': len(self.chain) + 1,
                'donor':donor,
                'doctor':doctor,
                'recipient':recipient,
				'timestamp': str(datetime.datetime.now()),
				'proof': proof,
				'previous_hash': previous_hash}
		self.chain.append(block)
		# with open(filename, 'w') as file:
    	# 	json.dump(self.chain, file)
		with open(filename,'w') as file:
			json.dump(self.chain,file)
		return block

	# This function is created
	# to display the previous block
	def print_previous_block(self):
		return self.chain[-1]

	# This is the function for proof of work
	# and used to successfully mine the block
	def proof_of_work(self, previous_proof):
		new_proof = 1
		check_proof = False

		while check_proof is False:
			hash_operation = hashlib.sha256(
				str(new_proof**2 - previous_proof**2).encode()).hexdigest()
			if hash_operation[:5] == '00000':
				check_proof = True
			else:
				new_proof += 1

		return new_proof

	def hash(self, block):
		encoded_block = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(encoded_block).hexdigest()

	def chain_valid(self, chain):
		previous_block = chain[0]
		block_index = 1

		while block_index < len(chain):
			block = chain[block_index]
			if block['previous_hash'] != self.hash(previous_block):
				return False

			previous_proof = previous_block['proof']
			proof = block['proof']
			hash_operation = hashlib.sha256(
				str(proof**2 - previous_proof**2).encode()).hexdigest()

			if hash_operation[:5] != '00000':
				return False
			previous_block = block
			block_index += 1

		return True
	

blockchain=Blockchain()

def add_details(donor,doctor,recipient):
	previous_block = blockchain.print_previous_block()
	previous_proof = previous_block['proof']
	proof = blockchain.proof_of_work(previous_proof)
	previous_hash = blockchain.hash(previous_block)
	blockchain.create_block(proof,previous_hash,donor,doctor,recipient)

def is_valid():
	return blockchain.chain_valid(blockchain.chain)

def print_chain():
	return blockchain.chain