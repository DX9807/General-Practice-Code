from datetime import datetime

now = datetime.now()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

print (mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)



now = datetime.now()

print()
print("Current date and time using str method of datetime object:")
print(str(now))

print()
print("Current date and time using instance attributes:")
print("Current year: %d" % now.year)
print("Current month: %d" % now.month)
print("Current day: %d" % now.day)
print("Current hour: %d" % now.hour)
print("Current minute: %d" % now.minute)
print("Current second: %d" % now.second)
print("Current microsecond: %d" % now.microsecond)

print()
print("Current date and time using strftime:")
print(now.strftime("%Y-%m-%d %H:%M"))