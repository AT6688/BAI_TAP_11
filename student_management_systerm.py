class Student:
    def __init__(self, st_id, name, dob, adr, cls):
        self.st_id = st_id
        self.name = name
        self.dob = dob
        self.adr = adr
        self.cls = cls
        
    def display_infor(self):
        print("student information: ")
        print("id: ",self.st_id)
        print("name: ", self.name)
        print("date of birth: ", self.dob)
        print("address: ", self.adr)
        print("class: ", self.cls)
        
class Studentlist:
    def __init__(self):
        self.student_list = []
    
    def display_student(self):
        for student in self.student_list:
            student.display_infor()
            
    def add_student(self):
        print("please input student information: ")
        st_id = int(input("student id : "))
        name = input("student name: ")
        dob = input("date of birth: ")
        adr = input("address: ")
        cls = input("class: ")
        new_student = Student(st_id,name,dob,adr,cls)
        self.student_list.append(new_student)
        
    def find_student_by_id(self):
        st_id = int(input("Input student id: "))
        index = -1
        for i in range(len(self.student_list)):
            if self.student_list[i].st_id == st_id:
                index = i
        return index
    
    def find_student_by_name(self):
        name = input("input student name: ")
        result_students = []
        for i in range(len(self.student_list)):
            if self.student_list[i].name == name:
                result_students.append(self.student_list[i])
                
        if len(result_students) == 0:
            print("Not found student name")
            
        else:
            for student in result_students:
                student.display_infor()
                
    def update_student_infor(self, name, dob, adr, cls):
        index_of_student = self.find_student_by_id()
        if index_of_student == -1:
            print("Not found student id")
        else:
            self.student_list[index_of_student].name = name
            self.student_list[index_of_student].dob = dob
            self.student_list[index_of_student].adr = adr
            self.student_list[index_of_student].cls = cls
                
    def delete_student_infor(self):       
        i = self.find_student_by_id()
        del self.student_list[i]


    def sort_student_by_name(self):
        return sorted(self.student_list, key = lambda x: x.name)
    
studentlist = Studentlist()

while True:
    option = int(input("Select function: \n \
                        1. View student information \n \
                        2. Add new student information \n \
                        3. Update student information \n \
                        4. Delete student information \n \
                        5. Find student \n \
                        6. Sort student by name \n \
                        "))
                        
                        
    if option == 1:
        studentlist.display_student()
    elif option == 2:
        studentlist.add_student()
    elif option == 3:
        print("please input student information: ")
        name = input("name: ")
        dob = input("date of birth: ")
        adr = input("address: ")
        cls = input("class: ")
        studentlist.update_student_infor(name,dob,adr,cls)
        
    elif option == 4:
        studentlist.delete_student_infor()
    elif option == 5:
        studentlist.find_student_by_name()
    elif option == 6:
        studentlist.student_list = studentlist.sort_student_by_name()
    else:
        print("Invalid option")
        
    confirm = input("Do you want to continue? Y/N ")
    if confirm.lower() == "n":
        break
        
        
        
        
                       
                       
                
                
                
                
                
                
                
                
                
                
                
                