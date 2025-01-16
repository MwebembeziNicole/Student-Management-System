class Person:
    def __init__(self,surname,firstname,gender,contact,email,nin_number):
        self.surname = surname
        self.firstname = firstname
        self.gender = gender
        self.contact = contact
        self.email=email
        self.nin_number=nin_number
        
class Student(Person):
    student_database={}
    def __init__(self,surname,firstname,gender,contact,email,nin_number,student_id):     
        super().__init__(surname,firstname,gender,contact,email,nin_number)
        
        self.__student_id = student_id
        
    def register_students(self):
        self.student_database[self.__student_id] = [self.surname,self.firstname,self.gender,self.contact,self.email,self.nin_number]
        
class Teacher(Person):
    teacher_database={}
    def __init__(self,surname,firstname,gender,contact,email,nin_number,teacher_id,course_id):
        super().__init__(surname,firstname,gender,contact,email,nin_number) 
        self.__teacher_id = teacher_id
        self.__course_id = course_id
        
    def register_teachers(self):
        self.teacher_database[self.__teacher_id] = [self.surname,self.firstname,self.gender,self.contact,self.email,self.nin_number,self.__course_id]  
        
    def display_teachers(self):
        # print(f"TEACHER'S INFO:\n") 
        print(f"{self.__teacher_id}:{self.teacher_database[self.__teacher_id][0]}")
        # for key,value in self.teacher_database.items():
        #     print (f"{key}:{value[0]}")        
        # return self.teacher_database            
             
        
        
# Student1=Student("MM","NN","Female",67344,"dif.gmail","23F3877",3)
# Student2=Student("QW","UB","Male",223955,"jed.gmail","BJ782200",5)
# Student1.register_students() 
# print(Student1.student_database)
# Student2.register_students() 
# print(Student2.student_database)
# print()
# print("_______________________________________________________________")
# print()

Teacher1=Teacher("TB","OO","Female",6700025,"bac.gmail","23FD4555",2,102)
Teacher2=Teacher("LW","UU","Male",2231108,"mas.gmail","BJ786681",6,133)
Teacher1.register_teachers()
Teacher2.register_teachers()

# print(Teacher1.teacher_database)
# print(f"6:{Teacher2.teacher_database[6][0]}")
Teacher1.display_teachers()
# Teacher2.register_teachers()
# print(Teacher2.teacher_database)
# print(Teacher2.teacher_database[6][2])
    





     
           
            