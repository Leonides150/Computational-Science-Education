#Check payment status using OOP, constructor, initiating a class
class Payslips:
    #Below is a constructor method that initializes the class with the given parameters. 
    # It is a special method that is called when an object of the class is created. 
    # It is used to initialize the attributes of the class. The name of the constructor method is __init__. 
    # It takes self as the first parameter, which refers to the instance of the class. The other parameters are name, 
    # payment and amount, which are used to initialize the attributes of the class.      
    def __init__(self, name, payment, amount) -> None:
        self.name = name 
        self.payment = payment 
        self.amount = amount 

    def pay(self):
        self.payment = "yes"
    
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " isn't paid yet"
        
ramesh = Payslips("Ramesh", "no", 1000)
navya = Payslips("Navya", "no", 3000)

print(ramesh.status(), "\n", navya.status())

#record payment
ramesh.pay()
print("After Payment")
print(ramesh.status(), "\n", navya.status())