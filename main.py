from ticket import*



if __name__ == "__main__":
    tickets = []
    ticket_counter = 2000;
    ticket_amount=0

    t1=Ticket(ticket_counter, "ISAACE", "Isaac","ie@xtra.nz","diasohfaiosdhfiuo",)
    tickets.append(t1)
    ticket_counter +=1;
    ticket_amount+=1
    t2=Ticket(ticket_counter,"MarinaK","Marina","marina@gmail.com","HELP")
    tickets.append(t2)
    ticket_counter +=1;
    ticket_amount+=1

    def input_new_ticket():
        print("Enter the new ticket...")
        staff_id=input("what is your staff id: ",)
        name=input("what is your name: ",)
        email=input("what is your email? ",)
        issue=input("what is your issue ",)
        
        t=Ticket(ticket_counter, staff_id, name, email, issue,)
        tickets.append(t)
    
    def display_tickets():
        for t in tickets:
            t.display()

    def responses():
        for t in tickets:
            t.display()
        t_n = int(input("What is the ticket Number you want to respond to?"))
        
        rs = input("What is your response? " )
        
        for t in tickets:
            
            if t.ticket_id == t_n:
                
                t.response=rs
                t.status="CLOSED"
                print("\n")
                t.display()
        

    def reopen():
        for t in tickets:
            t.display()
        re=int(input("What is the ticket Number you want to reopen to?",))
        for t in tickets:

            if t.ticket_id==re:
                t.status="OPEN"
            
    
    def display_stats():
        print ("Amount of tickets: ",ticket_amount)

    smenu = -1
    while smenu != "6":
        print("\n\n########################")
        print("| Selection Menu:      |")
        print("|1:Create a ticket     | ")
        print("|2: Display all tickets| ")
        print("|3:Provide a response  |")
        print("|4:reopen a ticket     |")
        print("|5:display stats       |")
        print("|6:quit                |")
        print("########################\n")
        smenu=int(input(":"))
        if smenu==1:
            input_new_ticket()
            ticket_counter+=1
            ticket_amount+=1
        elif smenu==2:
            display_tickets()
        elif smenu==3:
            responses()
        elif smenu==4:
            reopen()
        elif smenu==5:
            display_stats()
        elif smenu==6:
            print("")
            print("Thank you, Have a good day!")
            pass;
        else:
            print("NOT AN OPTION")

