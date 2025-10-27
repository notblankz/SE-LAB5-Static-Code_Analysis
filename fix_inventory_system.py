"""
This module implements a basic inventory system.
FIX: Added missing module docstring.
"""

import json
# FIX: Removed unused 'logging' import
from datetime import datetime

# FIX: Removed the 'stock_data = {}' global variable.
# State will now be passed as an argument to functions.


# FIX: Expected 2 blank lines before function definition
# FIX: Renamed function to snake_case (was 'addItem')
# FIX: Added 'stock' as the first argument to operate on.
def add_item(stock, item="default", qty=0, logs=None):
    # FIX: Added missing function docstring
    """Adds an item to the stock data."""

    # FIX: Dangerous default value [] as argument.
    # Initialize a new list inside the function if one isn't provided.
    if logs is None:
        logs = []

    # FIX: Added basic type validation based on the original file's
    # comment about 'addItem(123, "ten")'
    if not isinstance(item, str) or not isinstance(qty, int):
        print(
            f"Error: Invalid type for item ({type(item)}) or "
            f"qty ({type(qty)}). Skipping."
        )
        return

    if not item:
        return

    # FIX: Operate on the passed 'stock' argument
    stock[item] = stock.get(item, 0) + qty

    # FIX: Converted to an f-string for better readability
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


# FIX: Renamed function to snake_case (was 'removeItem')
# FIX: Added 'stock' as the first argument
def remove_item(stock, item, qty):
    """Removes a specified quantity of an item from stock."""
    try:
        # FIX: (W0603) Operate on the passed 'stock' argument
        stock[item] -= qty
        if stock[item] <= 0:
            del stock[item]
    # FIX: Do not use bare 'except'.
    # This now specifically catches KeyError if the item doesn't exist.
    except KeyError:
        pass  # Silently ignore if the item is not in stock


# FIX: Added 'stock' as the first argument
def get_qty(stock, item):
    """Gets the quantity of a specific item."""
    # Robustness fix: Use .get() to return 0 instead of
    # raising a KeyError if the item doesn't exist.
    # FIX: Operate on the passed 'stock' argument
    return stock.get(item, 0)


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
        print(f"Warning: {file} not found. "
              "Starting with empty inventory.")
        return {}  # Return an empty dict if file doesn't exist
    except json.JSONDecodeError:
        print(f"Error: Could not decode {file}. "
              "Starting with empty inventory.")
        return {}


# FIX: Added 'stock' as the first argument
def save_data(stock, file="inventory.json"):
    """Saves the current stock data to a JSON file."""
    # FIX: Use 'with' for resource-allocating operations
    # FIX: Specify 'encoding' when opening files
    with open(file, "w", encoding="utf-8") as f:
        # Added indent=4 for human-readable JSON
        # FIX: Dump the passed 'stock' argument
        json.dump(stock, f, indent=4)


# FIX: Added 'stock' as the first argument
def print_data(stock):
    """Prints a report of all items and their quantities."""
    print("Items Report")
    # FIX: Iterate over the passed 'stock' argument
    for i in stock:
        # FIX: Converted to f-string
        print(f"{i} -> {stock[i]}")


# FIX: Added 'stock' as the first argument
def check_low_items(stock, threshold=5):
    """Returns a list of items below a given stock threshold."""
    result = []
    # FIX: Iterate over the passed 'stock' argument
    for i in stock:
        if stock[i] < threshold:
            result.append(i)
    return result


def main():
    """Main function to run the inventory system demo."""

    # FIX: Removed 'global stock_data'.
    # 'stock' is now a local variable, initialized here.
    stock = load_data()

    # FIX: Pass the local 'stock' variable to all functions
    add_item(stock, "apple", 10)
    add_item(stock, "banana", -2)

    # This invalid call is now gracefully handled by the type check in add_item
    add_item(stock, 123, "ten")

    remove_item(stock, "apple", 3)
    remove_item(stock, "orange", 1)  # Will now silently fail (KeyError caught)

    print(f"Apple stock: {get_qty(stock, 'apple')}")
    print(f"Low items: {check_low_items(stock)}")

    save_data(stock)

    # Re-load data into the local 'stock' variable
    stock = load_data()
    print_data(stock)

    # FIX: Removed dangerous and insecure 'eval' call
    # eval("print('eval used')")
    print("--- End of program ---")


# Added a standard __name__ == "__main__" guard
if __name__ == "__main__":
    main()
