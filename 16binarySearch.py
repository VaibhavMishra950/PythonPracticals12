def binary_search(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        step = step+1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid

        elif element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]     
element = int(input("Enter Element to search: "))
print("Searching for {} in {}".format(element, array))
print("Index of {}: {}".format(element, binary_search(array, element)))

