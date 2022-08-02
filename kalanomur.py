age = int(input("enter your age: "))
#90 yil 32850 gun. 4680 hafta. 1080 ay.

year = 90 - age
month = 1080 - age * 12
week = 4680 - age * 50
day = 32850 - age * 365

print(f"you have left {day} days, {month} months, {week} weeks, {year} years.")