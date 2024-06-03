# Write a function that checks if a given string is a valid email address.

def valid_email(inp_str: str) -> bool:
    ans = True
    if chr(64) in inp_str and chr(46) in inp_str:
        check_list = [inp_str[:inp_str.index(chr(64))], inp_str[inp_str.index(chr(64))+1:]]
        for j in check_list:
            for i in j:
                if not (i.isalpha() or i.isdigit() or i in [chr(45), chr(46)]):
                    ans = False
    else:
        ans = False
    return ans


print(valid_email("abc@gmail.com"))
