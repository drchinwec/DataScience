swimtime = int(input("Enter your swimming time in minutes:"))
cycletime = int(input("Enter your cycling time in minutes:"))
runtime = int(input("Enter your running time in minutes:"))

totaltime = swimtime + cycletime + runtime
print("You have completed the triathlon in " + str(totaltime) + " minutes.")
print("")

if totaltime <= 100:
    print("You have been awarded Provincial colours!")
elif totaltime <= 105:
    print("You have been awarded Provincial half colours!")
elif totaltime <= 110:
    print("You have been awarded the Provincial scroll!")
else:
    print("You have not qualified for an award.")