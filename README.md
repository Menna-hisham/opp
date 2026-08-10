> # What is the project about?
>
>> **This Project is Like a Garage Management system**
>> **it now contains the features of adding cars only, but it will be containing features of displaying all the cars in garage, edit their information, retire a car, after I do some edits**

> # How to Run the project
>
>>**it is now a primary version that only take the information and create the object**
>> 1- ** but the vision is that there will be a menu that will appear with numerated options 1-add ,2-display,3-edit,4-retire**


> # Project structure
## Encapsulation
>- By making the data in the class private and some methods protected so that I limit their access outside the class 
>- it will also be easy i think adding new child classes,
## Abstraction 
>- supporting the Encapsulation by using the abstraction method so that the detailed code is in the class and in the main code only the methods appear enough to say what is happening but not to show how it is happening 
>- I also used the abstractmethod decorator from ABC class to make the *abstraction methods (display-performance_score-check_in)* as the parent class Cars is an abstraction class only like a mold for the child classes.
## Polymorphism
>- is done as I used the abstraction methods in the Racer class to do a certain function and by creating another child classes it will be exist with the same name but performing a slightly different function.
## also, inheritance is obv. used 

## debugging "ideas behind the code" 
>- 1-   the error when entering a letter in the age or number so I tried handling it by checking the input before it reaches the method "so that I can avoid the error of the attribute not having a value if the input is wrong", and I think that mean that I don't need the setters because the input is already checked so it will always be the valid one !!!,
>- 2-   the getter for each attribute may seem not useful but I think it may be useful in case of adding any features I tried to use everything I learned so far, but I think the code may contain some unnecessary parts after I made them, I realized they are not necessary like the getters, on protected method, I am not sure if there is more non efficient parts.
>- 3-   I am willing to continue and make the code more organized and advanced but this how far I could reach for now.
