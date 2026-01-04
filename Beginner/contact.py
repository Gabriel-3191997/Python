def myContacts():
    # Create one dictionary to hold all contacts
    address = {}

    # Contact 1
    contact_name_1 = input("Name: ")
    contact_phone_1 = input("Mobile Number: ")
    address[contact_name_1] = contact_phone_1

    # Contact 2
    contact_name_2 = input("Name: ")
    contact_phone_2 = input("Mobile Number: ")
    address[contact_name_2] = contact_phone_2


    for name, phone in address.items():  
    
        print(f"\n\nName: {name}\nMobile Number: {phone}")


myContacts()
