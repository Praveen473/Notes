#if we use mapping
#user=input()
#list1=list(map(int,user.split()))
#not using mapping
# user_input = input("Enter list of values to insert into BST (e.g. 5 3 7 2 4): ").split()
# values = [int(val) for val in user_input]

#---------------------------------------------------------------------------------------------------------------
#dict
# def count(w):
#     counts={}
#     for i in w:
#         counts[i]=counts.get(i,0)+1
#     return counts
# a=count("bat")


# s = "aaaaabbc"
# d = {}
#
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

#---------------------------------------------------------------------------------------------------------------
# a=[1,2,3,4,5]
# print(*a) #is a shorthand way of printing all elements in the list a separated by spaces.
#----------------------------------------------------------------------------------------------------------------
# Lambda
"""Anonymous Functions:
 Sometimes we can declare a function without any name,such type of nameless
functions are called anonymous functions or lambda functions.
 The main purpose of anonymous function is just for instant use(i.e for one time usage)"""
# s=lambda a,b:a+b
# print(s(4,5))
#---------------------------------------------------------------------------------------------------------------
#filter
"""filter() Function:
We can use filter() function to filter values from the given sequence based on some
condition.
filter(function,sequence)
Where Function Argument is responsible to perform conditional check Sequence can be
List OR Tuple OR String."""
# def square(val):
#     if val%2==0:
#         return val
# a=[1,2,3,4,5]
# print(list(filter(square,a)))#[2,4]
#print(list(square(a)))#error
#print(list(map(square,a)))
#---------------------------------------------------------------------------------------------------------------
#map
"""For every element present in the given sequence,apply some functionality and
generate new element with the required modification. For this requirement we
should go for map() function.
: For every element present in the list perform double and generate new list of
doubles  Syntax: map(function, sequence)"""
#without lambda
# def square(val):
#     if val%2==0:
#         return val
# a=[1,2,3,4,5]
# print(list(map(square,a)))#[None, 2, None, 4, None]
#---------------------------------------------------------------------------------------------------------------
#withlambda
# b=[1,2,3,4,5]
# print(list(map(lambda x:x*x,b)))#[1, 4, 9, 16, 25]
#-------------------------------------
#reduce() Function:
"""reduce() function reduces sequence of elements into a single element by applying the
specified function.
 reduce(function,sequence)
 reduce() function present in functools module and hence we should write import
statement.
"""
# from functools import *
# l=[10,20,30,40,50]
# print(reduce(lambda x,y:x+y,l))#150
#---------------------------------------------------------------------------------------------------------------
#important
"""Everything is an Object:
 In Python every thing is treated as object.
 Even functions also internally treated as objects only."""
# def f1():
#     print("Hello")
# print(f1)
# print(id(f1))## prints the ID (usually the memory address in decimal)--------------------important----------------------
#----------------------------------------------------------------------------------------------------------------
"""Function Aliasing:
For the existing function we can give another name, which is nothing but function aliasing. """
# def func(name):
#     print("func")
# alias=func#------------------------aliasing---------------------
# func(1)
# alias(1)
#---------------------------------------------------------------------------------------------------------------
"""types of variable
There are 3 types of variables are allowed.
1) Instance Variables (Object Level Variables)
2) Static Variables (Class Level Variables)
3) Local variables (Method Level Variables)"""
# class test:
#     static_var=10
#     def __init__(self,val):
#         self.instance_var=val
#     def call(self,data):
#         res=data+10#local
#         print(res,self.instance_var,test.static_var)
# a=test(10)
# a.call(20)

#access modfier methods
# class Car:
#     def start_engine(self):          # Public method
#         print("Engine started.")
#
#     def _check_oil(self):            # Protected method (convention)
#         print("Oil level is good.")
#
#     def __fuel_injector_status(self):  # Private method
#         print("Fuel injector is working fine.")
#
#     def service(self):               # Public method calling private one
#         self._check_oil()
#         self.__fuel_injector_status()
#         print("Car serviced.")
#
# c = Car()
#
# c.start_engine()         # ✅ Public method: works fine
# c._check_oil()           # ⚠️ Protected method: works, but should not be used outside
# c.service()              # ✅ Calls private and protected methods internally
#
# c.__fuel_injector_status()  # ❌ Private method: Error (AttributeError)



