


course={
    "name":"software Development Fundamentls",
    "duration": "8 weeks" 
}

print(course);

print(course["name"]);
course["fee"]=1000.00
course["copyright"]="Whitecliffe"

print(course)

course.pop("fee")
print(course)

for x in course:
    print (x,":",course[x])
