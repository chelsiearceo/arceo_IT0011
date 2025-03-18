class Item:
    def __init__(self, item_id, name, description, price):
        try:
            if price < 0:
                raise ValueError("Price cannot be negative.")
            self.item_id = item_id
            self.name = name
            self.description = description
            self.price = price
        except ValueError as e:
            print(f"Error: {e}")

    def display(self):
        print(f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}")

class ItemManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, description, price):
        try:
            if item_id in self.items:
                raise KeyError("Item ID already exists.")
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully.")
        except KeyError as e:
            print(f"Error: {e}")

    def view_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                item.display()

    def update_item(self, item_id, name=None, description=None, price=None):
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            if price is not None and price < 0:
                raise ValueError("Price cannot be negative.")
            
            item = self.items[item_id]
            if name: item.name = name
            if description: item.description = description
            if price is not None: item.price = price
            print("Item updated successfully.")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def delete_item(self, item_id):
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            del self.items[item_id]
            print("Item deleted successfully.")
        except KeyError as e:
            print(f"Error: {e}")

def main():
    manager = ItemManager()
    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                item_id = input("Enter Item ID: ")
                name = input("Enter Name: ")
                description = input("Enter Description: ")
                price = float(input("Enter Price: "))
                manager.add_item(item_id, name, description, price)
            elif choice == "2":
                manager.view_items()
            elif choice == "3":
                item_id = input("Enter Item ID to update: ")
                name = input("Enter new Name (press Enter to skip): ") or None
                description = input("Enter new Description (press Enter to skip): ") or None
                price_input = input("Enter new Price (press Enter to skip): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name, description, price)
            elif choice == "4":
                item_id = input("Enter Item ID to delete: ")
                manager.delete_item(item_id)
            elif choice == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter the correct data type.")

if __name__ == "__main__":
    main()