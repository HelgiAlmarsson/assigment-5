# Prompts for number
n = int(input("Enter the length of the sequence: ")) # Do not change this line
num0 = 0
num1 = 1
num2 = 2

# Print 1, 2
print(num1)
print(num2)
# Make a for loop
for i in range(0, n - 2):
    # Add the numbers together
    new_number = num0 + num1 + num2
    # Update numbers
    num0 = num1
    num1 = num2
    num2 = new_number
    # Print number
    print(new_number)
