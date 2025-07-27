session_data = [
    {"user_id": "U001", "session_id": 1, "duration": 30, "pages": 5},
    {"user_id": "U001", "session_id": 2, "duration": 20, "pages": 3},
    {"user_id": "U002", "session_id": 1, "duration": 25, "pages": 4},
    {"user_id": "U003", "session_id": 1, "duration": 0, "pages": 0},
    {"user_id": "U002", "session_id": 2, "duration": 45, "pages": 7},
    {"user_id": "U004", "session_id": 1, "duration": 15, "pages": "five"},
    {"user_id": "U005", "session_id": 1, "duration": 35, "pages": 6},
    {"user_id": "U003", "session_id": 2, "duration": 10, "pages": 2},
]

clean_session_data = []
group_by_user = {}
duration = 0
pages = 0
user_statistics = {}

def average(sum,total):
    average_ = round((sum/total),2)
    return average_
    

for data in session_data:
    try:
        data["duration"] = int(data["duration"])
        data["pages"] = int(data["pages"])
        if data["duration"] != 0:
            clean_session_data.append(data)
    except:
        data["duration"] = data["duration"]
        data["pages"] = data["pages"]

for data in clean_session_data:
        if data["user_id"] in group_by_user:
            group_by_user[data["user_id"]].append({"duration": data["duration"],
                     "pages": data["pages"]})
        else:
            group_by_user.update({data["user_id"]: [{"duration": data["duration"],
                     "pages": data["pages"]}]})
    
    
for user,data in group_by_user.items():
    for dat in data:
        duration += dat["duration"]
    session = len(dat) + 1 
    pages += dat["pages"]
    avg = average(pages,session)
    user_statistics.update({user:{
       "total_sessions": session,
       "total_duration": duration,
       "avg_pages": avg
    }})
        
        
        
        
print(user_statistics)
print(group_by_user)
print(clean_session_data)