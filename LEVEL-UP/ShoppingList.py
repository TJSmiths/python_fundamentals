shopping_list= ["chicken", "beef", "cabbage"] # Create variable shopping_list as a list

print("Your current shopping list is", *shopping_list, sep= ", ") # Print current shopping list, iterates through each item in the list for the print and using a comma as a seperator

while True: # While loop to allow multiple entries
    retry = input("Would you like to add an item? Y/N\n").lower()
    if retry == "y": # Operation for if the user decides to add a new item
        print("Add a new item to the list")
        new_item= input("add item: ")
        if new_item in shopping_list: # If statement to check if the item already exists in the list
            print("Item already in list, please input a different one!")
        else:
            shopping_list.append(new_item)
            print(f"You have added {new_item} to your shopping list!")
    elif retry == "n": # Operation for if the user decides not to add anything else
        print("Your shopping list is now", *shopping_list, sep= ", ") # Prints updated shopping list, using comma as seperator
        break
    else: # Catch for not inputting correctly 
        print("Please pick an option.")