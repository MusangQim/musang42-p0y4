#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_archive_creation.py <file>")
        exit()
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
    except FileNotFoundError as a:
        print(f"Error opening file '{sys.argv[1]}': {a}\n")
    except PermissionError as b:
        print(f"Error opening file '{sys.argv[1]}': {b}\n")


if __name__ == "__main__":
    main()
