def length_of_last_word(s):
    str = s.split()
    if len(str) == 0:
        return 0
    return len(str[-1])
user_input = input("Enter a string: ")
output = length_of_last_word(user_input)
print("Length of the last word:", output)

