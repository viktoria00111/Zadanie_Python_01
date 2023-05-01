#  Задача 30:  Заполните массив элементами арифметической прогрессии.
#  Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
#  Формула для получения n-го члена прогрессии: a_n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# n = int(input())
# a = [0]*n
# a[0] = int(input("введите число"))
# d = int(input())
# print(a[0])

# for i in range(1,n):
#     a[i] = a [i - 1] + d
# print(a[i])





a1 = int(input())
d = int(input())
n = int(input())
# a1= [0]*d
# print(a1[0],end=' ')
for i in range(1,n):
#  a1[i]= a1[i-1]+n
  print(a1 + i * d)

# n = int(input('Input n '))

# d = int(input('Input d '))


# a[0] = int(input('Input a[0] '))

#for i in range(1,d):
    
   # print([i],end=' ')


   # не нашла общего решения