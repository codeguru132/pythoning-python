hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

new_hour = ((hour + dura // 60) + (mins + dura%60) // 60)% 24

new_mins = (mins + dura % 60) % 60

print(str(new_hour) + ":" + str(new_mins))