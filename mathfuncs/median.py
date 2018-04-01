from maths.sort import sort_sequence


def find_med(sequence):
    sorted_sequence = sort_sequence(sequence)
    idx = len(sorted_sequence) / 2
    median = sorted_sequence[int(idx)]
    if idx - int(idx) == 0:
        median = (sorted_sequence[int(idx) - 1] + median) / 2
    return median


if __name__ == '__main__':
    numbers = [5, 6, 8, 4, 1, 1]
    print(find_med(numbers))
