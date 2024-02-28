# Data abstraction is one of the most essential concepts of Python OOPs which is used to hide irrelevant details from the user and show the details that are relevant to the users. 
# For example, the readers of geeksforgeeks only know that a writer can write an article on geeksforgeeks, and when it gets published readers can read the articles but the reader is not aware of the background process of publishing the article.

# A simple example of this can be a car. A car has an accelerator, clutch, and break and we all know that pressing an accelerator will increase the speed of the car and applying the brake can stop the car but we don’t the internal mechanism of the car and how these functionalities can work this detail hiding is known as data abstraction.

# To understand data abstraction we should be aware of the below basic concepts:

#     OOP concepts in Python
#     Classes in Python
#     Abstract classes in Python

# Importance of Data Abstraction

# It enables programmers to hide complex implementation details while just showing users the most crucial data and functions. This abstraction makes it easier to design modular and well-organized code, makes it simpler to understand and maintain, promotes code reuse, and improves developer collaboration.
# Data Abstraction in Python

# Data abstraction in Python is a programming concept that hides complex implementation details while exposing only essential information and functionalities to users. In Python, we can achieve data abstraction by using abstract classes and abstract classes can be created using abc (abstract base class) module and abstractmethod of abc module.
# Abstraction classes in Python

# Abstract class is a class in which one or more abstract methods are defined. When a method is declared inside the class without its implementation is known as abstract method.

# Abstract Method: In Python, abstract method feature is not a default feature as in Java. To create abstract method and abstract classes we have to import the “ABC” and “abstractmethod” classes from abc (Abstract Base Class) library. Abstract method of base class force its child class to write the implementation of the all abstract methods defined in base class. If we do not implement the abstract methods of base class in the child class then our code will give error. In the below code method_1 is a abstract method created using @abstractmethod decorator.

from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
         #empty body
         pass

# Concrete Method: Concrete methods are the methods defined in an abstract base class with their complete implementation. Concrete methods are required to avoid reprication of code in subclasses. For example, in abstract base class there may be a method that implementation is to be same in all its subclasses, so we write the implementation of that method in abstract base class after which we do not need to write implementation of the concrete method again and again in every subclass. In the below code startEngine is a concrete method.

class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_started = True

    def startEngine(self):
        if not self.engine_started:
            print(f"Starting the {self.model}'s engine.")
            self.engine_started = True
        else:
            print("Engine is already running.")

# Steps to Create Abstract Base Class and Abstract Method:

#     Firstly, we import ABC and abstractmethod class from abc (Abstract Base Class) library.
#     Create a BaseClass that inherits from the ABC class. In Python, when a class inherits from ABC, it indicates that the class is intended to be an abstract base class.
#     Inside BaseClass we declare an abstract method named “method_1” by using “abstractmethod” decorater. Any subclass derived from BaseClass must implement this method_1 method. We write pass in this method which indicates that there is no code or logic in this method.

from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
         #empty body
         pass

# Implementation of Data Abstraction in Python

# In the below code, we have implemented data abstraction using abstract class and method. Firstly, we import the required modules or classes from abc library then we create a base class ‘Car’ that inherited from ‘ABC’ class that we have imported. Inside base class we create init function, abstract function and non-abstract functions. To declare abstract function printDetails we use “@abstractmethod” decorator. After that we create child class hatchback and suv. Since, these child classes inherited from abstract class so, we need to write the implementation of all abstract function declared in the base class. We write the implementation of abstract method in both child class. We create an instance of a child class and call the printDetails method. In this way we can achieve the data abstraction.

# Import required modules
from abc import ABC, abstractmethod
 
# Create Abstract base class
class Car(ABC):
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
     
  # Create abstract method      
  @abstractmethod
  def printDetails(self):
    pass
   
  # Create concrete method
  def accelerate(self):
    print("speed up ...")
   
  def break_applied(self):
    print("Car stop")
     
# Create a child class
class Hatchback(Car):
   
  def printDetails(self):
    print("Brand:", self.brand);
    print("Model:", self.model);
    print("Year:", self.year);
   
  def Sunroof(self):
    print("Not having this feature")
     
# Create a child class
class Suv(Car):
   
  def printDetails(self):
    print("Brand:", self.brand);
    print("Model:", self.model);
    print("Year:", self.year);
   
  def Sunroof(self):
    print("Available")
 
     
car1 = Hatchback("Maruti", "Alto", "2022");
 
car1.printDetails()
car1.accelerate()
     
  

# Output
'''
Brand: Maruti
Model: Alto
Year: 2022
speed up ...
'''
