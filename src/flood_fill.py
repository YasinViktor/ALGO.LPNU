# flood_fill.py

from collections import deque
import os

def flood_fill(row, col, image, start_x, start_y, new_color):
    x, y = row, col
    original_color = image[start_x][start_y]

    if original_color == new_color:
        return image

    result = [list(row) for row in image]
    visited = set()

    queue = deque([(start_x, start_y)])

    while queue:
        current_x, current_y = queue.popleft()

        if 0 <= current_x < x and 0 <= current_y < y and result[current_x][current_y] == original_color and (current_x, current_y) not in visited:

            result[current_x][current_y] = new_color
            visited.add((current_x, current_y))

            queue.append((current_x - 1, current_y))  # Top
            queue.append((current_x + 1, current_y))  # Bot
            queue.append((current_x, current_y - 1))  # Left
            queue.append((current_x, current_y + 1))  # Right

    return result

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        row, col = map(int, file.readline().strip().split(','))

        start_x, start_y = map(int, file.readline().strip().split(','))

        new_color = file.readline().strip()[0]

        image_lines = [list(line.strip()) for line in file.readlines()]

    return row, col, start_x, start_y, new_color, image_lines

def save_to_file(matrix, output_file):
    with open(output_file, 'w') as file:
        for row in matrix:
            file.write(''.join(row) + '\n')

if __name__ == "__main__":
    # Get the current directory
    current_dir = os.path.dirname(os.path.realpath(__file__))

    input_file = os.path.join(current_dir, 'input.txt')
    output_file = os.path.join(current_dir, 'output.txt')

    row, col, start_x, start_y, new_color, image = read_file(input_file)

    result_matrix = flood_fill(row, col, image, start_x, start_y, new_color)

    save_to_file(result_matrix, output_file)
