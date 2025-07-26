# 📝 learning_python_reader.py
# Author: Victor Espinal
# Description:
#   This script reads the content of a text file and prints it in two ways:
#   (1) the entire content at once, and (2) line-by-line reconstruction into a single string.

from pathlib import Path  # Import Path from the pathlib module for file path handling

# Define the path to the text file
path = Path("text_files/learning_python.txt")  # Specify path where the file is located

# Read the full contents of the file
contents = path.read_text(encoding="utf-8")  # Read the entire file as a single string

# Print the complete content directly
print("\n--- Full Content ---")
print(contents)

# Process the file line by line using splitlines()
lines = contents.splitlines()  # Split content into a list of lines
text = ""
for line in lines:
    text += line  # Reconstruct all lines into a single string without line breaks

# Print the reconstructed text
print("\n--- Reconstructed Text ---")
print(text)
