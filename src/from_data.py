from bson import ObjectId
import finding_match
import pymongo
import json
import rsa_algo
from bson import ObjectId
from bson.json_util import default
import organ_chain
import os
import webbrowser
# code for recieving data from database
import validate

# Connect to MongoDB
def func():
    client = pymongo.MongoClient("mongodb+srv://KrackHack:bipanjit2422@krackhack.hgev8sl.mongodb.net/?retryWrites=true&w=majority")
    db = client["blockchain_db"]

    donor_collection=db['donar']
    reciver_collection=db['RE']
    reciver_collection=db['Receiver']

    # adding all data in list
    donor_list=[]
    for data in donor_collection.find():
        donor_list.append(data)
    recipient_list=[]
    for data in reciver_collection.find():
        recipient_list.append(data)

    # print(donor_list)
    # print(recipient_list)
    match=finding_match.find_match(donor_list,recipient_list)
    if(match==(-1,-1)):
        print("nomatch")
        return 1
    # else:
        # filename = 'file:///'+os.getcwd()+'/' + 'comfirmation.html'
        # webbrowser.open_new_tab(filename)
    # now assuming that comfirmation has came from both end

    # creating public and private keys
    donor_public,donor_private=rsa_algo.generate_key_pair()
    # doctor_public,doctor_private=rsa_algo.generate_key_pair()
    recipient_public,recipient_private=rsa_algo.generate_key_pair()

    # converting dict to string 
    def custom_json_encoder(obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return default(obj)

    # Convert dictionary to a string, handling non-serializable data
    recipient_details = json.dumps(recipient_list[match[1]], default=custom_json_encoder)
    donor_details = json.dumps(donor_list[match[0]], default=custom_json_encoder)

    enc_donor_details=rsa_algo.encrypt_message(donor_private,donor_details)
    enc_reci_details=rsa_algo.encrypt_message(recipient_private,recipient_details)
    # print(rsa_algo.decrypt_message(donor_public,enc_donor_details))
    # print("he;")
    # print(donor_public,donor_private)
    if(validate.check_validity([enc_donor_details,donor_public],[enc_reci_details,recipient_public])):
        # print(1)
        organ_chain.add_details(rsa_algo.decrypt_message(donor_public,enc_donor_details),rsa_algo.decrypt_message(recipient_public,enc_reci_details))
    print(organ_chain.is_valid())
    print(organ_chain.print_chain())
    print(len(organ_chain.print_chain()))
    donor_collection.delete_one({"_id": ObjectId(donor_list[match[0]]['_id'])})
    reciver_collection.delete_one({"_id": ObjectId(recipient_list[match[1]]['_id'])})