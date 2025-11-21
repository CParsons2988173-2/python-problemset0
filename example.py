import numpy as np

# Ask the user to enter x
x = int(input("Enter number x: "))

# Ask the user to enter y
y = int(input("Enter number y: "))

# Calculate x raised to the power y
power_value = x ** y

# Calculate log base 2 of x
log_value = np.log2(x)

# Print the results
print("x**y =", power_value)
print("log(x) =", log_value)