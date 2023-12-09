import calendar

y = int(input("Enter the year :"))
for m in range(1,4):\
        print(calendar.month(y, m),sep=" ")