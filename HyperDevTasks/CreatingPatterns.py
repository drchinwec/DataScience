pattern = []
j = 1
for i in range(1,10):
    if i < 6:
        pattern = i*"*"
        print(pattern)
    elif i >= 6:
        pattern = (i-2*j)*"*"
        print(pattern)
        j += 1
        
#return [i for i, letter in enumerate(str) if letter == ch]