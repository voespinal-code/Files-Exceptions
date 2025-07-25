# 📝 guest_entry.py
# Author: [Tu Nombre]
# Description:
#   This script prompts the user to enter their name and saves it to a text file.
#   Useful for basic input/output practice or as part of a simple guestbook application.

from pathlib import Path  # Import Path from the pathlib module for file path handling

# Prompt the user for their name
name = input("Please enter your name: ")

# Define the path to the file where the guest's name will be saved
path = Path("text_files/guest.txt")

# Write the user's name to the file (overwrites existing content)
# If you want to keep all entries, use append mode instead
path.write_text(name + "\n", encoding="utf-8")