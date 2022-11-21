try:
    list_i = input("Введите последовательность чисел через пробел: ").split()
    list_int = list(map(int, list_i))
except ValueError:
    print("Последовательность должна содержать только числа!")
    list_i = input("Введите последовательность чисел через пробел: ").split()
    list_int = list(map(int, list_i))
try:
    digit = int(input("Введите любое число: "))
except ValueError:
    print("Пожалуйста, введите число")
    digit = int(input("Введите любое число: "))

def qsort(L, start, end):
    mid = (start + end) // 2
    eq = L[mid]
    i, j = start, end
    while i <= j:
        while L[i] < eq:
            i += 1
        while L[j] > eq:
            j -= 1
        if i <= j:
            L[i], L[j] = L[j], L[i]
            i += 1
            j -=1
    if end > i:
        qsort(L, i, end)
    if j > start:
        qsort(L, start, j)
    return L

def bsearch(L, element, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if L[mid] == element:
        return mid
    elif element < L[mid]:
        return bsearch(L, element, start, mid-1)
    else:
        return bsearch(L, element, mid+1, end)

print(f'Отсортированная последовательность: {qsort(list_int, 0, len(list_int)-1)}')
search_v = bsearch(list_int, digit, 0, len(list_int)-1)
if search_v:
    print(f'Позиция числа перед введенным Вами элементом: {search_v-1}')
else:
    print("Такого числа нет в указанной последовательности")
