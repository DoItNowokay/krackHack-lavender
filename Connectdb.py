import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://KrackHack:bipanjit2422@krackhack.hgev8sl.mongodb.net/?retryWrites=true&w=majority")
db = client["blockchain_db"]

# Define collections
blocks_collection = db["blocks"]
transactions_collection = db["transactions"]

# Define sample data
block_data = {
    "block_number": 1,
    "hash": "xyz123",
    "previous_hash": "abc123",
    "timestamp": "2024-02-11 12:00:00",
    # Other block data...
}

transaction_data = {
    "tx_id": "tx123",
    "from_address": "address1",
    "to_address": "address2",
    "amount": 10,
    # Other transaction data...
}

# Insert data into collections
blocks_collection.insert_one(block_data)
transactions_collection.insert_one(transaction_data)

# Query data
block = blocks_collection.find_one({"block_number": 1})
print(block)

transaction = transactions_collection.find_one({"tx_id": "tx123"})
print(transaction)
