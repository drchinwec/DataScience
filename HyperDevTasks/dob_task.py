def bold_text(text): # define function to put text in bold
    return "\033[1m" + text + "\033[0m"

names = "" # initialise storage for names
birthdate = "" # initialise storage for birthdate
with open("DOB.txt", "r+") as file: # read in file
    # lines = file.read()
    for line in file: # iterate through each line in the file
        separate_words = line.split(' ') # split each line using space as delimiter

        two_names = " ".join(separate_words[0:2]) # join the first two words using space as a delimiter
        names = names + two_names + "\n" # write in each joined word on a separate line

        dob = " ".join(separate_words[2:5]) # join the last two strings to form the birthdate
        birthdate = birthdate + dob # write in each on a separate line
print(bold_text("Names"))
print(names)
print(bold_text("Birthdate") + "\n" + birthdate)