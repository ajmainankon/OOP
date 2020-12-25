class Student:
    noOfStudents = 0
    def __init__(self, name, student_id, marks):
        Student.noOfStudents += 1
        self.nme = name
        self.sid = student_id
        self.mks = marks
       
    def get_name(self):
        return self.nme
   
    def get_sid(self):
        return self.sid
   
    def get_marks(self):
        return self.mks
   
    def set_name(self, name):
        self.nme = name
       
    def set_sid(self, sid):
        self.student_id = student_id
       
    def set_marks(self, marks):
        self.mks = mks
       

ank = Student('Ankon', '1', '70')
print(f'{ank.get_sid()}. {ank.get_name()} {ank.get_marks()}')
raj = Student('raj', '2', '20')
print(f'{raj.get_sid()}. {raj.get_name()} {raj.get_marks()}')
srk = Student('Khan', '3', '90')
print(f'{srk.get_sid()}. {srk.get_name()} {srk.get_marks()}')
pk = Student('AKhan', '4','12')
print(f'{pk.get_sid()}. {pk.get_name()} {pk.get_marks()}')
lj = Student('Karim', '5', '60')
print(f'{lj.get_sid()}. {lj.get_name()} {lj.get_marks()}')