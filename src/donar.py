from flask import Flask, request
import pymongo
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
class BlockchainDB:
    def __init__(self, connection_uri, db_name):
        self.client = pymongo.MongoClient(connection_uri)
        self.db = self.client[db_name]
        self.donar_collection = self.db["donar"]
        self.receivers_collection = self.db["Receiver"]
        self.donar_count=0
        self.receiver_count=0

    def insert_donar(self, donar_data):
        self.donar_count+=1
        donar_data["donar_number"] = self.donar_count
        self.donar_collection.insert_one(donar_data)

    def insert_receiver(self, receiver_data):
        self.receiver_count+=1
        receiver_data["receiver_number"] = self.receiver_count
        self.receivers_collection.insert_one(receiver_data)

    def find_donar(self,no):
        return self.donar_collection.find_one({"donar_number": no})

    def find_receiver(self, no):
        return self.receivers_collection.find_one({"receiver_number": no})
    
    def donar_number(self):
        return self.donar_count
    
    def receiver_number(self):
        return self.receiver_count

# Initialize the BlockchainDB object
connection_uri = "mongodb+srv://KrackHack:bipanjit2422@krackhack.hgev8sl.mongodb.net/?retryWrites=true&w=majority"
db_name = "blockchain_db"
blockchain_db = BlockchainDB(connection_uri, db_name)

@app.route('/donarData', methods=['POST'])
def add_donar():
    if request.method == 'POST':
        print(request.form)
        donar_data = {
            "userName": request.form['userName'],
            "Organ": request.form['Organ'],
            "bloodgroup": request.form['bloodgroup'],
            "donarid": request.form['donarid']
        }
        print(donar_data)
        blockchain_db.insert_donar(donar_data)
        return 'Donar data added successfully!'

@app.route('/receiverData', methods=['POST'])
def add_receiver():
    if request.method == 'POST':
        receiver_data = {
            "userName": request.form['userName'],
            "bloodgroup": request.form['bloodgroup'],
            "organNeeded": request.form['Organ'],
            "receiverid": request.form['receiverid']
        }
        blockchain_db.insert_receiver(receiver_data)
        return 'Receiver data added successfully!'

if __name__ == '__main__':
    app.run(debug=True,port=5000)
