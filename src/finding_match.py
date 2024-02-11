from bson import ObjectId
# donor=True
# x=[
#     {'_id': ObjectId('65c89aaba4979e3a61037e90'), 'donar_number': 1, 'age': '23', 'blood': 'A+', 'organ':'heart'},
#     {'_id': ObjectId('65c89aaba4979e3a61037e91'), 'donar_number': 2, 'age': '23', 'blood': 'A+', 'organ':'kidey'},
#     {'_id': ObjectId('65c89aaba4979e3a61037e92'), 'donar_number': 3, 'age': '23', 'blood': 'A+', 'organ':'liver'},
#     {'_id': ObjectId('65c89aaba4979e3a61037e93'), 'donar_number': 4, 'age': '23', 'blood': 'A+', 'organ':'brain'},
#     ]
# y=[
#     {'_id': ObjectId('65c89aaba4979e3a61037e90'), 'reciver_number': 1, 'age': '23', 'blood': 'A+', 'organ':'liver'},
#     {'_id': ObjectId('65c89aaba4979e3a61037e90'), 'reciver_number': 2, 'age': '23', 'blood': 'A+', 'organ':'liver'},
#     {'_id': ObjectId('65c89aaba4979e3a61037e90'), 'reciver_number': 3, 'age': '23', 'blood': 'A+', 'organ':'liver'},
#     {'_id': ObjectId('65c89aaba4979e3a61037e90'), 'reciver_number': 4, 'age': '23', 'blood': 'A+', 'organ':'liver'}
# ]
def find_match(donor_list,reci_list):
    if(len(reci_list)==0 or len(donor_list)==0):
          return -1,-1
    for inx in range(len(donor_list)):
            if(reci_list[0]['organNeeded']==donor_list[inx]['Organ']):
                return inx,0
    for inx in range(len(reci_list)):
            if(donor_list[0]['Organ']==reci_list[inx]['organNeeded']):
                return 0,inx
    return -1,-1

# print(find_match(x,y,False))