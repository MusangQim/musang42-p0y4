#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>\n")
        exit()
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file: typing.IO = open(sys.argv[1], "r")
        content = file.read()
        file.close()
        print("---\n")
        print(content)
        print("---")
        print(f"File '{sys.argv[1]}' closed")
    except FileNotFoundError as a:
        print(f"Error opening file '{sys.argv[1]}': {a}\n")
    except PermissionError as b:
        print(f"Error opening file '{sys.argv[1]}': {b}\n")


if __name__ == "__main__":
    main()
