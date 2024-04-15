input_string = input("Enter a sentence :")
a = len(input_string)
i = 0
new_str = ""
while i < a:
    one_str = input_string[i]
    if i % 2 == 0:
        new_str = new_str + one_str.upper()
    else:
        new_str = new_str + one_str.lower()
    i += 1
print(new_str)

sep_word = input_string.split(' ')
b = len(sep_word)
j = 0
# print(sep_word)
alt_sent = ""
while j < b:
    one_word = sep_word[j]
    if j % 2 == 0:
        alt_sent = alt_sent + one_word.upper() + " "
    else:
        alt_sent = alt_sent + one_word.lower() + " "
    j += 1
print(alt_sent)