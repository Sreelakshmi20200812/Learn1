# Inheritance is the ability to inherit features or attributes from already written classes into newer classes we make.
# Mainly three types of Inheritance. 1. Single inheritance, 2. Multi-level Inheritance, 3. Multiple Inheritance
# Parent1 -> Child1 : Single Inheritance 
# Parent1 -> Child1 -> Child2: Multi- level Inheritance
# Parent1 -> Child2 <- Parent2 : Multiple Inheritance

# Single Inheritance

class parent:                    # Parent class
    def func1(self):
        print ("Hello Parent")

class child(parent):                    # Child class
    def func2(self):
        print ("Hello Child")    
        
# Driver code 
test = child()
test.func1()
test.func2()


# Multiple Inheritance

class parent1:                          # Parent class1
    def func1(self):
        print ("Hello Parent1")
        
class parent2:                          # Parent class2
    def func2(self):
        print ("Hello Parent2")        

class parent3:                          # Parent class3
    def func2(self):                    # function same as that of parent2
        print ("Hello Parent3") 
        
class child(parent1,parent2,parent3):   # Child class
    def func3(self):
        print ("Hello Child")    
        
# Driver code 
test = child()
test.func1()
test.func2()
test.func3()


# Multi-level Inheritance

class grandparent:                          # First level
    def func1(self):
        print ("Hello Grandparent")        

class parent(grandparent):                  # Second level
    def func2(self):                    
        print ("Hello Parent") 
        
class child(parent):                        # Third level
    def func3(self):
        print ("Hello Child")  

# Driver code 
test = child()     # Object created
test.func1()       # Third level calling first level
test.func2()       # Third level calling second level
test.func3()       # Third level calling third level