#---------------------------------------------------------------------------------------------------
# Types of method
# 1) Instance Methods
# 2) Class Methods
# 3) Static Methods

# class test:
#     static_var=10
#     def call(self,data):
#         res=data+10#local
#         print(res,test.static_var)
#     @classmethod
#     def call2(cls,c):
#         print(c)
#     @staticmethod
#     def call1(aa):
#         print(aa)
# a=test()
# a.call(10)
# a.call1(5)
# a.call2(20)

#class method use
# class Employee:
#     company = "TechCorp"  # ✅ Class (static) variable shared across all instances
#
#     def __init__(self, name):
#         self.name = name  # ✅ Instance variable unique to each object
#
#     @classmethod
#     def set_company(cls, new_name):
#         cls.company = new_name  # ✅ Class method that modifies the class variable
# e1 = Employee("Alice")
# e2 = Employee("Bob")
#
# print(e1.company)  # TechCorp
# print(e2.company)  # TechCorp
#
# Employee.set_company("OpenAI")  # Class method call to change the company name
#
# print(e1.company)  # OpenAI
# print(e2.company)  # OpenAI

#---------------------------------------------------------------------------------------------------
#inheritance
#single
# class A:
#     var_a=10
# class B(A):
#     pass
#     def cc(self):
#         print(self.var_a)#within a method in B
#     #print(var_a)
# b=B()
# b.cc()
# print(B.var_a)#Using the class name directly
# print(b.var_a)#Using an instance of B
#---------------------------------------------------------------------------------------------------
#Multilevel Inheritance
# class Grandparent:
#     def greet(self):
#         print("Hello from Grandparent")
#
# class Parent(Grandparent):
#     def welcome(self):
#         print("Hello from Parent")
#
# class Child(Parent):
#     def say_name(self):
#         print("I am Child")
#
# c = Child()
# c.greet()
# c.welcome()
# c.say_name()
#---------------------------------------------------------------------------------------------------------------
#3. Hierarchical Inheritance
# class Parent:
#     def greet(self):
#         print("Hello from Parent")
#
# class Child1(Parent):
#     pass
#
# class Child2(Parent):
#     pass
#
# c1 = Child1()
# c2 = Child2()
# c1.greet()
# c2.greet()
#---------------------------------------------------------------------------------------------------------------
#Multiple Inheritance
# class Father:
#     def skills(self):
#         print("Coding")
#
# class Mother:
#     def hobbies(self):
#         print("Painting")
#
# class Child(Father, Mother):
#     def cc(self):
#         print(self.skills(),self.hobbies())
#
# c = Child()
# c.cc()
#---------------------------------------------------------------------------------------------------------------
#Hybrid Inheritance
# class A:
#     def method_A(self):
#         print("A")
#
# class B(A):
#     def method_B(self):
#         print("B")
#
# class C(A):
#     def method_C(self):
#         print("C")
#
# class D(B, C):  # Hybrid: D inherits from both B and C, which inherit from A
#     def method_D(self):
#         print("D")
#
# d = D()
# d.method_A()
# d.method_B()
# d.method_C()
# d.method_D()
#---------------------------------------------------------------------------------------------------------------
#super -super() is a built-in method which is useful to call the super class constructors,variables
#and methods from the child class
# class P:
#     a=10
#     def __init__(self):
#         print("parent")
#     def call(self):
#         print("parent function")
# class C(P):
#     def call1(self,var):
#         self.var=var
#         self.call()
#         super().call()
#         super().__init__()
#         print(super().a)#-------------------**************-----------
# c=C()
# c.call1(4)
#---------------------------------------------------------------------------------------------------------------
# Overloading
# 1) Operator Overloading
# 2) Method Overloading
# 3) Constructor Overloading
# print(10+20)#30
# print('durga'+'soft')

#So even though you did not use the word self, the first parameter (a) still receives the instance, and the second argument (10) goes to b.
# class test:
#     def method_overloading(a,b=None):#eventhough we are not declare self it take a as self ---------------------------------****************------------------------
#         print(b)
# a=test()
# a.method_overloading(10)#a value is self assign b=10


#example
# class Greet:
#     def hello(a,aa):
#         a.aa=aa
#     def gg(a):
#         print(a.aa)
# g = Greet()
# g.hello("John")
# g.gg()

