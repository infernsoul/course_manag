students = {}

def register_student(name, student_id, email):
    if name == "" or student_id == "" or email == "":
        return "Error: all fields are required"

    if student_id in students:
        return "Error: student ID already exists"

    if "@" not in email or "." not in email:
        return "Error: invalid email"

    students[student_id] = {"name": name, "email": email}
    return "Student added"


print(register_student("malek", "S001", "malekziat@gmail.com"))    
print(register_student("ikram", "S001", "ikokimouch@gmail.com"))  
print(register_student("khadija", "S002", "khadija.com"))      
print(register_student("", "S003", "mm@com"))          