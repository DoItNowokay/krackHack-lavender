import json

# Define the filename
filename = "simroop/data.json"

# Read existing data from the file, if any
try:
    with open(filename, 'r') as file:
        existing_data = json.load(file)
except FileNotFoundError:
    existing_data = []

# New data to add
new_data = {'index': 2, 'donor': 'John Doe', 'doctor': 'Dr. Smith', 'recipient': 'Jane Doe', 'timestamp': '2024-02-11 17:00:00', 'proof': 2, 'previous_hash': 'aefc2456'}

# Append new data to existing data
existing_data.append(new_data)

# Write updated data back to the file
with open(filename, 'w') as file:
    json.dump(existing_data, file)

print("New data has been added to", filename)