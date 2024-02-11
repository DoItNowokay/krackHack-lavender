''' 
this script is for checking if the transection is valid or not
'''

import pandas as pd
import rsa_algo 
import json
# data of donor
donor="{'name':'bilal','blood_group':'x+','organ':'kidney1','age':10,'unique_donor_id':'xyz'}"
doctor="{'name':'chetan','donor_name':'bilal','donor_age':10,'donor_organ':'kidney1','recipient_name':'bilal','recipient_age':10,'recipient_organ':'kidney2','unique_donor_id':'xyz','unique_reci_id':'abc'}"
recipient="{'name':'bilal','blood_group':'x+','organ':'kidney2','age':10,'unique_reci_id':'abc'}"

# key for all
donor_public,donor_private=rsa_algo.generate_key_pair()
doctor_public,doctor_private=rsa_algo.generate_key_pair()
recipient_public,recipient_private=rsa_algo.generate_key_pair()

# encrption using private key
enc_donor=rsa_algo.encrypt_message(donor_private,donor)
enc_doctor=rsa_algo.encrypt_message(doctor_private,doctor)
enc_reci=rsa_algo.encrypt_message(recipient_private,recipient)

def decrypt(enc_data,public_key):
    return eval(rsa_algo.decrypt_message(public_key,enc_data))
# checking if everythign is fine 
def check_validity(donor,doctor,recipient):
    try:
        doctor[0]=decrypt(doctor[0],doctor[1])
        donor[0]=decrypt(donor[0],donor[1])
        recipient[0]=decrypt(recipient[0],recipient[1])
    except:
        return False
    if(doctor[0]['donor_name']!=donor[0]['name'] or doctor[0]['recipient_name']!=recipient[0]['name']): return False
    if(doctor[0]['donor_organ']!=donor[0]['organ'] or doctor[0]['recipient_organ']!=recipient[0]['organ']): return False
    return True


# decryption in dictionary
# dec_donor=decrypt(enc_donor,donor_public)
# dec_doctor=decrypt(enc_doctor,doctor_public)
# dec_recipient=decrypt(enc_reci,recipient_public)

# def check_validity():
#     return check_valid([enc_donor,donor_public],[enc_doctor,doctor_public],[enc_reci,recipient_public])

# print(check_validity([enc_donor,donor_public],[enc_doctor,doctor_public],[enc_reci,recipient_public]))