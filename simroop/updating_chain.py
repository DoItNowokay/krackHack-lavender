import organ_chain
import validate



# this is copy of what i am supposed to get form database  [donor_details,public key]
donor=[validate.enc_donor,validate.donor_public]
doctor=[validate.enc_doctor,validate.doctor_public]
recipient=[validate.enc_reci,validate.recipient_public]


if(validate.check_validity(donor,doctor,recipient)):
    organ_chain.add_details(validate.donor,validate.doctor,validate.recipient)
# organ_chain.add_details(validate.donor,validate.doctor,validate.recipient)
print(organ_chain.is_valid())
chain=organ_chain.print_chain()
for _ in chain:
    print(_)