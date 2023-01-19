# Question 3:

"""Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class."""
class Person:
    def getGender(self):
        pass

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

person = Person()
male = Male()
female = Female()

person.getGender() # will not print anything 
male.getGender() # will print 'Male'
female.getGender() # will print 'Female'
