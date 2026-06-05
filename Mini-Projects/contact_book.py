class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show_contact(self):
        print(f"Name : {self.name}\nPhone : {self.phone}\n")


con1 = Contact("ravi", 8885054532)
con2 = Contact("candy", 986489374)
con3 = Contact("nish", 87694838323)
contacts= [con1, con2, con3]
for i in contacts:
    i.show_contact()
search = input("search contact : ")
found=False
for i in contacts:
 if search == i.name:
         
         print(f"Number : {i.phone},")
         found=True
if found==False:
    print("Not found")
    

    