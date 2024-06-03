# Given a real number, round it to the nearest whole.

num_to_round = float(input())

if num_to_round % 1 * 10 < 5:
    num_to_round = int(num_to_round // 1)
else:
    num_to_round = int(num_to_round // 1 + 1)

print(num_to_round)