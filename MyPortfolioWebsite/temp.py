
text = "Hello, 123-world!"
remove_chars = ",-"  # Characters to get rid of

# Method 1: Replace with empty string

new_text = text.replace(remove_chars, "")
print(new_text)
# Method 2: Loop and build new string
new_text = ""
for char in text:
    if char not in remove_chars:
        new_text += char

print(new_text)  # Output: "Hello123world"