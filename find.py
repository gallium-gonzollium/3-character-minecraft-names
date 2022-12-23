# Enter usernames text here
usernames = '''

'''

def separate_usernames(c):
    c = c.split('\n')
    for i in range(len(c)):
        c[i] = c[i][0:3]
    return c
def shortness_value(string):
  # Initialize the shortness value to the length of the string
    shortness = len(string) - 1
  
  # Create a lookup table for the shortness values of each character
    shortness_values = {
        'a': 5, 'b': 5, 'c': 5, 'd': 5, 'e': 5,
        'f': 3, 'g': 5, 'h': 5, 'i': 1, 'j': 5, 
        'k': 5, 'l': 2, 'm': 5, 'n': 5, 'o': 5, 
        'p': 5, 'q': 5, 'r': 5, 's': 5, 't': 3, 
        'u': 5, 'v': 5, 'w': 5, 'x': 5, 'y': 5, 
        'z': 5, '0': 5, '1': 5, '2': 5, '3': 5, 
        '4': 5, '5': 5, '6': 5, '7': 5, '8': 5, 
        '9': 5, '_': 5
  }
  
  # Iterate through each character in the string
    for char in string:
    # Add the shortness value for the character to the total shortness
        shortness += shortness_values.get(char, 0)
  
  # Return the final shortness value
    return shortness

# Test the function with some sample inputs

strings = separate_usernames(usernames)
shortness_values = []

for string in strings:
    string = string.lower()
    shortness = shortness_value(string)
    shortness_values.append((string, shortness))

# Sort the list of tuples by shortness value
shortness_values = sorted(shortness_values, key=lambda x: x[1])

# Print the sorted list of tuples
out = ''
for string, shortness in shortness_values:
    out += f'{string} -> {shortness}\n'
print(out)
