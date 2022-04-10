import json 
fileName = "./data/data.json"

def choices():
    print("""
    1. Add a new record
    2. Edit a record
    3. Delete a record
    4. Search for a record
    5. Show all records
    6. Quit
    """)

def view_data():
    with open(fileName, "r") as f:
        data = json.load(f)
        #print(data)
        i = 0
        for entry in data:
            location    = entry["location"]
            name        = entry["name"]
            workstation = entry["workstation"]
            print (f"Index number: {i}")
            print (f"Location: {location}")
            print (f"Name: {name}")
            print (f"Workstation: {workstation}")
            print("\n")
            i += 1

def delete_data():
    view_data()
    new_data=[]
    with open(fileName, "r") as f:
        data = json.load(f)
        data_lenght = len(data)-1
    print("Enter the index number of the record you want to delete: ")
    delete_option = int(input(f"Select a number between 0 and {data_lenght}: "))
    i = 0
    for entry in data:
        if i == int(delete_option):
            pass
            i += 1
        else:
            new_data.append(entry)
            i += 1
    with open(fileName, "w") as f:
        json.dump(new_data, f, indent = 4)

def add_data():
    item_data = {}
    with open(fileName, "r") as f:
        data = json.load(f)
    location = input("Enter the location: ")
    name = input("Enter the name: ") 
    workstation = input("Enter the workstation name: ")
    data.append({"location": location, "name": name, "workstation": workstation})
    with open(fileName, "w") as f:
        json.dump(data, f, indent = 4)


def edit_data():
    view_data()
    new_data = []
    with open(fileName, "r") as f:
        data = json.load(f)
        data_length = len(data)-1
    print("Enter the index number of the record you want to edit: ")
    edit_option = int(input(f"Select a number between 0 and {data_length}: "))
    i = 0
    for entry in data:
        if i == int(edit_option):
            location                = input("Enter the new location: ") or entry["location"]
            name                    = input("Enter the new name: ") or entry["name"]
            workstation             = input("Enter the new workstation name: ") or entry["workstation"]
            entry["location"]       = location
            entry["name"]           = name
            entry["workstation"]    = workstation
            new_data.append(entry)
            i += 1
        else:
            new_data.append(entry)
            i += 1
    with open(fileName, "w") as f:
        json.dump(new_data, f, indent = 4)

while True:
    choices()
    option = int(input("\nSelect an option: "))
    if option   == 1:
        add_data()      # Add a new record
    elif option == 2:
        edit_data()     # Edit a record
    elif option == 3:
        delete_data()   # Delete a record
    elif option == 4:
        view_data()     # Search for a record
    elif option == 5:
        view_data()     # Show all records
    elif option == 6:
        break
