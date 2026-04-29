#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_stream_management.py <file>\n")
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
        transformed = []
        for line in lines:
            new_line = line + '#'
            transformed.append(new_line)
        for line in transformed:
            print(line)
        print("\n---")
        # --- ENTERING INPUT FOR NEW FILE NAME ---
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_input = sys.stdin.readline().strip()
        if new_input:
            try:
                print(f"Saving data to '{new_input}'")
                new_file: typing.IO = open(new_input, "w")
                new_file.write('\n'.join(transformed))
                new_file.close()
                print(f"Data saved in file '{new_input}'")
            except (FileNotFoundError, PermissionError) as a:
                sys.stderr.write(f"[STDERR] Error opening file"
                                 f" '{new_input}': {a}\n")
                sys.stderr.flush()
                print("Data not saved.")
        else:
            print("Not saving data.")
    except (FileNotFoundError, PermissionError) as b:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {b}\n")
        sys.stderr.flush()


if __name__ == "__main__":
    main()
