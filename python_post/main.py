
from traceback import print_tb
import requests

# payload = {"tupid":"TUPC-18-0638",
# "firstname":"Michael Angelo",
# "lastname":"Rilan",
# "phone":654654654,
# "address":"Bacoor,Cavite",
# "email":"micorilan1999@gmail.com",
# }

# r = requests.post('http://localhost:3100/users',json=payload)
# print(r.text)
class send_payload:
    def __init__(self):
        self.payload_insert = {"tupid":'', "firstname":'',"lastname":'',"phone":'',"address":'',"email":''}
        self.payload_select = {}
        self.payload_update = {"lastname":'', "address":'',"tupid":''}
        self.payload_delete = {"tupid":''}
    def choose(self):
        chs = input("\n\nPlease choose what you want to do: \n\n" + "a: Insert Data in the Database\n" + "b: Read All Data in the Database \n" + "c: Update some info in the Database\n" +"d: Delete row in database\n"+"e: Exit Program \n\n>>>")        
        return chs




obj_send_payload = send_payload()
while True:
    chosen = obj_send_payload.choose()


    if chosen == "a":
       
        input_tupid = input("Enter Student ID: ")
        obj_send_payload.payload_insert["tupid"] = input_tupid

        input_firstname = input("Enter Firstname: ")
        obj_send_payload.payload_insert["firstname"] = input_firstname

        input_lastname = input("Enter Lastname: ")
        obj_send_payload.payload_insert["lastname"] = input_lastname

        input_phone = input("Enter Phone number: ")
        obj_send_payload.payload_insert["phone"] = input_phone


        input_address = input("Enter Address: ")
        obj_send_payload.payload_insert["address"] = input_address

        input_email = input("Enter Email: ")
        obj_send_payload.payload_insert["email"] = input_email

        print(obj_send_payload.payload_insert)

        r= requests.post('http://localhost:3100/users',json=obj_send_payload.payload_insert)
        print(r.text)

    elif chosen == "b":
        r= requests.get('http://localhost:3100/users',json=obj_send_payload.payload_select)
        print(r.text)
        
    elif chosen == "c":

        input_tupid = input("Enter Student ID: ")
        obj_send_payload.payload_update["tupid"] = input_tupid

        input_lastname = input("Enter Lastname: ")
        obj_send_payload.payload_update["lastname"] = input_lastname

        input_address = input("Enter Address: ")
        obj_send_payload.payload_update["address"] = input_address
        
        print(obj_send_payload.payload_update)

        r= requests.put('http://localhost:3100/users',json=obj_send_payload.payload_update)
        print(r.text)

        
    elif chosen == "d":
        input_tupid = input("Enter Student ID You Wish to delete: ")
        obj_send_payload.payload_delete["tupid"] = input_tupid
        r= requests.delete('http://localhost:3100/users',json=obj_send_payload.payload_delete)
        print(r.text)
    elif chosen == "e":
        print("GoodBye")
        break
    else:
        print("Wrong Input, Please Try Again!! \n")
