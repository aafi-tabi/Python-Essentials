logs = [
    {"user_id": "U001", "visits": 10, "clicks": 25, "time_spent": 100},
    {"user_id": "U002", "visits": 0, "clicks": 18, "time_spent": 90},
    {"user_id": "U003", "visits": "five", "clicks": 10, "time_spent": 40},
    {"user_id": "U004", "visits": 7, "clicks": None, "time_spent": 60},
    {"user_id": "U005", "visits": 12, "clicks": 30, "time_spent": 150}
]

cleaned_list = []
avg_visits = []
avg_clicks = []
avg_time = []
user_id_score = []
summary_stats = {}
score_ = 0

def logged_scores(clicks,visits,time_spent):
    score = round((clicks / visits) + (time_spent / 10))
    scores = round(score,2)
    return scores

def average(sum,len):
    average_ = sum/len
    return average_

for log in logs:
    try:
        log["visits"] = int(log["visits"])
        log["clicks"] = int(log["clicks"])
        log["time_spent"] = int(log["time_spent"])
        cleaned_list.append(log)
    except:
        log["visits"] = log["visits"]
        log["clicks"] = log["clicks"]
        log["time_spent"] = log["time_spent"]
    
for logs in cleaned_list:
    if logs["visits"] == 0:
        logs["score"] = 0
    else:
        score = logged_scores(logs["clicks"],logs["visits"],logs["time_spent"])
        logs["score"] = score

    
avg_visit = [avg_visits.append(log["visits"]) for log in cleaned_list]
avg_click = [avg_clicks.append(log["clicks"]) for log in cleaned_list]
avg_timee = [avg_time.append(log["time_spent"]) for log in cleaned_list]


sum_visit = sum(avg_visits)
sum_click = sum(avg_clicks)
sum_time = sum(avg_time)

len_visit = len(avg_visits)
len_click = len(avg_clicks)
len_time = len(avg_time)

visit_avg = average(sum_visit,len_visit)
time_avg = average(sum_time,len_time)
click_avg = average(sum_click,len_click)

summary_stats = {"avg_visits" : visit_avg,
                 "avg_timespent" : time_avg,
                 "avg_clicks" : click_avg,
                 "max_score_user" : 00 }


for log in cleaned_list:
    if log["score"] > score_:
        score_ = log["score"]
        summary_stats["max_score_user"] = log["user_id"]
        

cleaned_list_ = sorted(cleaned_list,key= lambda x:x["score"],reverse=True)
print(cleaned_list_)


print(avg_visits)
print(summary_stats)
    
    
print(cleaned_list)
 
  
        

    