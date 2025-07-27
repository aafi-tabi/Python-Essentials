users = [
    {"name": "Aafi", "email": "aafi123@gmail.com"},
    {"name": "Zoya Khan", "email": "zkhan@yahoo.com"},
    {"name": "Lia Rose", "email": "lia.rose@data.com"},
    {"name": "Ali", "email": "ali_11@gmail.com"}
]



for user in users:
    user["name"] = user["name"].lower().strip() # name (string)
    user ["name"] = user["name"].split() # due to space in between names, spliting names inta a list
    user ["name"] = "".join(user["name"]) # again joining a name list inta string withot any gap in btw
    name = user ["name"]
    
    
for user in users:
    user["email"] = user["email"].split("@") # making a list a email like [name, ****.com]
    user["email"] = user["email"][1] # converting a [name, ****.com] to a ****.com (string)
    domain = user["email"]
    print(f"{name}@{domain}")
    


    
    
     
    
    
    
