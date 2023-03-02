array = [int(x) for x in input("Введите числа от 1 до 99 через пробел: ").split()]


def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


print(merge_sort(array))


def binary_search(array, digit, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == digit:
        return middle
    elif digit < array[middle]:
        return binary_search(array, digit, left, middle - 1)
    else:
        return binary_search(array, digit, middle + 1, right)


while True:
    try:
        digit = int(input("Введите число от 1 до 99: "))
        if digit < 1 or digit > 99:
            raise Exception
        break
    except ValueError:
        print("Введите число!")
    except Exception:
        print("Неверный диапазон!")
print(binary_search(array, digit, 0, len(array)))