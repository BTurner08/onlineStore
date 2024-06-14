


students = [

    {

        "first_name": "Alice",

        "last_name": "Smith",

        "age": 20,

        "gender": "Female",

        "preferred_color": "Blue"

    },

    {

        "first_name": "Bob",

        "last_name": "Johnson",

        "age": 22,

        "gender": "Male",

        "preferred_color": "Green"

    },

    {

        "first_name": "Charlie",

        "last_name": "Brown",

        "age": 19,

        "gender": "Male",

        "preferred_color": "Red"

    },

    {

        "first_name": "Diana",

        "last_name": "Miller",

        "age": 21,

        "gender": "Female",

        "preferred_color": "Yellow"

    },

{

        "first_name": "Ethan",

        "last_name": "Davis",

        "age": 23,

        "gender": "Male",

        "preferred_color": "Black"

    },

    {

        "first_name": "Fiona",

        "last_name": "Garcia",

        "age": 20,

        "gender": "Female",

        "preferred_color": "Purple"

    },

    {

        "first_name": "George",

        "last_name": "Martinez",

        "age": 22,

        "gender": "Male",

        "preferred_color": "Orange"

    },

    {

        "first_name": "Hannah",

        "last_name": "Lopez",

        "age": 21,

        "gender": "Female",

        "preferred_color": "Pink"

    },

{

        "first_name": "Ian",

        "last_name": "Gonzalez",

        "age": 19,

        "gender": "Male",

        "preferred_color": "White"

    },

    {

        "first_name": "Jessica",

        "last_name": "Wilson",

        "age": 23,

        "gender": "Female",

        "preferred_color": "Brown"

    }

]
[
{

        "first_name": "Ian",

        "last_name": "Gonzalez",

        "age": 19,

        "gender": "Male",

        "preferred_color": "White"

    },

{

        "first_name": "Jessica",

        "last_name": "Wilson",

        "age": 23,

        "gender": "Female",

        "preferred_color": "Brown"

    }
]


# 1 - print each name
for student in students:
    full_name = student["first_name"] + " " + student["last_name"]
    print(full_name)

print("------------")

#2 - print the preferred colors
#2a - of females
for student in students:
    if student ["gender"] == "Female":
        print(student["preferred_color"])

print("------------")

#3 - print ages over 21

for student in students:
    if student ["age"] > 21:
        print(student["first_name"] + " - " + str(student["age"]))

#4 - how many Females and males are there?
females = 0
males = 0
for student in students:
    if student ['gender'] == "Female":
        females += 1

    if student ['gender'] == "Male":
        males += 1

print("There are " + str(females) + " females")
print("There are " + str(males) + " males")