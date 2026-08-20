
# Basic File Handling Program with Exception Handling

try:

    # 1. Create and write into a file
    file = open("student.txt", "w")

    file.write("Name: Omkar\n")
    file.write("Course: Computer Science\n")
    file.write("College: MIT ADT\n")

    file.close()

    # 2. Read the complete file
    file = open("student.txt", "r")

    data = file.read()
    print("File Content:")
    print(data)

    file.close()

    # 3. Read one line
    file = open("student.txt", "r")

    line = file.readline()
    print("First Line:")
    print(line)

    file.close()

    # 4. Read all lines
    file = open("student.txt", "r")

    lines = file.readlines()
    print("All Lines:")
    print(lines)

    file.close()

    # 5. Append new data
    file = open("student.txt", "a")

    file.write("Year: First Year\n")

    file.close()

    print("New data added successfully.")

    # 6. Write the previously read lines back into the file
    with open("student.txt", "w") as file:
        file.writelines(lines)

    print("File operation completed successfully.")

except FileNotFoundError:
    print("Error: The file was not found.")
