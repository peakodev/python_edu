from functools import reduce


# Функція отримує масив цілих чисел А. Знайти найбільший добуток який може бути зроблено шляхом множення всіх,
# крім одного, записів в А. (Запис не можна використовувати більше одного разу)
#
# Використовуйте генератор і lambda для обчислення щоб скоротити споживання пам'яті.
# Визначте сценарій (чисел < 0 парна або непарна кількість)
# Розбийте функцію на 2 логічні частини -- пошук індексу в А, який треба пропустити і саме обчислення добутку.
def max_product(A):

    neg_num = 0
    pos_idx = None
    neg_idx = None
    max_neg_idx = None

    for i, a in enumerate(A):
        if a < 0:
            neg_num += 1
            if neg_idx is None or A[neg_idx] < a:
                neg_idx = i
            if max_neg_idx is None or a < A[max_neg_idx]:
                max_neg_idx = i
        else:
            if pos_idx is None or a < A[pos_idx]:
                pos_idx = i

    skip_idx = (neg_idx if neg_num % 2 else pos_idx if pos_idx is not None else max_neg_idx)
    return reduce(lambda product, a: product * a, (a for i, a in enumerate(A) if i != skip_idx))


print(max_product([3, 2, 5, 4]))

print(max_product([3, 2, -1, 5, 4]))

print(max_product([3, 2, -1, 6, 4, -1]))
