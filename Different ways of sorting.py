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


#original sizing command for uniform grps/parade
def sizing_org(matrix):
    m, n = len(matrix), len(matrix[0])
    arr = [element for row in matrix for element in row]
    arr.sort() #use whatever sorting algorithm is efficient
    satu = arr[::2] #1, 3, 2 from the back (shortest in the middle)
    dua = arr[1::2] # 2, 3, 1 from the front (tallest in the middle)

    def arrange_132(arr, row):
        if len(arr) == 0:
            return []
        elif len(arr) == 1:
            return arr
        temp = arr[:-row - 1:-1] #from the back
        def helper(arr):
            if len(arr) == 0:
                return []
            elif len(arr) == 1:
                return arr
            return [arr[0]] + helper(arr[2:]) + [arr[1]] # 1, 3, 2 recursively

        return helper(temp) + arrange_132(arr[:-row], row)

    def arrange_231(arr, row):
        if len(arr) == 0:
            return []
        elif len(arr) == 1:
            return arr
        temp = arr[:row] #from the front

        def helper(arr):
            if len(arr) == 0:
                return []
            elif len(arr) == 1:
                return arr
            return [arr[1]] + helper(arr[2:]) + [arr[0]]  # 2, 3, 1 recursively

        return helper(temp) + arrange_132(arr[row:], row)

    new_arr = arrange_132(satu, m) + arrange_231(dua, m)
    new_matrix = [[] for i in range(m)]
    while new_arr:
        for row in range(m):
            new_matrix[m - row - 1].append(new_arr.pop())

    return new_matrix
#
# print(sizing_org([[1, 4, 5], [2, 6, 3], [7, 9, 8]]))

#[[6, 3, 9], [2, 1, 5], [8, 4, 7]]
