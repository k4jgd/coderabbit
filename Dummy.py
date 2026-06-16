def find_duplicates(numbers):
    duplicates = []

    for i in range(len(numbers)):
        count = 0

        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                count += 1

        if count > 1:
            already_exists = False

            for k in range(len(duplicates)):
                if duplicates[k] == numbers[i]:
                    already_exists = True

            if already_exists == False:
                duplicates.append(numbers[i])

    return duplicates


def sort_numbers(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] < numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp

    return numbers


def process_data(numbers):
    duplicates = find_duplicates(numbers)

    sorted_duplicates = sort_numbers(duplicates)

    result = []

    for i in range(len(sorted_duplicates)):
        result.append({
            "value": sorted_duplicates[i],
            "square": sorted_duplicates[i] * sorted_duplicates[i]
        })

    return result


data = list(range(5000)) + list(range(2500))

output = process_data(data)

for item in output:
    print(item)