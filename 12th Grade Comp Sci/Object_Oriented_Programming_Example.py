'''
Use this example as a template
'''

class User:
    total_users = 0  # This is a CLASS ATTRIBUTE
    
    '''INIT Method '''
    def __init__(self, first, last, age):
        self._first = first # This is a private regular attribute
        self._last = last # This is a private regular attribute
        self.age = age # This is a non-private regular attribute
        User.total_users += 1  # This modifies the class attribute

    '''REPR Method'''
    # Below is the __repr__ method. This will control
    # what happens if I try to print(User)
    def __repr__(self):
        return f"{self.first} {self.last} is {self.age} years old."


    '''Getters and Setters'''
    # Below are the getter and setter method for the attribute FIRST
    def getFirst(self):
        return self._first
    
    def setFirst(self, new_first):
        self._first = new_first


    # Below are the getter and setter method for the attribute LAST
    def getLast(self):
        return self._last
    
    def setLast(self, new_last):
        self._last = new_last


    # Below are the getter and setter method for the attribute AGE
    def getAge(self):
        return self.age
    
    def setAge(self, new_age):
        self.age = new_age

    

    '''Extra Methods'''

    def age_in_x_years(self, years):
        '''This method takes a number of years and tell you 
        how old you will be in that many years'''
        future_age = self.age + years
        return f"{self.first} will be {future_age} in {years} years"
    
    def yearOfBirth(self, current_year):
        '''This function takes the current year as a parameter and
        returns the year this person was born'''
        year_of_birth = current_year - self.age
        return f"{self.frist} was born in {year_of_birth}"


    