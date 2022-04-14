'''Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...
'''


def nums_gen(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


nums = nums_gen(6)
print(next(nums))
print(next(nums))
print(next(nums))


# 2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
# ключевое слово yield.

max_nums = 6
oneline_gen = (num for num in range(1, max_nums + 1, 2))
print(*oneline_gen, sep=' ')