#---------------------------------------------------------------------------------------------------------------
#overloading
#Python does not support true method overloading like Java or C++, but you can achieve similar behavior using default arguments or *args and **kwargs.
# class Greet:
#     def hello(self, name=None):
#         if name:
#             print(f"Hello, {name}")
#         else:
#             print("Hello")
#
# g = Greet()
# g.hello()        # Output: Hello
# g.hello("John")  # Output: Hello, John

#usig args,kwargs
# class Calculator:
#     def add(self, *args, **kwargs):
"""It allows you to pass a variable number of positional (non-keyword) arguments to a function.
It allows you to pass a variable number of keyword arguments (i.e., key=value) to a function.eg c.add(a=100, b=200)"""
#         total = 0
#         # Sum positional arguments
#         for num in args:
#             total += num
#         # Sum keyword arguments
#         for key in kwargs:
#             total += kwargs[key]
#         print("Sum is:", total)
# c = Calculator()
# c.add(1, 2, 3, 4, 5)  # Output: 15
# c.add(10, 20, a=5, b=15)  # Output: 50

#---------------------------------------------------------------------------------------------------------------
# Constructor Overloading (Simulated)Python does not support multiple __init__ methods. You can simulate constructor overloading using default parameters or *args.
# class Demo:
#     def __init__(self, a=None, b=None):#or using def __init__(self, *args):
#         if a is not None and b is not None:
#             print("Two arguments:", a, b)
#         elif a is not None:
#             print("One argument:", a)
#         else:
#             print("No arguments")
# d1 = Demo()
# d1 = Demo(10)
# d1 = Demo(10, 20)



#---------------------------------------------------------------------------------------------------------------
#3) Overriding
#1) Method Overriding
# class Parent:
#     def show(self):
#         print("Parent method")
#
# class Child(Parent):
#     def show(self):  # Overrides parent's show()
#         print("Child method")
#
# c = Child()
# c.show()  # Output: Child method

# 2) Constructor Overriding
# class Parent:
#     def __init__(self):
#         print("Parent Constructor")
#
# class Child(Parent):
#     def __init__(self):
#         print("Child Constructor")
#
# c = Child()  # Output: Child Constructor




#---------------------------------------------------------------------------------------------------------------
"""Abstract Method:
 Sometimes we don't know about implementation, still we can declare a method. Such
types of methods are called abstract methods.i.e abstract method has only declaration
but not implementation.
 In python we can declare abstract method by using @abstractmethod decorator as
follows."""

# from abc import *
# class Fruit:
#     @abstractmethod
#     def taste(self):
#         pass
# a=Fruit()
# print(a.taste())

"""Abstract class:
Some times implementation of a class is not complete,such type of partially
implementation classes are called abstract classes. Every abstract class in Python should
be derived from ABC class which is present in abc module.
Abstract classes cannot be instantiated directly."""

#1-----example abstract class with abstract method
# from abc import *
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
#
# # a = Animal()  # ❌ Error: Can't instantiate abstract class
# d = Dog()
# c=Cat()
# print(c.sound())#Meow
# print(d.sound())  # ✅ Output: Bark



#2--abstract class without abstract method
# from abc import ABC
#
# class Animal(ABC):  # Abstract class, but no abstract methods
#     def speak(self):
#         print("Animal speaking")
#
# a = Animal()  # ✅ Allowed in Python, but usually abstract class has at least one abstract method
# a.speak()

#---------------------------------------------------------------------------------------------------------------
#A concrete method can be:
# | Type                | Concrete? | Needs Implementation? |
# | ------------------- | --------- | --------------------- |
# | **Instance Method** | ✅ Yes     | Yes ✅                 |
# | **Class Method**    | ✅ Yes     | Yes ✅                 |
# | **Static Method**   | ✅ Yes     | Yes ✅                 |

#---------------------------------------------------------------------------------------------------------------


"""First: Abstract Class in Python
An abstract class is a class that:
Can have both abstract and concrete methods
Cannot be instantiated
Is used to provide common behavior + enforce rules
🔸 Example: Abstract Class with Abstract + Concrete Method"""

# from abc import ABC, abstractmethod
#
# class Animal(ABC):  # Abstract class
#     @abstractmethod
#     def sound(self):  # Abstract method
#         pass
#
#     def sleep(self):  # Concrete method
#         print("Sleeping...")  # Common behavior for all animals
#
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
#
# d = Dog()
# d.sound()      # Output: Bark
# d.sleep()      # Output: Sleeping...

