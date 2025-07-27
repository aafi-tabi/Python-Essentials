students = [
    {"name": "Aafi", "skills": "Python, ML, AI"},
    {"name": "Lia", "skills": "python, ai"},
    {"name": "Ali", "skills": "ML, cloud, ai"},
    {"name": "Sara", "skills": "AI, Python"},
    {"name": "Zoya", "skills": "ML, ai, cloud"}
]

python = []
ai = []
ml = [] 
cloud = []

python_users = set()
ai_user= set()
ml_user = set()
cloud_user = set()

for student in students:
    skills = student["skills"].lower() # lowercase all skills(string) skills: "python, ml, ai"
    skills_ = skills.split(",") # split each student skills into list skills: [python, ml, ai]
    for i in range(len(skills_)):
        skills_[i] = skills_[i].strip()
        if skills_[i] == "python":
            python.append(skills_[i])
            python_users.add(student["name"])
        elif skills_[i] == "ml":
            ml.append(skills_[i])
            ml_user.add(student["name"])
        elif skills_[i] == "cloud":
            cloud.append(skills_[i])
            cloud_user.add(student["name"])
        else:
            ai.append(skills_[i])
            ai_user.add(student["name"])
        
        
        
if len(python) >len(ai) and len(python) > len(ml) and len(python) > len(cloud):
    print("more students are learning python")
elif len(ai) >len(ai) and len(ai) > len(ml) and len(ai) > len(python):
    print("more students are learning AI")
elif len(ml) >len(ai) and len(ml) > len(cloud) and len(ml) > len(python):
    print("more students are leaning  ML")
elif len(cloud) >len(ai) and len(cloud) > len(ml) and len(cloud) > len(python):
     print("more students are leaning  Cloud")
else:
     print("same numbers of students are leaning two or more same feilds")
        
            
            
    # for i in range(len(skills_list)):
    #         for j in range(len(skills_list[i])):
    #             if len(skills_list[i]) > leng:
    #                 leng = len(skills_list[i])
       
    
# print(f"{skills_list[i]} has {leng} users")     
             
             
skills_user = {
  "python": list(python_users),
  "ai": list(ai_user),
  "ml" : list(ml_user),
  "cloud" : list(cloud_user)
  
}

# print(python)
# print(ai)
# print(ml)
# print(cloud)
print("\npython learning student are",python_users)

print("ai learning students are",ai_user)

print("cloud learning students are",cloud_user)

print("ml learning students are",ml_user)

print("\nskills user dic is")
print(skills_user)