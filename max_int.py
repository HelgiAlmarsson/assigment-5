max_int = 0
while True:
    # Prompt for a number
    num_int = int(input("Input a number: "))    # Do not change this line
    # Check if less than 0
    if num_int < 0:
        break
    # Check if new number is larger than the one before
    if num_int > max_int:
        # If larger then change to that number    
        max_int = num_int

print("The maximum is", max_int)    # Do not change this line
