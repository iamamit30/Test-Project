hours = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duratin (minutes): "))

mins = mins + dura
hours = hours + mins //60
mins = mins % 60
hours = hours % 24

print(hours, ":", mins)
print("\nPress any key to end the program.")
input()
print("--THE END--")