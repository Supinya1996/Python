d=int(input())
h=int(input())
m=int(input())

if d == 1:
    day = "sunday"
if d == 2:
    day = "monday"
if d == 3:
    day = "tuesday"
if d == 4:
    day = "wednesday"
if d == 5:
    day = "thursday"
if d == 6:
    day = "friday"
if d == 7:
    day = "saturday"

if  (h == 4 and m > 0 or h > 4 and h < 12 or h == 12 and m ==0):
    time = "morning"
elif h >= 12 and h < 18 or h == 18 and m == 0:
    if (h == 12 and m > 0 or h >= 12 and h <= 18) and m < 60:
        time = "afternoon"
elif h >= 18 and h < 22 or h == 22 and m == 0:
    if (h == 18 and m > 0 or h == 22 and m == 0 or h >= 18 and h <= 22) and m < 60:
        time = "evening"
elif h >= 22 and h <= 24 or h >= 0 and h < 4 or h == 4 and m == 0:
    if (h == 22 and m > 0 or h == 4 and m == 0 or h >= 22 and h <= 24 or h >= 0 and h <= 4) and m < 60:
        time = "night"

print("good-%s-%s.png" % (time,day))
