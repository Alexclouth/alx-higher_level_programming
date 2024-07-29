#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("/home/lazarus/alx-higher_level_programming/0x0B-python-input_output/add_item.json")
    except FileNotFoundError:
        pass
    items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "/home/lazarus/alx-higher_level_programming/0x0B-python-input_output/add_item.json")
