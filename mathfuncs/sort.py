

def sort_sequence(sequence):
    sorted_sequence = []
    for item in sequence:
        idx = 0
        for sorted_item in sorted_sequence:
            if item <= sorted_item:
                break
            idx += 1
        sorted_sequence.insert(idx, item)
    return sorted_sequence


if __name__ == '__main__':
    numbers = [5, 6, 8, 4, 1, 1]
    print(sort_sequence(numbers))
