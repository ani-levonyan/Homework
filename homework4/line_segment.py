# You are given four real numbers - the coordinates of two points on a
# plane. The first two numbers are the x and y coordinates of the first point,
# and the last two numbers are the x and y coordinates of the second point.
# Output the length of the line segment bounded by the two points.

first_point_x = float(input("Enter x coordinate of the first point: "))
first_point_y = float(input("Enter y coordinate of the first point: "))
second_point_x = float(input("Enter x coordinate of the second point: "))
second_point_y = float(input("Enter y coordinate of the second point: "))

length_of_line = ((second_point_x - first_point_x) ** 2 + (second_point_y - first_point_y) ** 2) ** 0.5

if length_of_line % 1 == 0:
    length_of_line = int(length_of_line)
else:
    length_of_line = length_of_line // 1 + int((length_of_line % 1) * 10000 // 1) / 10000

print(length_of_line)
