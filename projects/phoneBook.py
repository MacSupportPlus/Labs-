phonebook_dic = {
    "Alice": "703-493-1834",
    "Bob" : "857-384-1234",
    "Elizabeth": "484-584-2923"
}
# Functions start here
def UserQuestion():
    userInput = int(input(f""" What would you like to do?
1. Look up an entry
2. Add a new entry
3. Delete an entry
4. Listing all the entries
5. Quit phonebook
"""))
    return userInput
def setEntry():
    lookup_name = input("Who do you want to look up? >> ")
    result = phonebook_dic[lookup_name]
    print(result)
def addEntry():
    new_user = input("so you want to add a new name to the phone book? who do you want to add? >> ")
    new_number = input("what is their phone number? >> ")
    phonebook_dic [f"{new_user}"] = f"{new_number}"
    print(phonebook_dic)
def deleteEntry():
    delete_entry = input("Who do you want to delete from the phone book? >> ")
    del phonebook_dic[f"{delete_entry}"]
    print(phonebook_dic)
    print(f"You have no deleted {delete_entry} from the phonebook")
def listAllEntry():
    print("You can find all the entries currently in the phone book below")
    print(phonebook_dic)
# Main Code
userInput = input(f""" What would you like to do? ******
1. Look up an entry
2. Add a new entry
3. Delete an entry
4. Listing all the entries
5. Quit phonebook
""")
choice = int(userInput)
while True:
    if choice == 1 :
        setEntry()
        choice = UserQuestion()
    elif choice == 2:
        addEntry()
        choice = UserQuestion()
    elif choice == 3:
        deleteEntry()
        choice = UserQuestion()
    elif choice == 4:
        listAllEntry()
        choice = UserQuestion()
    elif choice == 5 :
        print("You have now exited the phonebook")
        break