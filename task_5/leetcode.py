# 1 - topshiriq


# digits = [4,3,2,1]
# def plusOne(digits):
#     fornow = ''
#     for i in digits:
#         fornow += str(i)
#
#     fornow = int(fornow) + 1
#
#     numbers = list()
#     for i in str(fornow):
#         numbers.append(int(i))
#
#     return numbers
#     print(plusOne(digits))




# 2 - topshiriq

s = "(([]){})"

def isValid(s):
    uzun = len(s)
    counter1 = 0
    counter1_1 = 0
    counter2 = 0
    counter2_1 = 0
    counter3 = 0
    counter3_1 = 0
    for t in range(uzun):
        if s[t] == "(":
            counter1 += 1
        elif s[t] == ")":
            counter1_1 += 1
        elif s[t] == "{":
            counter2 += 1
        elif s[t] == "}":
            counter2_1 += 1
        elif s[t] == "[":
            counter3 += 1
        elif s[t] == "]":
            counter3_1 += 1
    if counter1 == counter1_1 and counter2 == counter2_1 and counter3 == counter3_1:
        if len(s) >= 2 and s[len(s) - 1] != "(" and s[len(s) - 1] != "{" and s[len(s) - 1] != "[" and len(s) % 2 == 0:
            x = []
            chars = {")": "(", "}": "{", "]": "["}
            for i in s:
                if i in chars:
                    if x:
                        z = x.pop()
                    if chars[i] != z:
                        return False
                else:
                    x.append(i)
            return not x

        else:
            return False
    return False

print(isValid(s))


















