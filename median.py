"""Median calculator."""

def median(numbers):
    length = len(numbers)
    numbers.sort()
    if length % 2 == 1:
        return numbers[int((length - 1 ) / 2)]
    else:
        index = int(length / 2)
        return (numbers[index] + numbers[index-1]) / 2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median(numbers))
