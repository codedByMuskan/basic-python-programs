## Letter template
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

# Get user input
name = input("Enter your name: ")
date = input("Enter the date: ")

# Replace placeholders with actual values
filled_letter = letter.replace("<|Name|>", name).replace("<|Date|>", date)

# Print the filled letter
print("\n" + filled_letter)
