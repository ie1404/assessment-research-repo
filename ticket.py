



 




    # ticket=2000

    # while ticket >=2000:
    #     time.sleep(1)
    #     print("ticket #:",ticket)


class Ticket():
    ticket_id:None
    staff_id:None
    name:None
    email:None
    issue:None
    response:None
    status:None

    def __init__(self, ticket_id, staff_id, name, email, issue):
        self.ticket_id=ticket_id
        self.staff_id=staff_id
        self.name=name
        self.email=email
        self.issue=issue
        # self.response=response
        self.response = "not provided yet"
        self.status = "SUBMITTED"
    
    def display(self):
        print("\n************************")
        print("Ticket Id:",self.ticket_id)
        print("Staff Id: ", self.staff_id)
        print("Name: ",self.name)
        print("Email: ",self.email)
        print("Issue: ",self.issue)
        print("Response:", self.response)
        print("Status:",self.status)
        print("************************\n")
    
            
    
    # class teponse(ticket):
    #     Hel:int
    #     def __init__(self, id, name, email, issue,Hel):
    #         super().__init__( id, name, email, issue)
    #         self.Hel=Hel
        
            
    #     def display(self):
    #         super().display()
    #         print("0:Technical")
    #         print("1:technical")
    #         print("2:techn")
            
        
        
                
            

        
            
            
    # Staff=ticket("Id",input("Whats your name:"),input("whats your email"),input("whats your issue:"))
    # Staff.display()

    # print("0:Technical")
    # print("1:technical")
    # print("2:techn")
    # x=input()
    

    # if x=='0':
    #     print("ddd")
        
    # elif x=='1':
    #     print("meh")
        
    # elif x=='2':
    #     print("qqq")
    # else:
    #     print("not an option\n")
    

    





# class Staff():
#     Id:None
#     Name:None
#     email:None
#     issue:None
    
#     def __init__(staff,Id,Name,email,issue):
#         staff.Id=Id
#         staff.Name=Name
#         staff.email=email
#         staff.issue=issue

#     def display(staff):
#         print("Staff Id: ",staff.Id)
#         print("Name: ",staff.Name)
#         print("Email: ",staff.email)
#         print("Issue: ",staff.issue)





#ticket id displayed

# staff ID displayed

#staff name displayed

# email displayed

#type of issue

#response





