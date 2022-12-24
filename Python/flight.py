class Flight ():
    def __init__(self,capacity):
       self.capacity=capacity
       self.passenger= []
    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True
    def open_seats(self):
        return self.capacity-len(self.passenger)  
fl=Flight(3)       
people=["Harry","Ron","Harmione","Ginny"]
for p in people:
    success = fl.add_passenger(p)
    if success:
        print (f"Added {p} to flight successfully")    
    else:
        print("No avilable seats preasent now!!")    