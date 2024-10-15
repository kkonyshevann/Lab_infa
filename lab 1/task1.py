numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
mis = numbers.index(None)
numbers2 = numbers[:mis] + numbers[mis + 1:]
s = sum(numbers2)
count = len(numbers)
average = s / count
numbers[mis] = average
print("Измененный список:", numbers)
