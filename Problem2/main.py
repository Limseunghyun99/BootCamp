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


if __name__ == '__main__':
    arr = ArrayUtil([1, 2, 3, 3, 4], [2, 3, 4])
    emptyArr = ArrayUtil()
    emptyArr.set([1, 2, 3, 3, 4], [2, 3, 4])

