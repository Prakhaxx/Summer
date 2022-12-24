people =[
    {"name":"Harry","house":"Gryffindor"},
    {"name": "Cho","house":"Ravenclaw"},
    {"name":"Draco","house":"Slytherin"}
]
#def f(person):
   # return person["name"]
#people.sort(key=f)
people.sort(key=lambda person:person["house"])
# if we not use above way or lamda function we will
#get exception of "type Error'<'"
print(people)