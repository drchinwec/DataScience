sum1 = 0
i = 0
while True:
    num = int(input("Enter a number:"))
    if num != -1:
        sum1 += num
        i += 1
    else:
        break
avg_num = sum1/i
print(f'The average of all the numbers you entered is: {avg_num}')