#interface
"""Second: Interface in Python (using Abstract Class with ONLY Abstract Methods)
An interface is:
A class with only abstract methods
Acts like a blueprint or contract
Child classes must implement all methods
🔸 Example: Interface-like Class"""

# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):  # Interface
#     @abstractmethod
#     def start(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#     def start(self):
#         print("Car started")
#
#     def stop(self):
#         print("Car stopped")
#
# c = Car()
# c.start()   # Output: Car started
# c.stop()    # Output: Car stopped



"""Concreate class vs Abstract Class vs Inteface:
1) If we dont know anything about implementation just we have requirement
specification then we should go for interface.
2) If we are talking about implementation but not completely then we should go for
abstract class. (partially implemented class).
3) If we are talking about implementation completely and ready to provide service then
we should go for concrete class."""

#---------------------------------------------------------------------------------------------------------------
"""Public, Protected and Private Attributes:
By default every attribute is public. We can access from anywhere either within the class
or from outside of the class.
Eg: name = 'durga'
Protected attributes can be accessed within the class anywhere but from outside of the
class only in child classes. We can specify an attribute as protected by prefexing with _
symbol.
Syntax: _variablename = value
Eg: _name='durga'
But is is just convention and in reality does not exists protected attributes.
private attributes can be accessed only within the class.i.e from outside of the class we
cannot access. We can declare a variable as private explicitly by prefexing with 2
underscore symbols.
syntax: __variablename=value"""

# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name           # public
#         self._age = age            # protected (by convention)
#         self.__salary = salary     # private (name mangling)
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self._age)
#         print("Salary:", self.__salary)
# p = Person("Alice", 30, 50000)
# # Accessing public attribute
# print(p.name)        # ✅ Accessible
# # Accessing protected attribute
# print(p._age)        # ⚠️ Accessible but should be treated as protected
# # Accessing private attribute
# # print(p.__salary)  ❌ Error: AttributeError
# # Correct way to access private variable (if needed)
# print(p._Person__salary)  # ✅ Name mangling allows access
#

# Example of Protected Attributes
# class Animal:
#     def __init__(self, name):
#         self._name = name  # Protected attribute
#
#     def speak(self):
#         print(f"{self._name} is speaking.")
#
# class Dog(Animal):
#     def speak(self):
#         print(f"{self._name} barks.")
#
# # Main program
# dog = Dog("Buddy")
# dog.speak()  # Accesses _name through inheritance



#---------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#__str__
#__str__ is a built-in method in Python.
#It is called when you pass an object to print() or use str() on the object.
#It returns a string that should be a readable, user-friendly description of the object.
# class Point:
#     def __init__(self, x):
#         self.x = x
#
#     def __str__(self):
#         return f"Point({self.x})"
#
# p = Point(10)
# print(p)       # Calls p.__str__() internally
# print(str(p))  # Same as above

#---------------------------------------------------------------------------------------------------------------

# Step 1: Create a custom exception class
# class MyCustomException(Exception):
#     def __init__(self, message="An error occurred"):
#         super().__init__(message)
#
# # Step 2: Function that validates string length
# def check_string(s):
#     if len(s) < 10 or len(s) < 20:
#         raise MyCustomException("String must be at least 20 characters long.")
#
# # Step 3: Use a try-except block to catch all exceptions through MyCustomException
# def main():
#     test_string = "short one"  # Try changing this to test
#
#     try:
#         check_string(test_string)
#         print("String is valid.")
#     except MyCustomException as e:
#         print("Caught a custom exception:", e)
#
# if __name__ == "__main__":
#     main()




#---------------------------------------------------------------------------------------------------------------
# def findEvenNumbers(digits):
#     res = []
#     count = 0
#     for i in range(len(digits)):
#         count = 0
#         for j in range(i, i+3):
#             if digits[i] != 0:
#                 print(digits[j])
#                 count = count * 10 + digits[j]
#         print("")
#         res.append(count)
#     #return res
#
# findEvenNumbers([2,1,3,0])
#print(*a)
#---------------------------------------------------------------------------------------------------------------
# words = ['apple', 'kiwi', 'banana', 'fig']
# sorted(words, key=len)            #-----------------------------imp------------------------------------
#
# nums = [7, 2, 9, 4, 1]
# sorted(nums, key=lambda x: x % 3)
#

#---------------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------------
