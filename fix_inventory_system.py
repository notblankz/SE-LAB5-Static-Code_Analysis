import json
# FIX: Removed unused 'logging' import
from datetime import datetime

# Global variable
stock_data = {}


# FIX: Expected 2 blank lines before function definition
# FIX: Renamed function to snake_case (was 'addItem')
def add_item(item="default", qty=0, logs=None):
    # FIX: Added missing function docstring
    """Adds an item to the stock data."""

    # FIX: Dangerous default value [] as argument.
    # Initialize a new list inside the function if one isn't provided.
    if logs is None:
        logs = []

    # FIX: Added basic type validation based on the original file's
    # comment about 'addItem(123, "ten")'
    if not isinstance(item, str) or not isinstance(qty, int):
        print(f"Error: Invalid type for item ({type(item)}) or qty ({type(qty)}). Skipping.")
        return

    if not item:
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    
    # FIX: Converted to an f-string for better readability
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


# FIX: Renamed function to snake_case (was 'removeItem')
def remove_item(item, qty):
    """Removes a specified quantity of an item from stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    # FIX: Do not use bare 'except'.
    # This now specifically catches KeyError if the item doesn't exist.
    except KeyError:
        pass  # Silently ignore if the item is not in stock


def get_qty(item):
    """Gets the quantity of a specific item."""
    # Robustness fix: Use .get() to return 0 instead of
    # raising a KeyError if the item doesn't exist.
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Loads the stock data from a JSON file."""
    # FIX: Use 'with' for resource-allocating operations
    # FIX: Specify 'encoding' when opening files
    try:
        with open(file, "r", encoding="utf-8") as f:
            # FIX: Avoid 'global' statement.
            # Return the loaded data instead.
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with empty inventory.")
        return {}  # Return an empty dict if file doesn't exist
    except json.JSONDecodeError:
        print(f"Error: Could not decode {file}. Starting with empty inventory.")
        return {}


def save_data(file="inventory.json"):
    """Saves the current stock data to a JSON file."""
    # FIX: Use 'with' for resource-allocating operations
    # FIX: Specify 'encoding' when opening files
    with open(file, "w", encoding="utf-8") as f:
        # Added indent=4 for human-readable JSON
        json.dump(stock_data, f, indent=4)


def print_data():
    """Prints a report of all items and their quantities."""
    print("Items Report")
    for i in stock_data:
        # FIX: Converted to f-string
        print(f"{i} -> {stock_data[i]}")


def check_low_items(threshold=5):
    """Returns a list of items below a given stock threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Main function to run the inventory system demo."""
    
    global stock_data
    # FIX: 'load_data' no longer uses 'global',
    # so we assign its return value to the module-level 'stock_data'
    stock_data = load_data()

    # FIX: Update all function calls to use new snake_case names
    add_item("apple", 10)
    add_item("banana", -2)
    
    # This invalid call is now gracefully handled by the type check in add_item
    add_item(123, "ten")

    remove_item("apple", 3)
    remove_item("orange", 1)  # Will now silently fail (KeyError caught)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    
    # Re-load data from the file we just saved
    stock_data = load_data()
    print_data()

    # FIX: Removed dangerous and insecure 'eval' call
    # eval("print('eval used')")
    print("--- End of program ---")


# Added a standard __name__ == "__main__" guard
if __name__ == "__main__":
    main()