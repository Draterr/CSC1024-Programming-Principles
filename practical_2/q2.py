elapsed_seconds = int(input("Time elapsed in seconds: "))

in_hour = int((elapsed_seconds / 3600))
in_minute = int((elapsed_seconds / 60) % 60)
in_seconds = round((elapsed_seconds / 60) % 60 % 1 * 60)

print(f"{in_hour}:{in_minute}:{in_seconds}")
    
