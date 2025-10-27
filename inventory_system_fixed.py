"""Inventory Management System - Cleaned and Secure Version"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="inventory_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item with a specified quantity."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning(f"Invalid input types: item={item}, qty={qty}")
        return

    if qty <= 0:
        logging.warning(f"Quantity must be positive for {item}.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    message = f"Added {qty} of {item}"
    logs.append(message)
    logging.info(message)


def remove_item(item, qty):
    """Remove specified quantity of an item."""
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning(f"Invalid remove_item input: {item}, {qty}")
        return

    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
                logging.info(f"{item} removed from stock.")
        else:
            logging.warning(f"Attempted to remove non-existent item: {item}")
    except KeyError as e:
        logging.error(f"Key error while removing item: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")


def get_qty(item):
    """Return the quantity of the given item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Inventory data loaded successfully.")
    except FileNotFoundError:
        logging.warning(f"{file} not found. Starting with empty stock.")
        stock_data = {}
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")


def save_data(file="inventory.json"):
    """Save inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Inventory data saved successfully.")
    except Exception as e:
        logging.error(f"Error saving data: {e}")


def print_data():
    """Display current stock information."""
    print("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return list of items below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution flow."""
    add_item("apple", 10)
    add_item("banana", 5)
    add_item("grapes", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
