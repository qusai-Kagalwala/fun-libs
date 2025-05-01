import re

# Read the story from the file
file = open("story.txt", "r")
story = file.read()
file.close()

# Find all placeholders in < >
placeholders = re.findall(r"<(.*?)>", story)

# Dictionary to store user inputs
user_inputs = {}

# Ask user input for each placeholder (only once per word)
for word in placeholders:
    if word not in user_inputs:
        user_input = input(f"Enter a {word.replace('_', ' ')}: ")
        user_inputs[word] = user_input

# Replace each placeholder with user input using a loop
for word in placeholders:
    story = story.replace(f"<{word}>", user_inputs[word], 1)

# Print the final funny story
print("\n😂 --- Your Funny Story --- 😂\n")
print(story)
