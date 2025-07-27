students = [
    {"name": "Aafi", "email": "aafi123@gmail.com"},
    {"name": "Zoya Khan", "email": "zkhan@yahoo.com"},
    {"name": "Lia Rose", "email": "lia.rose@data.com"},
    {"name": "Ali", "email": "ali_11@gmail.com"},
    {"name": "Lia Rose", "email": "lia.rose@data.com"}  # duplicate

]

seen_emails = set()
student_list = []
gmail_users = set()
data_users = set()
yahoo_user = set()


for student in students:
    seen_emails.add(student["email"])
    
for student in students:
    student["name"] = student["name"].lower().strip() # removes left and right spaces and make lowercase a names
    student["name"] = student["name"].split(" ") # split names into list 
    student["name"] = "".join(student["name"]) # joining a name again without spaces in between
    
for student in students:
    student["email"] = student["email"].split("@") # splitting a str email int list ['name', '****.com']
    student["email"] = student["email"][1].split(".") # ['****','com']
    student["email"] = student["email"][0]
    # print(f"{student["name"]}@{student["email"]}")  
    
    username = student["name"] + "@" + student["email"]
    student_list.append((username,student["email"]+".com" ))
    
    if student["email"] == "gmail":
        gmail_users.add(student["name"])
    elif student["email"] == "data":
        data_users.add(student["name"])
    else:
        yahoo_user.add(student["name"])
        

    
print(student_list)
print(f" Yahoo users :{yahoo_user}")
print(f"gmail users :{gmail_users}")
print(f"data users :{data_users}")


if len(yahoo_user) > len(data_users) and len(yahoo_user) > len(gmail_users):
    print("yahoo s most common")
elif len(data_users) > len(yahoo_user) and len(data_users) > len(gmail_users):
    print("data is most common")
elif len(gmail_users) > len(data_users) and len(gmail_users) > len(yahoo_user):
    print("gmail is more common")
else:
    print("two ore more domains are common")

    
    

    
    
