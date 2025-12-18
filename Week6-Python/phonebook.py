people = {
    "Carter": "+1-353-546-1999",
    "David": "+1-345-664-2345"
}

name = input("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")