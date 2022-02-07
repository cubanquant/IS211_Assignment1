def listDivide(numbers, divide=2):
    count = 0
    if (len(numbers) == 0):
        return 0
    for i in numbers:
        try:
            if (i % divide == 0):
                count += 1
        except:
            return 'Error: ListDividException'
    return count


def testListDivide():
    print(listDivide([1, 2, 3, 4, 5]))
    print(listDivide([2, 4, 6, 8, 10]))
    print(listDivide([30, 54, 63, 98, 100], divide=10))
    print(listDivide([]))
    print(listDivide([1, 2, 3, 4, 5], 1))


testListDivide()