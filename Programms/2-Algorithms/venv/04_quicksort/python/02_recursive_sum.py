def sum(list):
  if list == []:
    return 0
  return list[0] + sum(list[1:])


list = [2,3,4,5,5,6]

# def sum(list):
#     if (list.__len__() == 0):
#         return 0
#     else:
#         return list[0] + sum(list[1:])

print(sum(list))