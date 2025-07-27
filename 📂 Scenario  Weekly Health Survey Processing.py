survey_data = [
    {"user_id": "U01", "mood": 7, "sleep_hours": 6, "steps_walked": 5000},
    {"user_id": "U02", "mood": 9, "sleep_hours": 8, "steps_walked": 12000},
    {"user_id": "U03", "mood": "good", "sleep_hours": 7, "steps_walked": 7000},
    {"user_id": "U04", "mood": 6, "sleep_hours": None, "steps_walked": 3000},
    {"user_id": "U05", "mood": 8, "sleep_hours": 9, "steps_walked": 15000},
    {"user_id": "U06", "mood": 5, "sleep_hours": 6, "steps_walked": "eight thousand"},
]

clean_survey_data = []
mood = []
sleep = []
steps = []
scores = 0

def wellness_score(mood,sleep_hours,steps_walked):
    score_ = round((mood * 2) + (sleep_hours * 1.5) + (steps_walked / 1000) , 2)
    return score_

def sum_(score):
    scores = sum(score)
    return scores

def average_(sum,len):
    average =  sum/len
    return average
    
def categorize_users(score):
    if score >= 25:
        return "Excellent"
    elif 20 <= score <= 24.99:
        return "Good"
    elif 15 <= score <= 15.99:
        return "Average"
    else:
        return "Poor"
    
    
for data in survey_data:
    try:
        data["mood"] = int(data["mood"])
        data["sleep_hours"] = int(data["sleep_hours"])
        data["steps_walked"] = int(data["steps_walked"])
        clean_survey_data.append(data)
    except:
        data["mood"] = data["mood"]
        data["sleep_hours"] = data["sleep_hours"]
        data["steps_walked"] = data["steps_walked"]
    
for data in clean_survey_data:  
    score  = wellness_score(data["mood"],data["sleep_hours"],data["steps_walked"])
    data["score"] = score
    data["categeory"] =  categorize_users(score)
      
sleep_ = [sleep.append(data["sleep_hours"]) for data in clean_survey_data]  
mood_ = [mood.append(data["mood"]) for data in clean_survey_data]     
steps_ = [steps.append(data["steps_walked"]) for data in clean_survey_data]

sum_sleep = sum_(sleep)
sum_mood = sum_(mood)
sum_steps = sum_(steps)

len_sleep = len(sleep)
len_mood = len(mood)
len_steps = len(steps)
    
avg_sleep = average_(sum_sleep,len_sleep)
avg_mood = average_(sum_mood,len_mood)
avg_steps = average_(sum_steps,len_steps)

sort = sorted(clean_survey_data,key=lambda x:x["score"], reverse=True)
user_id = sort[0]["user_id"]

summary = {"average_mood" : avg_mood,
           "average_sleep" : avg_sleep,
           "average_steps" : avg_steps,
           "top_user" : user_id}
        
print(sort)
print(clean_survey_data)
print(summary)