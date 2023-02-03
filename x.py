# s = "abcdefg"
# def split(word):
#     y = []
#     for i in range(0, len(word), 2):
#         if len(word) % 2 == 0:
#             if i != len(word) - 1:
#                 y.append(word[i] + word[i+1])
#         else:
#             if i != len(word) - 1:
#                 y.append(word[i] + word[i + 1])
#             if i == len(word) - 1:
#                     y.append(word[i] + "_")
#     return y
#
# print(split(s))
x = [1, 2, 2]
y = [1, 2, 1]

def array_diff(a, b):
    for i in range(len(b)):
        x = b[i]
        if i == len(b) - 1 and x in a:
            a = [i for i in a if i != x]
        if x in a:
            a = [i for i in a if i != x]
    return a

print(array_diff(x,y))




