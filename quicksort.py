"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    less = []
    greater = []
    equal = []
    
    if len(array) > 1:
        pivot = array[-1]
        for n in array:
            if n>pivot:
                greater.append(n)
            elif n<pivot:
                less.append(n)
            elif n==pivot:
                equal.append(n)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
