import random

class HUMAN:

    def __init__(self, age=None, gender=None):
        
        if age is not None:
            self._age = age
        else:
            self._age = random.randint(0, 160)
            random.ran
        if gender is not None:
            self._gender = gender
        else:
            self._gender = random.choice(['female', 'male'])

    def eat(self):
        pass

    def sleep(self):
        pass

    def run(self):
        pass


class STUDENT(HUMAN) :
    def init (self, age=None, gender=None, id=None, grade=None, credits=None) :
        super().init(age, gender)
        
        if id is not None:
            self._id = id
        else:
            self._id = random.randint(0, 9999)
        
        if grade is not None :
            self._grade = grade
        else :
            self._grade = round(random.uniform(0,4.0),1)
        
        if credits is not None :
            self._credits = credits
        else :
            self._credits = random.randint(0,250)

        if age is not None :
            self._age = age 
        else :
            self._age = "Student age {}".format(random.randrange(18, 28))

        if gender is not None :
            self._gender = gender 
        else :
            self._gender = "Student gender {}".format(random.choice(["Male", "Female"]))
    @property
    def id(self):
        return self._id

    @property
    def credits(self):
        return self._credits

    @property
    def grade(self):
        return self._grade
    
    def result(self) :
        if self._grade > 3.8 and self._grade < 4.0 :
            return "A+"
        elif self._grade < 3.5 and self._grade > 3.3 :
            return "A"
        elif self._grade > 3.0 and self._grade < 3.2 :
            return "B+"
        elif self._grade > 2.6 and self._grade < 2.9 : 
            return "B"  
        elif self._grade > 1.8 and self._grade < 2.5 :
            return "C"
        elif self._grade < 1.8 :
            return "D"
    
    def graduate(result, self) :
        if result != "D" and self._credits == 250 :
            return True 
        else:
            return False