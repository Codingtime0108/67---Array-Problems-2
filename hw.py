#max dif between 2 arrays
def max_difference(a):

    min_num = a[0]
    max_num = a[0]

    i = 1
    while i < len(a):
        if a[i] < min_num:
            min_num = a[i]
        if a[i] > max_num:
            max_num = a[i]
        i += 1
    
    return max_num - min_num

a = [4, 5, 234, 2, 6, 82, 234, 5234]
print("Maximum Difference:", max_difference(a))