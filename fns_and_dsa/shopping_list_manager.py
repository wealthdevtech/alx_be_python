def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            user_item = input("Enter an item: ").lower()
            shopping_list.append(user_item)
        elif choice == '2':
            # Prompt for and remove an item
            user_item = input("What item do you want to remove?")
            if user_item in shopping_list:
                shopping_list.remove(user_item)
            else:
                print("Item doesn't exist!")
        elif choice == '3':
            # Display the shopping list
            if len(shopping_list) == 0:
                print("List is empty!")
            else:
                print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()