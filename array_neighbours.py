def find_horizontal_and_vertical_neighbours(arr):
    """
    This method takes 2d array and return list of all elements
    with all horizontal and vertical neighbours

    :param arr: 2d array
    :return: list of array elements with  neighbours
    """
    neighbors = []

    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):

            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                # corners
                new_neighbors = []
                if i != 0:
                    new_neighbors.append(arr[i - 1][j])  # top neighbor
                if j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i][j + 1])  # right neighbor
                if i != len(arr) - 1:
                    new_neighbors.append(arr[i + 1][j])  # bottom neighbor
                if j != 0:
                    new_neighbors.append(arr[i][j - 1])  # left neighbor

            else:
                # add neighbors
                new_neighbors = [
                    arr[i - 1][j],  # top neighbor
                    arr[i][j + 1],  # right neighbor
                    arr[i + 1][j],  # bottom neighbor
                    arr[i][j - 1]   # left neighbor
                ]

            neighbors.append({
                "index": i * len(arr[i]) + j,
                "value": value,
                "neighbors": new_neighbors})

    return neighbors


def find_diagonal_neighbours(arr):
    """
    This method takes 2d array and return list of all elements
    with all horizontal and vertical neighbours

    :param arr: 2d array
    :return: list of array elements with all neighbours
    """
    neighbors = []

    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):

            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                # corners
                new_neighbors = []
                if i != 0 and j != 0:
                    new_neighbors.append(arr[i - 1][j - 1])     # left top neighbour
                if i != 0 and j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i - 1][j + 1])     # right top neighbour
                if i != len(arr) - 1 and j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i + 1][j + 1])     # right bottom neighbour
                if i != len(arr) - 1 and j != 0:
                    new_neighbors.append(arr[i + 1][j - 1])     # left bottom neighbour

            else:
                # add neighbors
                new_neighbors = [
                    arr[i - 1][j - 1],  # left top neighbour
                    arr[i - 1][j + 1],  # right top neighbour
                    arr[i + 1][j + 1],  # right bottom neighbour
                    arr[i + 1][j - 1],  # left bottom neighbour
                ]

            neighbors.append({
                "index": i * len(arr[i]) + j,
                "value": value,
                "neighbors": new_neighbors})

    return neighbors


def find_all_neighbours(arr):
    """
    This method takes 2d array and return list of all elements
    with all horizontal and vertical neighbours

    :param arr: 2d array
    :return: list of array elements with all neighbours
    """
    neighbors = []

    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):

            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                # corners
                new_neighbors = []
                if i != 0 and j != 0:
                    new_neighbors.append(arr[i - 1][j - 1])  # left top neighbour
                if i != 0:
                    new_neighbors.append(arr[i - 1][j])  # top neighbor
                if i != 0 and j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i - 1][j + 1])  # right top neighbour
                if j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i][j + 1])  # right neighbor
                if i != len(arr) - 1 and j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i + 1][j + 1])  # right bottom neighbour
                if i != len(arr) - 1:
                    new_neighbors.append(arr[i + 1][j])  # bottom neighbor
                if i != len(arr) - 1 and j != 0:
                    new_neighbors.append(arr[i + 1][j - 1])  # left bottom neighbour
                if j != 0:
                    new_neighbors.append(arr[i][j - 1])  # left neighbor

            else:
                # add neighbors
                new_neighbors = [
                    arr[i - 1][j - 1],  # left top neighbour
                    arr[i - 1][j],  # top neighbor
                    arr[i - 1][j + 1],  # right top neighbour
                    arr[i][j + 1],  # right neighbor
                    arr[i + 1][j + 1],  # right bottom neighbour
                    arr[i + 1][j],  # bottom neighbor
                    arr[i + 1][j - 1],  # left bottom neighbour
                    arr[i][j - 1]  # left neighbor
                ]

            neighbors.append({
                "index": i * len(arr[i]) + j,
                "value": value,
                "neighbors": new_neighbors})

    return neighbors


if __name__ == '__main__':
    # create array
    arr = [['a', 'b', 'c'],
           ['d', 'e', 'f'],
           ['g', 'h', 'k']]

    # find all neighbours
    neighbors = find_all_neighbours(arr)
    for n in  neighbors:
        print(n)

