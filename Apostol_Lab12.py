def display_menu(): # Display the menu
    num_food_menu = 1

    print("\n=== Menu ===")
    for item in food_menu:
        print(f"{num_food_menu}. {item['name']}: ${item['price']}")
        num_food_menu += 1
    print()

def select_item(): # Choose their desired item
    while True:
        choice = int(input("Enter the number of your choice: "))
        if 1 <= choice <= len(food_menu):
            return food_menu[choice - 1]
        else:
            print(f"Invalid choice! Please choose a number between 1 and {len(food_menu)}.")

def payment_process(): # Processing time!
    while True:
        cash = float(input(f"Enter cash amount: "))
        if cash >= cost:
            change = cash - cost
            return change
        else:
            print("Insuffient cash. Please try again.")

food_menu = [
    {
        "name": "Isaw",
        "price": 15.0
    },

    {
        "name": "Balut",
        "price": 35.0
    },

    {
        "name": "Gulaman drink",
        "price": 10.0
    },

    {
        "name": "Taho",
        "price": 20.0
    },

    {
        "name": "Banana Cue",
        "price": 15.0
    }
]


# Main Program
print("Hello, Welcome to Jayphie's!")

# Display menu
display_menu()

# Choose their desired food item
selected_item = select_item()
print(f"You have selected {selected_item['name']} - ${selected_item['price']}")

# Payment and calculation
cost = selected_item['price']
change = payment_process()

# Dispplay results
print(f"\n=== Order Summary ===")
print(f"Selected item: {selected_item['name']}")
print(f"Total: ${cost}")
print(f"Change: ${change}")
print("Thank you for your order!")
