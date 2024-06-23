def count_triplets(filename):
    with open(filename, 'r') as f:
        numbers = [int(line.strip()) for line in f]

    max_ending_13 = max(num for num in numbers if num % 10 == 3)
    count = 0
    max_sum = 0

    for i in range(len(numbers) - 2):
        triplet = numbers[i:i+3]
        if sum(triplet) >= max_ending_13:
            two_digit_count = sum(10 <= num < 100 for num in triplet)
            if two_digit_count == 1:
                count += 1
                max_sum = max(max_sum, sum(triplet))

    return count, max_sum

filename = 'input.txt'  # replace with your file name
count, max_sum = count_triplets(filename)
print(f'Count: {count}, Max sum: {max_sum}')
