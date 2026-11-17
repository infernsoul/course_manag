courses = {}

def add_course(name, code, capacity):
    if not name or not code or not capacity:
        return "Error: All fields required"
    if code in courses:
        return "Error: Code exists"
    if int(capacity) <= 0:
        return "Error: Capacity must be > 0"
    courses[code] = {"name": name, "capacity": int(capacity)}
    return "Course added" 

print(add_course("MMAGL", "M101", 30))   
print(add_course("GP", "M101", 20)) 
print(add_course("ART", "A101", 0))    
print(add_course("", "B101", 10))       


