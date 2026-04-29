#!/usr/bin/env python3

def secure_archive(filename, action, content) -> tuple:
    print("=== Cyber Archives Security ===")
    try:
        raise ValueError
    except FileNotFoundError as a:
        return(False, str(a))
