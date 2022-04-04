def sizing(matrix):
    new_arr = []
    for row in matrix:
        for element in row:
            new_arr.append(element)
    def merge(left, right):
        arr = []
        while left and right:
            if left[0] < right[0]:
                arr.append(left.pop(0))
            else:
                arr.append(right.pop(0))
        arr.extend(left)
        arr.extend(right)
        return arr

    def merge_sort(arr):
        if len(arr) < 2:
            return arr
        else:
            left = arr[:len(arr)//2]
            right = arr[len(arr)//2:]
            return merge(merge_sort(left), merge_sort(right))

    sorted = merge_sort(new_arr)

    def arrange(arr):
        if len(arr) < 3:
            return arr
        return [arr[-2]] + arrange(arr[:-2]) + [arr[-1]]

    m, n = len(matrix), len(matrix[0])
    new_matrix = []
    for i in range(m):
        row_involved = sorted[:n]
        sorted = sorted[n:]
        new_matrix.append(arrange(row_involved))

    return arrange(new_matrix)

#print(sizing([[1, 4, 5], [2, 6, 3], [7, 9, 8]]))
#[[5, 4, 6], [2, 1, 3], [8, 7, 9]]
