from decimal import Decimal, getcontext

getcontext().prec = 5
print(Decimal(1) / Decimal(7))
a = Decimal(0.1) + Decimal(0)
print(a)
b = Decimal(0.2) + Decimal(0)
print(b)
c = a + b
print(c)



def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    sum_decimal = sum(Decimal(num) for num in number_list)
    return sum_decimal / Decimal(len(number_list))


print(decimal_average([3, 5, 77, 23, 0.57], 6))
print(decimal_average([31, 55, 177, 2300, 1.57], 9))