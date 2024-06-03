x1 = float(input("Enter x coordinate of the first point: "))
y1 = float(input("Enter y coordinate of the first point: "))
x2 = float(input("Enter x coordinate of the second point: "))
y2 = float(input("Enter y coordinate of the second point: "))

# Calculate the distance using the distance formula
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Check if the distance is an integer
if distance.is_integer():
    rounded_distance = int(distance)
else:
    rounded_distance = round(distance, 4)

# Print the length of the line segment
print(rounded_distance)