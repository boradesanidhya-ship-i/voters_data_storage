size = int(input("Enter Number of houses in your area "))
Hash_table = [[] for _ in range(size)]

def hash_key(house_no):
    return house_no % size  

def insert_val(house_no, id, name, address, members, age):
    location = hash_key(house_no)
    if len(Hash_table[location]) > 0:
        print("Chaining\n")
    
    record = {
        "House_No": house_no,
        "ID": id,
        "Name": name,
        "Address": address,
        "Age": age,
        "Members": members
    }
    Hash_table[location].append(record)

def search_val():
    key = int(input("Enter voter id to be searched:\n"))
    for i in range(size):
        for record in Hash_table[i]:
            if record["ID"] == key:
                print(f" Found in House {record['House_No']} (Hash Slot {i}):")
                print(f"  ID: {record['ID']}")
                print(f"  Name: {record['Name']}")
                print(f"  Address: {record['Address']}")
                print(f"  Age: {record['Age']}")
                print(f"  Members: {record['Members']}")
                return
    print(" Element not found")

def delete_val():
    key = int(input("Enter voter ID to be deleted:\n"))
    for i in range(size):
        for record in Hash_table[i]:
            if record["ID"] == key:
                Hash_table[i].remove(record)
                print("Record deleted\n")
                return
    print(" Element doesn't exist")

def display():
    print("\nHash Table Contents:")
    for i in range(size):
        print(f" Hash Slot {i}:")
        if not Hash_table[i]:
            print("  Empty")
        else:
            # Group records by house number
            house_groups = {}
            for record in Hash_table[i]:
                house_no = record["House_No"]
                if house_no not in house_groups:
                    house_groups[house_no] = []
                house_groups[house_no].append(record)

            # Display members of each house with full details
            for house_no, member_list in house_groups.items():
                print(f"House {house_no}:")
                for member in member_list:
                    name = member['Name']
                    age = member['Age']
                    address = member['Address']
                    print(f"  - Name: {name}, Age: {age}, Address: {address}")


while True:
    print("\n1. Insert value in table")
    print("2. Display table")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")
   
    choice = int(input("Enter your choice: "))

    if choice == 1:
        house_no = int(input("Enter house number: "))
        id_mem = int(input("Enter number of members in house: "))
        for i in range(id_mem):
            age_ip = int(input("Enter age:\t"))
            if age_ip >= 18:
                id_input = int(input("Enter voter ID to insert: "))
                name_input = input("Enter name: ")
                address_input = input("Enter address: ")
                insert_val(house_no, id_input, name_input, address_input, id_mem, age_ip)
            else:
                print("Not eligible (under 18)")    
    elif choice == 2:
        display()
    elif choice == 3:
        search_val()
    elif choice == 4:
        delete_val()
    elif choice == 5:
        print("Exited")
        break
    else:
        print("Invalid choice")
