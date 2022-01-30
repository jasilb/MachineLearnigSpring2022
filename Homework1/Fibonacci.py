def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_imperative(n):
    sequence = [0, 1]
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[n]


def fibonacci_matrix(n):
    matrix = [[1, 1], [1, 0]]
    m2 = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    if n == 1:
        return 1

    for i in range(2, n):
        a = (matrix[0][0] * m2[0][0]) + (matrix[0][1] * m2[1][0])
        b = (matrix[0][0] * m2[0][1]) + (matrix[0][1] * m2[1][1])
        c = (matrix[1][0] * m2[0][0]) + (matrix[1][1] * m2[1][0])
        d = (matrix[1][0] * m2[0][1]) + (matrix[1][1] * m2[1][1])
        matrix[0][0] = a
        matrix[0][1] = b
        matrix[1][0] = c
        matrix[1][1] = d
    return matrix[0][0]


def main():
    print('recursive')
    for n in range(10):
        print(fibonacci_recursive(n))
    print('imperative')
    for n in range(10):
        print(fibonacci_imperative(n))
    print('matrix')
    for n in range(10):
        print(fibonacci_matrix(n))


if __name__ == '__main__':
    main()
