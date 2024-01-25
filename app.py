def average(numbers: []) -> float:
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

def greatest(numbers:[]) -> int:
    big = 0
    for number in numbers:
        if number > big:
            big = number
    return big

if __name__ == '__main__':
    print('new dawn, new day')
    numbers = [0, 1, 2, 3, 4]
    print(average(numbers))
    print(greatest(numbers))

    numbers2 = [4, 4, 4, 4]
    print(average(numbers2))
    print(greatest(numbers2))
