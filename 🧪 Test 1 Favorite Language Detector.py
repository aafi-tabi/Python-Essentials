students = [
    {"name": "Aafi",
     "languages": "Python, C++, Java"},
    {"name": "Zoya",
     "languages": "python, java"},
    {"name": "Lia",
     "languages": "C++, python"},
    {"name": "Sara",
     "languages": "java, python"},
    {"name": "Ali",
     "languages": "C++"},
]

python = []
java= []
c =[]

for student in students:
    languages_ =  student["languages"]
    languages = languages_.split(",") # list of languages
    student["languages"] = languages
    for i in range(len(student["languages"])):
        student["languages"][i] = student["languages"][i].strip().lower()
        if student["languages"][i] == "python":
            python.append(student["languages"][i])
        elif student["languages"][i] == "c++":
            c.append(student["languages"][i])
        else:
            java.append(student["languages"][i])
        

print(python)
print(java)
print(c)



for i in range(len(student["languages"])):
    if len(python) > len(c) and len(python) > len(java):
        print("most students are learning python")
    elif len(c) > len(python) and len(c) > len(java):
        print("most student are learning c++")
    else:
         print("most students are learning a java")
         
python_list = []
c_list = []
java_list = []

for student in students:
    for i in range(len(student["languages"])):
        if student["languages"][i] == "python":
            python_list.append(student["name"])
        elif student["languages"][i] == "java":
            java_list.append(student["name"])
        else:
            c_list.append(student["name"])
            
python_list = list(set(python_list))
java_list = list(set(java_list))
c_list = list(set(c_list))



students_languages = {
    "python" : python_list,
    "c++" : c_list,
    "java" : java_list    
}

print(students_languages)
print(students)

    