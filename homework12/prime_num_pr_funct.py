# Write a function that prints all prime numbers up to a given limit.

def is_prime(inp_num: int) -> bool:
    i = 3
    ans = True

    if inp_num > i:
        if inp_num % 2 == 0:
            ans = False
        else:
            while i < (inp_num / 2):
                if inp_num % i == 0:
                    ans = False
                    break
                i += 2
    return ans


def prime_nums_to_list(inp_num: int) -> list:
    prime_list = []
    for i in range(1, inp_num + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


print(prime_nums_to_list(15))
