students = [
    {"name": "Aafi", "score": "92"},
    {"name": "Lia", "score": "76"},
    {"name": "Zoya", "score": "not available"},
    {"name": "Sara", "score": None},
    {"name": "Ali", "score": "88"}
]

valid_score = []  # list containing valid scores
marks = 0



for student in students:
    try:
        student["score"] = int(student["score"]) # convert the scores into int (if possibie)
        valid_score.append(student["score"])
        
    except:
        student["score"] = None  # given scores cannot converted into int so they will convert into avg of valid marks(None)
        
for i in range(len(valid_score)): # to get avg of valid marks (total marks)
    marks += valid_score[i]
    

average =  marks/len(valid_score)  # average of marks
print(average)

for student in students:
    if student["score"] is None:
         student["score"] = average
         
         

        
print(students)




excellent = []
good = []
improve =[]


for student in students:
    if student["score"] >= 90:
        excellent.append(student["name"])
    elif 70 <= student["score"] <= 89: 
        good.append(student["name"])
    else:
        improve.append(student["name"])
        
        
grading = {
  "Excellent": excellent,
  "Good": good,
  "Needs Improvement": improve
}



print(f"excellent students are {excellent}")  
print(f"good students are {good}")   
print(f"student who need improvement are {improve}")   
        
    

# print(students)
print(f"valid scores are{valid_score}")
print(grading)


        