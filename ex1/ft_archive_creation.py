#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_archive_creation.py <file>\n")
        exit()
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        # --- FILE OPEN ---
        file: typing.IO = open(sys.argv[1], "r")
        # --- FILE READ ---
        content = file.read()
        print("---\n")
        print(content)
        print("\n---")
        # --- FILE CLOSE ---
        file.close()
        print(f"File '{sys.argv[1]}' closed.\n")
        # --- TRANSFORMING FILE ADDED '#' ---
        print("Transform data:")
        print("---\n")
        lines = content.split('\n')
        for line in lines:
            new_line = line + '#'
            print(new_line)
        print("\n---")
        # --- ENTERING INPUT FOR NEW FILE NAME ---
        new_input = input("Enter new file name(or empty):")
        print(new_input)
        if new_input:
            file.write()
            print(f"Saving data to '{new_input}'")
            print(f"Data saved in file '{new_input}'")
        else:
            print("Not saving data.")
    except FileNotFoundError as a:
        print(f"Error opening file '{sys.argv[1]}': {a}\n")
    except PermissionError as b:
        print(f"Error opening file '{sys.argv[1]}': {b}\n")


if __name__ == "__main__":
    main()
