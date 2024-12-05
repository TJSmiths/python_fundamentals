shopping_list= ["chicken", "beef", "cabbage"] # Create variable shopping_list as a list

print("Your current shopping list is", *shopping_list, sep= ", ") # Print current shopping list, iterates through each item in the list for the print and using a comma as a seperator

while True: # While loop to act as a selection menu
    menu = input("Would you like to add an item, remove an item or close the list? Add/Remove/Close\n").lower()
    if menu == "add": # Operation for if the user decides to add a new item
        new_item = input("Add a new item to the list:\n").lower()
        if new_item in [item.lower() for item in shopping_list]: # If statement to check if the item already exists in the list
            print("Item already in list, please input a different one!")
        else:
            shopping_list.append(new_item)
            print(f"You have added {new_item} to your shopping list!")
    elif menu == "remove": # Operation for if the user decides to remove an item
        print("Your current shopping list is", *shopping_list, sep= ", ")
        removeitem = input("What would you like to remove?\n").lower()
        if removeitem in [item.lower() for item in shopping_list]: # Check item exists in the list in order to remove it
            shopping_list.remove(removeitem)
        else:
            print("That item is not in the list!")
    elif menu == "close": # Operation for if the user decides not to add anything else
        print("Your shopping list is now", *shopping_list, sep= ", ") # Prints updated shopping list, using comma as seperator
        break
    else: # Catch for not inputting correctly 
        print("Please pick an option.")