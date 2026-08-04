class cars ():
    def __init__(self,Number,Age,Name,Type,Team,Speed,Capacity):
        self.set_number(Number)
        self.set_age(Age)
        self.set_Name(Name)
        self.Type=Type
        self.Team=Team
        self.set_speed(Speed)
        self.set_Capacity(Capacity) 
    def set_number(self,Number):
        if Number>0:
            self.Number=Number
        else:print("Enter a positive Number")
    def set_age(self,Age):
        if Age>0:
            self.Age=Age
        else:print("Enter a positive number")
    def set_speed(self,Speed):
        if Speed>0:
            self.Speed=Speed
        else:print("Enter a positive number")
    def set_Capacity(self,Capacity):
        if Capacity>0:
            self.Capacity=Capacity
        else:print("Enter a positive number")
