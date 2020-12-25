class Student:

    def __init__(self, name='default', dept='BBA'):
        self.nme = name
        self.dep = dept
       
    def set_department(self, d):
        self.dep = d
       
    def get_name(self):
        return self.nme  
   
    def set_name(self, name):
        self.nme = name
       
    def __str__(self):
        return f'Name: {self.nme} Department: {self.dep}'


class BBA_Student(Student):

    def __init__(self, name='default', dept='BBA'):
        super(name, dept)
     

print(BBA_Student().__str__())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student("Little Bo Peep"))