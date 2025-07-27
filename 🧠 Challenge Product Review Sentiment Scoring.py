reviews = [
    {"id": 1, "text": "Amazing product! Loved it. 5 stars", "score": 5},
    {"id": 2, "text": "bad quality, not worth the price", "score": 2},
    {"id": 3, "text": "Okay okay product. Decent but not wow", "score": 3},
    {"id": 4, "text": "Worst purchase ever. 1 star only", "score": 1},
    {"id": 5, "text": "Good value for money!", "score": 4}
]

def normalized_score(score,min_,max_):
    norm  = (score - min_)/(max_ - min_)
    return norm

def grading_score(normalized__score):
    if normalized__score >= 0.7:
        label = "positive"
        return label
    elif 0.4 <= normalized__score < 0.7:
        label = "neutral"
        return label
    else:
        label = "negative"
        return label
 
def counting_text(text):
    lenght = len(text)  
    return lenght  

def sentiment(text):
    words = ["worst" ,"bad"]
    for word in words:
        if word in text:
            return "toxic"
    return "amazing"
        
def count_sentiment_neg(text):
    bad = text.count("bad")
    worst = text.count("worst")
    return bad + worst
    
def count_sentiment_pos(text):
    good = text.count("good")
    amazing  = text.count("amazing")
    love = text.count("love")
    perfect = text.count("perfect")
    return good + love + amazing + perfect

def dominant_tone_(pos_score,neg_score):
    if pos_score < neg_score: 
        return "toxic"
    elif neg_score < pos_score:
        return "positive"
    elif neg_score == pos_score:
        return "neutral"
    elif pos_score > 0 and neg_score > 0 and pos_score  ==  neg_score:
        return "mixed"
    else:
        return "neutral"
    
    
def suspicous(sentiment,score):
    if sentiment == "toxic" and (score == 4 or score == 5):
        return True
    elif sentiment == "amazing" and (score == 1 or score == 2):
        return True
    else:
        return False
    
def count_reviews_(text):
    count  = len(text)
    if count < 4:
        return "too short"
    else:
        return "okay"
        
       

scores = []

for review in reviews:
        scores.append(review["score"])
              
max_ = max(scores)
min_ = min(scores)

for review in reviews:
    norm = normalized_score(review["score"],min_,max_)
    review["normalized_score"] = norm
    
feature_list  = []

    
for review in reviews:
    label = grading_score(review["normalized_score"])
    review["label"] = label
    lenght = counting_text(review["text"])
    review["counting_text"] = lenght
    lower_ =review["text"].lower()
    sentiment_ = sentiment(lower_)
    review["sentiment"] = sentiment_
    senti_ = lower_.replace(","," ").split()
    count_senti_neg = count_sentiment_neg(senti_)
    review["toxicity_score"] = count_senti_neg
    count_senti_pos = count_sentiment_pos(senti_)
    review["positivity_score"] = count_senti_pos
    dominant_tone = dominant_tone_(review["positivity_score"],review["toxicity_score"])
    review["dominant tone"] = dominant_tone
    suspicous_ = suspicous(review["sentiment"],review["score"])
    review["suspicous"]  = suspicous_
    count_reviews = count_reviews_(senti_)
    review["short_reviews"] = count_reviews
    feature_list.append({"norm_score" : review["normalized_score"],
                               "toxity score" : review["toxicity_score"],
                               "pos score" :     review["positivity_score"],
                               "token count" : review["sentiment"],
                                "dominant tone" : review["dominant tone"],
                                "label" : review["label"]
                               })
    
            
print(reviews)
print(feature_list)