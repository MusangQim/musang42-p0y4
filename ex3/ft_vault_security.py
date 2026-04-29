#!/usr/bin/env python3

def secure_archive(filename: str, action: str = "", content: str = "") -> tuple:
    try:
        if action == "read":
            with open(filename, "r") as f:
                data = f.read()
                return (True, data)
        if action == "write":
            with open(filename, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")
    except (PermissionError, FileNotFoundError) as a:
        return(False, str(a))
    return (False, "Invalid action")


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    attempt_1 = secure_archive("/not/existing/file", "read")
    print(attempt_1)
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    attempt_2 = secure_archive("/etc/master.passwd", "read")
    print(attempt_2)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    attempt_3 = secure_archive("ancient_fragment.txt", "read")
    print(attempt_3)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    attempt_4 = secure_archive("ancient_fragment.txt", "write", attempt_3[1])
    print(attempt_4)


if __name__ == "__main__":
    main()
