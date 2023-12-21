print("Please enter 3 different integers: ")
a = int(input("number 1: "))
b = int(input("number 2: "))
c = int(input("number 3: "))

sum_abc = a+b+c
print("The summ of all numbers {}, {} and {} is: {}".format(a, b, c, sum_abc))

minus = a-b
print("The first number {} minus second number {} is: {}".format(a, b, minus))

multi = c*a
print("The third number {} multiplied by first number {} is: {}".format(c, a, multi))

sum_c=sum_abc/c
print("The summ of all numbers {} diveded on last number {} is {}".format(sum_abc,c, sum_c))
