

# def factorial(f):
#     if(f == 1):
#         return 1
#     else:
#         return f*factorial(f-1)
#
# f = int(input("input a value  "))
# print(factorial(f))

# def max(list):
#     if len(list) == 2:
#       return list[0] if list[0] > list[1] else list[1]
#     sub_max = max(list[1:])
#     return sub_max if sub_max > list[0] else list[0]
#
#
# list = [22222,333,43,9,5,6222222]
#
# print(max(list))
#


def f(sum, l=[]):
    print(l, end='..')
    l.append(sum)
    print(l)



l = [1]
f(10)
f(10)
f(10, l)
f(10)
print(l)