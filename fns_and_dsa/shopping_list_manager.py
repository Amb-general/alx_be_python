# shopping_list_manager.py

def main():
    """
    Main function to run the shopping list manager.
    """
    shopping_list = []
    
    while True:
        # Display menu
        print("\n--- Shopping List Manager ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")
        
        # Get user choice
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            # Add item
            item = input("Enter the item to add: ").strip()
            if item:  # Only add non-empty items
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Cannot add empty item.")
                
        elif choice == "2":
            # Remove item
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
            else:
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print(f"'{item}' is not in your shopping list.")
                    
        elif choice == "3":
            # View list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                    
        elif choice == "4":
            # Exit
            print("Thank you for using the Shopping List Manager!")
            break
            
        else:
            # Invalid choice
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
