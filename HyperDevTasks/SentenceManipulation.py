def find_occ(str, ch):
    return [i for i, letter in enumerate(str) if letter == ch]

str_manip = input("Enter a short sentence:")
str_len = len(str_manip)
print("The length of the string is " + str(str_len))
lastletter = (str_manip[-1:])
index = find_occ(str_manip, lastletter)
print("The last letter occurs in positions: ")
print(index)

new_str = str_manip.replace(lastletter, "@")
print(new_str)
print(str_manip[:19:-1])

new_word = str_manip[0:3] + str_manip[str_len-2:]
print(new_word)