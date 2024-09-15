try:

    with open('my_file.txt', 'w') as file:
    
        file.write("Hello, i am interested in python language.\n")
        file.write("Number of experienced users: 150\n")
        file.write("Total amount: 3000\n")
    print("File created and initial content written successfully.")
    
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("Contents of 'my_file.txt':")
        print(content)
    
    with open('my_file.txt', 'a') as file:
        file.write("Appended line 1: Another update.\n")
        file.write("Appended line 2: Total sales: 4500\n")
        file.write("Appended line 3: End of file.\n")
    print("Additional content appended successfully.")
    
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("Contents of 'my_file.txt' after appending:")
        print(content)
    
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File operation completed.")
