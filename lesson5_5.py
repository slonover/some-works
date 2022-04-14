'''Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]'''


#вариант решения через словарь
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
d={}
for j in src: #O(n)
    if j in d:
        d[j]+=1
    else:
        d[j]=1
result=[el for el in d if d[el]==1] #O(n)
print(result)

#вариант решения через множества, требуется меньше памяти

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
tmp=set()
unik=set()
for el in src: #O(n)
    if el in tmp:
        unik.discard(el)
    else:
        unik.add(el)
        tmp.add(el)
result=[el for el in src if el in unik] #O(n)
print (result)