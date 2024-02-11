from bson import ObjectId
x=[
    {'_id': ObjectId('65c89aaba4979e3a61037e90'), 'donar_number': 1, 'age': '23', 'blood': 'A+', 'organ':'heart'},
    {'_id': ObjectId('65c89aaba4979e3a61037e91'), 'donar_number': 2, 'age': '23', 'blood': 'A+', 'organ':'kidey'},
    {'_id': ObjectId('65c89aaba4979e3a61037e92'), 'donar_number': 3, 'age': '23', 'blood': 'A+', 'organ':'liver'},
    {'_id': ObjectId('65c89aaba4979e3a61037e93'), 'donar_number': 4, 'age': '23', 'blood': 'A+', 'organ':'brain'},
    ]
y={'_id': ObjectId('65c89aaba4979e3a61037e90'), 'reciver_number': 1, 'age': '23', 'blood': 'A+', 'organ':'liver'}
def find_match(donor_list,reci):
    for inx in range(len(donor_list)):
        if(reci['organ']==donor_list[inx]['organ']):
            return inx
    return -1

# print(find_match(x,y))