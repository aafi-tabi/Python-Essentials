purchase_history = [
    {"user": "U01", "week": 1, "city": "Lahore", "amounts": [200, 500, 100]},
    {"user": "U02", "week": 1, "city": "Karachi", "amounts": [600, "error", 700]},
    {"user": "U01", "week": 2, "city": "Lahore", "amounts": [150, 150, 600]},
    {"user": "U03", "week": 1, "city": "Islamabad", "amounts": None},
    {"user": "U02", "week": 2, "city": "Karachi", "amounts": [900, 950, 1000]},
    {"user": "U04", "week": 1, "city": "Lahore", "amounts": [500]},
    {"user": "U05", "week": 1, "city": "Multan", "amounts": [0, 0, 0]},
    {"user": "U01", "week": 3, "city": "Lahore", "amounts": [400, 100, 800]},
]
def cleaned_data_():
    clean_data = []

    for log in purchase_history:
        try:
            for i in range(len(log["amounts"])):
                log["amounts"][i] = int(log["amounts"][i])
            clean_data.append(log)    
        except:
            continue
    return clean_data

cleaned_data = cleaned_data_()

def build_user_trends_():
    amount = 0
    build_user_trends = {}
    

    for log in cleaned_data:
        if log["user"] in build_user_trends:
            for i in range(len(log["amounts"])):
                amount += log["amounts"][i]
                avg = round(amount/len(log["amounts"]))
                   
            for loge in build_user_trends.values():
                loge["total_amount"] += amount
                loge["weekly_avg"] += avg
                
                
            build_user_trends[log["user"]].update({
              "city": log["city"],
             "total_amount": loge["total_amount"],
             "weeks_active": log["week"],
             "weekly_avg": loge["weekly_avg"],
             "spending_trend": loge["spending_trend"].append(avg)
            })
        else:
            for i in range(len(log["amounts"])):
                amount += log["amounts"][i]
                avg = round(amount/len(log["amounts"]))
            build_user_trends.update({log["user"] : {
             "city": log["city"],
             "total_amount": amount,
             "weeks_active": 1,
             "weekly_avg": avg,
             "spending_trend": [avg]
}
})
    return build_user_trends
        
build_user_trends__ = build_user_trends_()
print(build_user_trends__)

# print(cleaned_data)