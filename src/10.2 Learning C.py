# 📝 learning_python_replacer.py
# Author: Victor Espinal
# Description:
#   This script reads the content of a text file containing phrases about Python,
#   replaces all occurrences of the word 'Python' with 'C', and prints the result
#   in two different formats: full content and recomposed from lines.

from pathlib import Path  # Import Path from the pathlib module for file path handling

# Define the path to the source file
path = Path("text_files/learning_python.txt")

# Read the file's contents
contents = path.read_text(encoding="utf-8")

# Replace all occurrences of 'Python' with 'C'
new_contents = contents.replace("Python", "C")

# Print the modified content directly
print("\n--- Modified Full Text ---")
print(new_contents)

# Reconstruct the output line by line (alternative method)
text = ""
for new_content in new_contents.splitlines():
    text += new_content

# Print the recomposed result
print("\n--- Reconstructed Text ---")
print(text)