my_family = {
    "father": {
        "name": "Mark",
        "age": 53
    },
    "brother": {
        "name": "Danny",
        "age": 22
    },
    "sister": {
        "name": "Megan",
        "age": 20
    },
    "other sister": {
        "name": "Molly",
        "age": 20
    },
    "mother": {
        "name": "Mary",
        "age": 50
    }
}

for (relation, info) in my_family.items():
    print(f"{info['name']} is my {relation} and is {info['age']} years old.")       