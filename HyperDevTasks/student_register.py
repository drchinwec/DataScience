nums = int(input("Enter the number of students registering: "))
i = 0
with open('reg_form.txt', "w", encoding= 'utf-8-sig') as file:
    file.write("Student ID Numbers\n")
    while i < nums:
        sid = input("Enter the student ID number: ")
        file.write(sid + "..............\n")
        i += 1