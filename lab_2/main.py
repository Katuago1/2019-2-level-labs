"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    if not isinstance(num_rows, int) or not isinstance(num_cols, int):
        return []
    a =[]
    for i in range(num_rows):
        a.append([0]*num_cols)
    return a





def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    if not edit_matrix or not edit_matrix[0] or not isinstance(add_weight, int) or not isinstance(remove_weight, int):
        return list(edit_matrix)
    edit_matrix[0][0] = 0
    for j in range(1, len(edit_matrix[0])):
        edit_matrix[0][j] = edit_matrix[0][j-1] + add_weight
    for i in range(1, len(edit_matrix)):
        edit_matrix[i][0] = edit_matrix[i - 1][0] + remove_weight
    return list(edit_matrix)



def minimum_value(numbers: tuple) -> int:
    return min(numbers)



def fill_edit_matrix(edit_matrix: tuple,
    add_weight: int,
    remove_weight: int,
    substitute_weight: int,
    original_word: str,
    target_word: str) -> list:
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int) or not isinstance(substitute_weight, int) \
            or not isinstance(original_word, str) or not isinstance(target_word, str):
        return list(edit_matrix)
    for i in range(1, len(edit_matrix)):
        for j in range(1, len(edit_matrix[i])):
            r_weight = edit_matrix[i - 1][j] + remove_weight
            i_weight = edit_matrix[i][j - 1] + add_weight
            substitute = substitute_weight
            if original_word[i - 1] == target_word[j - 1]:
                substitute = 0
            s_weight = edit_matrix[i - 1][j - 1] + substitute
            edit_matrix[i][j] = minimum_value([i_weight, r_weight, s_weight])
    return list(edit_matrix)





def find_distance(original_word: str,
    target_word: str,
    add_weight: int,
    remove_weight: int,
    substitute_weight: int) -> int:
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int) or not isinstance(substitute_weight, int) \
            or not isinstance(original_word, str) or not isinstance(target_word, str):
        return -1
    matrix = generate_edit_matrix(len(original_word) + 1, len(target_word) + 1)
    initialize_edit_matrix(tuple(matrix), add_weight, remove_weight)
    fill_edit_matrix(tuple(matrix), add_weight, remove_weight, substitute_weight, original_word, target_word)
    return matrix[len(original_word)][len(target_word)]
