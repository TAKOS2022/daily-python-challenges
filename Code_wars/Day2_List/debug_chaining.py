"""
Debug the Dinglemouse class to make the following code work:
    - The dinglemouse class has a hello method that returrn string base on the order of the arguments passed to the class constructor.
    - The sex argument can be either 'M' or 'F' and should return Male or Female
Example :
Hello.
Hello. My name is Bob. I am 27. I am male.
Hello. I am 27. I am male. My name is Bob.
Hello. My name is Alice. I am female.
Hello. My name is Batman.
"""

class Dinglemouse(object):
    
    def __init__(self):
        self.name = None
        self.sex  = None
        self.age  = None
    
    def setAge(self, age):
        self.age = age
        return self
        
    def setSex(self, sex):
        self.sex = sex
        return self
        
    def setName(self, name):
        self.name = name
        return self
        
    def hello(self):
        return "Hello. My name is {}. I am {}. I am {}.".format(self.name, self.age, "male" if self.sex=='M' else "female")

"""
knowledge: (Chaining methods)
- Chaining methods is a programming technique where multiple method calls are made on the same object in a single line of code. This is often done by returning the object itself (usually self) from each method, allowing for a more concise and readable syntax.
- In Python, method chaining is commonly used in object-oriented programming to create a fluent interface, where methods can be called in a chain without needing to reference the object multiple times.

example:
- Without chaining:
    obj = MyClass()
    obj.method1()
    obj.method2()
    obj.method3()
- With chaining:
    obj = MyClass().method1().method2().method3()
"""


class Dinglemouse2(object):

    def __init__(self, name=None, age=None, sex=None):
        self.__fields = []
        if name is not None:
            self.setName(name)
        if age is not None:
            self.setAge(age)
        if sex is not None:
            self.setSex(sex)

    def setAge(self, age):
        self.age = age
        if 'age' not in self.__fields:
            self.__fields.append('age')
        return self

    def setSex(self, sex):
        self.sex = sex
        if 'sex' not in self.__fields:
            self.__fields.append('sex')
        return self

    def setName(self, name):
        self.name = name
        if 'name' not in self.__fields:
            self.__fields.append('name')
        return self

    def hello(self):
        result = "Hello."
        for field in self.__fields:
            if field == 'name':
                result += " My name is {}.".format(self.name)
            elif field == 'age':
                result += " I am {}.".format(self.age)
            elif field == 'sex':
                result += " I am {}.".format("male" if self.sex == 'M' else "female")
        return result

        
 

mouse = Dinglemouse2("Dingle", 27, "M")
print(mouse.hello())
