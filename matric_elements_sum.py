def matrix_elements_sum(in_matrix: list):
    result = 0
    for c in range(len(in_matrix[0])):
        for r in range(len(in_matrix)):
            price = in_matrix[r][c]
            if price == 0:
                break
            else:
                result += price
    return result


if __name__ == '__main__':

    matrix = [[0, 1, 1, 2],
              [0, 5, 0, 0],
              [2, 0, 3, 3]]

    total_price = matrix_elements_sum(matrix)

    print('Total Price:', total_price)
