#make the parent class of cars 
#the princeple "encapsulation is already used as we use a private attributes "
# adding the abstraction methods because in general i won't need to make an instance with car class instead i will use the childs of it that will inherit

from abc import ABC, abstractmethod



class Cars(ABC):
    #use init method to set the class attributes and make them private
    def __init__(self, Number, Age, Name, Team, Speed, Capacity):#the attributes are set by using setters 
        self.set_number(Number)
        self.set_age(Age)
        self.set_name(Name)
        self.set_team(Team)
        self.set_speed(Speed)
        self.set_capacity(Capacity)

# I noticed we check if the number is positive in many attributes so those are two static methods  
    @staticmethod
    def check_positive(number):#to check the input is number or not and if it positive or not 
        try:
            if int(number) <=0:
                print("enter a positive number")
                return False
            else: return True
        except ValueError:print("enter a valid integer Number \n")
### to check if the names are valid
    @staticmethod
    def check_names(text):## same for the text
        try:
            if any(letter.isalpha() for letter in text):### any retuns True or False
                return True
            else:
                print("please enter a valid name contain letters\n")
                return False
        except ValueError : print("enter a valid user name with at least one letter\n")

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

    @abstractmethod  ### to abstract method applied because they will peform alike functions in child class but with simple modifications
    def performance_score(self,Speed,Capacity):
        pass
    @abstractmethod
    def display(self):
        pass

    ##encapsulation and check in mechanisim idk is that true that this part is here or it may be not totally important in this case!!
    def _confirmation_message():## a protected method as there is no use of it  alone out of the class
        print("your information has been saved successfully !")

    @classmethod ##becasue it will need to create an object so it will need to take the class as attribute
    @abstractmethod ## it will also need to input a slightly different inputs accor to the child class
    def check_in(cls):
        print("please go on and enter your information \n")
        pass


#a getter for each attributes may not be benefit now but may be useful in case of adding more advanced features i think!!



#create the child classes ------> new attributes-setters for them-getters for them- the three abstract method we crated above 
class Racer(Cars):
    def __init__(self, Number, Age, Name, Team, Speed, Capacity,NoLapsCompleted,NoRacesCompleted):
        super().__init__( Number, Age, Name, Team, Speed, Capacity)#using to assign the parent class attributes 
        self.set_laps(NoLapsCompleted) #assigning the unique attributes of this class 
        self.set_races(NoRacesCompleted)

# the getter for the new attribues 
    @property
    def get_laps(self):
        return self.__NoLapscompleted
    @property
    def get_races(self):
        return self.__NoRacesCompleted
#the setters for the new attribute

    def set_laps(self,laps):
        if self.check_positive(laps):
            self.__NoLapsCompleted=laps
        else:print("enter a valid no of laps ")

    def set_races(self,races):
        if self.check_positive(races):
            self.__NoRacesCompleted=races
        else:print('enter a valid no of races ')
#the abstract methods ##to calculate the preformace "polymorphism"

    def performance_score(self):
        return(self.get_Speed * 10) + self.get_Capacity
    ### so the info can be easily displayed 
    def display(self): ## i guess i was capable of using the __dict__ method but i feel it display the class attributes name so they no more protected  should i use it !
            return {
        "Number": self.get_Number,
        "Age": self.get_Age,
        "Name": self.get_Name,
        "Team": self.get_Team,
        "Speed": self.get_Speed,
        "Capacity": self.get_Capacity,
        "Number of laps completed": self.__NoLapsCompleted,
        "Number of races completed":self.__NoRacesCompleted,
        "performance":self.performance_score()
    }
    @classmethod
    def check_in(cls):
        while True: ## check the inputed data before it reach and create the object so no error occure due to empty attribute
            print('check in is starting .........!!\n\n')            
            number = input("Enter the car number: ")
            if not Cars.check_positive(number):
                continue

            name = input("Enter the racer's name: ")
            if not Cars.check_names(name):
                continue

            age = input("Enter the racer age: ")
            if not Cars.check_positive(age):
                continue

            team = input("Enter the team: ")
            if not Cars.check_names(team):
                continue

            speed = input("Enter the speed: ")
            if not Cars.check_positive(speed):
                continue

            capacity =input("Enter the capacity: ")
            if not Cars.check_positive(capacity):
                continue

            nolaps = input("Enter the number of laps completed: ")
            if not Cars.check_positive(nolaps):
                continue

            noraces = input("Enter the number of races completed: ")
            if not Cars.check_positive(noraces):
                continue

            return cls( number, age, name, team, speed, capacity,nolaps, noraces)


    



        

#car1=Cars(integer,integer,string,string,integer,integer)
racer1 = Racer.check_in()
info=racer1.display() ## a dictionary i can iterate and print it in more organized way 
print(info)

