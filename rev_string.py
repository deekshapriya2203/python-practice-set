def reverse_string(s):
    # Base case
    if len(s) == 0:
        return s
    # Recursive case
    return reverse_string(s[1:]) + s[0]


text = "hello"
print("Original string:", text)
print("Reversed string:", reverse_string(text))
