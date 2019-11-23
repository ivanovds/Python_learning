# lesson1:
# name = input("как Вас зовут? ")
# print(name)

# lesson2:
# num_1 = float (input ("Enter first num: "))
# num_2 = float (input ("Enter second num: "))
# res = float (num_1) + num_2
# Res = input ("Enter something: ")
# Res *= 5
# print (Res)
#
# print ("Result is", res)


# lesson3:
# num = input ("Введите число: ")
#
# if int (num) > 0:
# 	if int (num) > 10:
# 		print ("Вы ввели число больше 10")
# 		if int (num) >= 50:
# 			print ("Вы ввели число больше 50")
# 	else:
# 		print ("Вы ввели число меньше 10 и больше 0")
# elif int (num) < -10:
# 	print ("Вы ввели число меньше -10")
# else:
# 	print ("Вы ввели число меньше 0 и больше -10")
# print ("All is okay!")
#
# name = input ()
# A = 'Yes' if name != "Test" else 'No'
# print (A)


# lesson4:
# i = 1000
# while i > 100:
# 	print (i)
# 	i /= 2
#
# for j in 'hello world':
# 	if j == 'a':
# 		break
# else:
# 	print ("Буквы а нету в слове")


# lesson5(lists):
# l = []
# lis = [1, 56, 'x', 34, 2.34, ['S', 't', 'r', 'o', 'k', 'a']]
# print (lis)
#
# a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
# print (a)
#
# l.append (23)
# l.append (34)
# b = [24, 67]
# l.extend (b)
# l.insert (1, 56)
# l.append (34)
# l.remove (34)
# l.pop (0)
# print (l.index (56))
# print (l.count (34))
# l.sort ()
# l.reverse ()
# l.clear ()
#
# print (l)

# индексы и срезы:
# a = [0, 23, "Hi", 1.56, 9] # Список
# print (a[-2]) # Будет выведено 1.56
# # срезы:
# # list[::3] # Берем каждый третий элемент
# # list[2::2] # Начиная со второго элемента берем каждый второй элемент
# # list[4:6:] # Начиная с 4 элемента берем все элементы по 6 элемент
# # list[::] # Берем все элементы
# l = [34, 'sd', 56, 34.34]
# i = 0
# while i < 4:
# 	print (str(l[i]) + " ", end="")
# 	i += 1
#
# print (l[-3::2])

# lesson6:
# some_list = [12, 56, 91, 12]
# print(set(some_list)) # Результат: 12, 56, 91
# print(some_list) # Результат:[12, 56, 91, 12]
