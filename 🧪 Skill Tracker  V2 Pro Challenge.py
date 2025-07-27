students = [
    {"name": "Aafi", "skills": "Python, ML, AI"},
    {"name": "Lia", "skills": "python, ai"},
    {"name": "Ali", "skills": "ML, cloud, ai"},
    {"name": "Sara", "skills": "AI, Python"},
    {"name": "Zoya", "skills": "ML, ai, cloud"},
    {"name": "Nora", "skills": "Cloud, DevOps, ML "},
    {"name": "Ray", "skills": " python,  ai,  cybersecurity "},
    {"name": "Areeba", "skills": "AI, Data Analysis, Python"},
    {"name": "Hassan", "skills": "DevOps, CLOUD, Ml, python"},
    {"name": "Zayn", "skills": "Python, ai, ml, Flutter"},
]

python = []
cloud = []
ai= []
ml =[]
d_a=[]
flut =[]
dev = []
cs =[]
python_users = set()
cloud_users = set()
ai_users = set()
ml_users =set()
d_a_users =  set()
flut_users = set()
dev_users = set()
cs_users = set()

students_dic = {}
skill_dic = {}


for student in students:
    student["skills"] = student["skills"].lower() # "skills": "python, ml, ai"
    student["skills"] = student["skills"].split(",") # "skills": [python, ml, ai]
    for i in range(len(student["skills"])):
        student["skills"][i] = student["skills"][i].strip()
        student["skills"][i] =student["skills"][i].split()
        student["skills"][i] = "".join(student["skills"][i])
        if student["skills"][i] == "python":
            python.append(student["skills"][i])
            python_users.add(student["name"]) 
        elif student["skills"][i] == "ai":
            ai.append(student["skills"][i])
            ai_users.add(student["name"]) 
        elif student["skills"][i] == "ml":
            ml.append(student["skills"][i])
            ml_users.add(student["name"])
        elif student["skills"][i] == "dataanalysis":
            d_a.append(student["skills"][i])
            d_a_users.add(student["name"])
        elif student["skills"][i] == "cloud":
            cloud.append(student["skills"][i])
            cloud_users.add(student["name"])
        elif student["skills"][i] == "flutter":
            flut.append(student["skills"][i])
            flut_users.add(student["name"])
        elif student["skills"][i] == "cybersecurity":
            cs.append(student["skills"][i])
            cs_users.add(student["name"])
        else:
            dev.append(student["skills"][i])
            dev_users.add(student["name"])
            
    
    
for student in students:
    students_dic.update({student["name"] : student["skills"]})


skill_dic ={
    "python" : python_users,
    "data analysis" : d_a_users,
    "ml" : ml_users,
    "ai" :ai_users,
    "flutter" : flut_users,
    "cybersecurity" :cs_users,
    "cloud" : cloud_users,
    "devops" :dev_users
    
}

skill_counts = [
    ("python", len(python_users)),
    ("ml", len(ml_users)),
    ("ai", len(ai_users)),
    ("cloud", len(cloud_users)),
    ("data analysis", len(d_a_users)),
    ("flutter", len(flut_users)),
    ("devops", len(dev_users)),
    ("cybersecurity", len(cs_users))
]

skill_counts.sort(key=lambda x: x[1], reverse=True)
most_common = skill_counts[0]

print(f"📢 Most students are learning {most_common[0].title()} with {most_common[1]} students!")
  
    
print(f"\n{students}")
print("\nstudents dictionary is")
print(students_dic)
print("\nskills dictionary is")
print(skill_dic)