#make the parent class of cars 
#the princeple "encapsulation is already used as we use a private attributes "

class Cars:
    #use init method to set the class attributes and make them private
    def __init__(self, Number, Age, Name, Team, Speed, Capacity):#the attributes are set by using setter 
        self.set_number(Number)
        self.set_age(Age)
        self.set_name(Name)
        self.set_team(Team)
        self.set_speed(Speed)
        self.set_capacity(Capacity)

# I noticed we check if the number is positive in many attributes so 
    def check_positive(self,number):
        try:
            if number <=0:
                print("enter a positive number")
                return False
                raise ValueError
            else: return True
        except TypeError:print("enter a valid")
### to check if the names are valid
    def check_names(self,text):
        try:
            if any(char.isalpha() for char in text):
                return True
            else:
                print("please enter a valid name contain letters")
                return False
        except TypeError : print("the name must contain letters")

#the getters  as the attributes are private

    @property
    def get_Number(self):
        return  self.__Number
    @property
    def get_Age(self):
        return  self.__Age
    @property
    def get_Name(self):
        return  self.__Name
    @property
    def get_Team(self):
        return  self.__Team
    @property
    def get_Speed(self):
        return  self.__Speed
    @property
    def get_Capacity(self):
        return  self.__Capacity

#start setting the setters  as we want the attributes to be private 
  
    def set_number(self,valid_number):
        if self.check_positive(valid_number):
            self.__Number=valid_number
       
    def set_age(self,valid_age):
        if self.check_positive(valid_age):
            self.__Age=valid_age
        
    def set_speed(self,valid_speed):
        if self.check_positive(valid_speed):
            self.__Speed=valid_speed
       
    def set_capacity(self,valid_capacity):
        if self.check_positive(valid_capacity):
            self.__Capacity=valid_capacity
            
        
    def set_name(self,valid_name):
        if self.check_names(valid_name):
            self.__Name=valid_name
        
    def set_team(self,valid_team):
        if self.check_names(valid_team):
            self.__Team=valid_team

### if we have a list of available team names we can also check if the entered team name is matching one of them and if not deny it

        

#car1=Cars(integer,integer,string,string,integer,integer)
