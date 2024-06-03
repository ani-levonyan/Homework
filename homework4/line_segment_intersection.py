# You are given four real numbers- a1, b1, a2, b2 - The endpoints of two
# line segments on a line. Find the length of their intersection. Note that the
# order of the endpoints of a segment is irrelevant, i.e. the segments [1;2]
# and [2;1] are considered the same.

first_point_a1 = max_first = float(input("Enter a1 coordinate of the first point: "))
first_point_b1 = min_first = float(input("Enter b1 coordinate of the first point: "))
second_point_a2 = min_second = float(input("Enter a2 coordinate of the second point: "))
second_point_b2 = max_second = float(input("Enter b2 coordinate of the second point: "))

if first_point_b1 > max_first:
    max_first = first_point_b1
    min_first = first_point_a1
if second_point_b2 < min_second:
    min_second = second_point_b2
    max_second = second_point_a2

if min_second < max_first:
    if min_first < min_second < max_second < max_first:
        print(max_second - min_second)
    elif min_second < min_first < max_first < max_second:
        print(max_first - min_first)
    elif min_second < min_first < max_second < max_first:
        print(max_second - min_first)
    else:
        print(max_first-min_second)
else:
    print(0)
