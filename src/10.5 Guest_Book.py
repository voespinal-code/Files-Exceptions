# 📝 Guest_Book.py
# Author: Victor Espinal
# Description:
#   This script prompts the user to enter their name multiple times and saves each entry
#   to a text file. It's a basic example of persistent user input and file handling in Python.
#   Useful for beginner file I/O practice or as the foundation for a simple guestbook app.

from pathlib import Path  # Import Path from the pathlib module for file path handling

# Define the path to the file where guest names will be stored
path = Path("text_files/Guest_Book.txt")

# Infinite loop to collect multiple guest names
while True:
    # Ask the user for their name
    name = input("Please enter your name: ")

    # Exit the loop if the user types 'quit'
    if name == "quit":
        break

    # Append the name to the guest book file (each entry on a new line)
    # 'a' mode ensures names are added, not overwritten
    with path.open(mode="a", encoding="utf-8") as file:
        file.write(name + "\n")



