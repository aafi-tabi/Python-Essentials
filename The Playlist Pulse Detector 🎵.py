import copy
playlist_logs = [
    {"user": "U01", "playlist": [
        {"genre": "lofi", "mood_score": 4},
        {"genre": "pop", "mood_score": 8},
        {"genre": "kpop", "mood_score": 7}
    ]},
    {"user": "U02", "playlist": [
        {"genre": "pop", "mood_score": "vibe"},
        {"genre": "lofi", "mood_score": 3},
        {"genre": "rnb", "mood_score": 6}
    ]},
    {"user": "U03", "playlist": None},
    {"user": "U04", "playlist": [
        {"genre": "kpop", "mood_score": 9},
        {"genre": "kpop", "mood_score": 10}
    ]},
    {"user": "U01", "playlist": [
        {"genre": "rnb", "mood_score": 5},
        {"genre": "lofi", "mood_score": 4}
    ]},
]
def clean_playlist_data_():
    cleanplaylist_data = []

    for log in playlist_logs:
        if log["playlist"] is not None:
            try:
                for i in range(len(log["playlist"])):
                    log["playlist"][i]["mood_score"] = int(log["playlist"][i]["mood_score"])
                cleanplaylist_data.append(log)
            except:
                continue
                
    return cleanplaylist_data

clean_playlist_data = clean_playlist_data_()

def user_profile_():
    user_profile = {} 
    

    for data in clean_playlist_data:
        if data["user"] in user_profile:
            for user,dataa in user_profile.items():
                kpop = dataa["genres"]["kpop"]
                lofi = dataa["genres"]["lofi"]
                rnb = dataa["genres"]["rnb"]
                pop = dataa["genres"]["pop"]
                mood_score = 0
                sum_variance = []
                for i in range(len(data["playlist"])):
                    if data["playlist"][i]["genre"] == "lofi":
                        lofi += 1
                    elif data["playlist"][i]["genre"] == "kpop":
                        kpop += 1
                    elif data["playlist"][i]["genre"] == "rnb":
                        rnb += 1
                    else:
                        pop += 1
                    mood_score += data["playlist"][i]["mood_score"]
                avg = round(mood_score/len(data["playlist"])) 
                for i in range(len(data["playlist"])):    
                    variance_ = (data["playlist"][i]["mood_score"] - avg) ** 2 
                    variance__  = sum_variance.append(variance_)
                sum_variance_ = sum(sum_variance)
                variance = sum_variance_/len(data["playlist"])
                sum_variance.clear()
                user_profile.update({data["user"]: {
             "genres": {"lofi": lofi, "pop": pop, "rnb": rnb,"kpop": kpop},  # count
             "mood_avg": avg + dataa["mood_avg"],
             "mood_variance": variance + dataa["mood_variance"],
             "playlist_length": dataa["playlist_length"] + len(data["playlist"])
    }
    })
        else:
            kpop = 0
            lofi = 0
            rnb = 0 
            pop = 0
            mood_score = 0
            sum_variance = []
            for i in range(len(data["playlist"])):
                if data["playlist"][i]["genre"] == "lofi":
                    lofi += 1
                elif data["playlist"][i]["genre"] == "kpop":
                    kpop += 1
                elif data["playlist"][i]["genre"] == "rnb":
                    rnb += 1
                else:
                    pop += 1
                mood_score += data["playlist"][i]["mood_score"]
            avg = round(mood_score/len(data["playlist"])) 
            for i in range(len(data["playlist"])):    
                variance_ = (data["playlist"][i]["mood_score"] - avg) ** 2 
                variance__  = sum_variance.append(variance_)
            sum_variance_ = sum(sum_variance)
            variance = sum_variance_/len(data["playlist"])
            sum_variance.clear()
            user_profile.update({data["user"]: {
         "genres": {"lofi": lofi, "pop": pop, "rnb": rnb,"kpop": kpop},  # count
         "mood_avg": avg,
         "mood_variance": variance,
         "playlist_length": len(data["playlist"])
}
})
   
    return user_profile

user_profile = user_profile_()
copy_user_profile = copy.deepcopy(user_profile)

def detect_emotion_imbalance():
    for data in user_profile.values():
        if data["mood_variance"] > 6:
            data["emotion"] = "unstable"
        else:
            data["emotion"] = "stable"
            
    return user_profile
            

emotion_imbalance = detect_emotion_imbalance()

def genre_bias_():
    for user_id, data in copy_user_profile.items():
        sorted_genres = sorted(data["genres"].items(), key=lambda x: x[1], reverse=True)
        emotion_imbalance[user_id]["top_genre"] = sorted_genres[0][0]

           
    return emotion_imbalance

genre_bias = genre_bias_()

def score_():
    for data in genre_bias.values():
        data["score"] = (data["playlist_length"] * 10) + data["mood_avg"] - data["mood_variance"]
        
    return emotion_imbalance

score = score_()
copy_score = copy.deepcopy(score)

def final_summary():
    sorted_users = sorted(
        copy_score.items(),
        key=lambda x: (x[1]["score"], x[1]["mood_avg"]),
        reverse=True
    )

    print("🎧 Ranked Listeners:\n")
    for rank, (user_id, data) in enumerate(sorted_users, start=1):
        print(f"Rank {rank}: {user_id}")
        print(f"  Score: {data['score']}")
        print(f"  Top Genre: {data['top_genre']}")
        print(f"  Mood Avg: {data['mood_avg']}")
        print(f"  Mood Variance: {round(data['mood_variance'], 2)}")
        print(f"  Playlist Length: {data['playlist_length']}")
        print(f"  Emotion Status: {data['emotion']}")
        print("-" * 35)


rank = final_summary()


        
        
        
        
    
    
print(clean_playlist_data)
print(user_profile)
print(emotion_imbalance)
print(genre_bias)
print(score)
        