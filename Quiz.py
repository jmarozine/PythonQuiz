import math

# Prompt the user to enter the radius
radius = int(input("Enter the radius of the circle as an integer: "))

# Calculate the area and circumference
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

# Display the area and circumference using F-Strings
print(f"The area of the circle is: {area:.2f}")
print(f"The circumference of the circle is: {circumference:.2f}")