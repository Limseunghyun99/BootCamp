class ArrayUtil:
    arr1 = []
    arr2 = []

    def __init__(self, arr1=None, arr2=None):
        if arr2 is None:
            arr2 = []
        if arr1 is None:
            arr1 = []

        self.arr1 = arr1
        self.arr2 = arr2

    def set(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def uniquify(self, arr):
        return list(set(arr))


if __name__ == '__main__':
    arr = ArrayUtil([1, 2, 3, 3, 4], [2, 3, 4])
    emptyArr = ArrayUtil()
    emptyArr.set([1, 2, 3, 3, 4], [2, 3, 4])

    print(arr.uniquify([1, 2, 3, 3, 4]))

    # Case 1: 숫자 리스트가 아닌 경우
    try:
        arr = ArrayUtil(['1', '2', '3', '3', '4'], ['2', '3', '4'])
        exit(1)
    except ValueError:
        pass

    # Case 2: 리스트가 아닌 경우
    try:
        arr = ArrayUtil(1, 2)
        exit(1)
    except SyntaxError:
        pass

    # Case 3: 중복된 값만 존재하는 리스트인 경우
    if arr.uniquify([1, 1, 1, 1, 1]) != [1]:
        exit(1)

    # Case 4: 교집합이 없는 경우
    arr = ArrayUtil([1, 2, 3], [4, 5])
    if arr.intersect() != []:
        exit(1)

    # Case 5: 교집합이 전체인 경우
    arr = ArrayUtil([1, 2, 3], [1, 2, 3])
    if arr.intersect() != [1, 2, 3]:
        exit(1)

    # Case 6: 중복 제거에 실패하는 경우 (1)
    arr = ArrayUtil([1, 2, 3], [4, 5])
    if arr.union() != [1, 2, 3, 4, 5]:
        exit(1)

    # Case 7: 중복 제거에 실패하는 경우 (2)
    arr = ArrayUtil([1, 2, 3], [1, 2, 3])
    if arr.union() != [1, 2, 3]:
        exit(1)

    print("Test OK")
