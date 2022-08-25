#       Covert the time into 24 hr format

time = input("Enter the time (hh:mm AM/PM) : ")
period = time.split()[1]
hh = int((time.split()[0]).split(":")[0])
mm = (time.split()[0]).split(":")[1]

if period == "PM" :
    hh += 12
else:
    hh %= 12

print("{0:02d}:{1}".format(hh, mm))
print("{:.2f}".format(2.33434343))
