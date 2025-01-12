def display_menu():
    print("\nshopping List Manager")
    print("1. add item")
    print("2. remove item")
    print("3. view list")
    print("4. exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("enter your choice: ").strip()

        if choice == '1':
            item = input("enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has beem added to the shopping list.")
        elif choice == '2':
            item = input("enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print("f'{item}' has been removed from the shopping list")
            else:
                print(f"'{item}' is not in the shopping list.")
        elif choice == '3':
            if shopping_list:
                print("\ncurrent shopping list; ")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else: 
                print("the shopping list is currently empty.")
        elif  choice == '4':
            print("goodbye!")
            break 
        else: 
            print ("invalid choice. please try again")

if __name__ == "__main__":
    main()
