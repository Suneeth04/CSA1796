from itertools import permutations
def solve_cryptarithmetic(puzzle):
    words = puzzle.split()
    letters = set("".join(words))
    if len(letters) > 10:
        return "Too many unique letters"
    digit_permutations = permutations("0123456789", len(letters))
    for perm in digit_permutations:
        digit_map = dict(zip(letters, perm))
        if all(int("".join([digit_map[c] for c in word])) for word in words):
           
            solution = " ".join([word.translate(str.maketrans(digit_map)) for word in words])
            return solution

    return "No solution found"
puzzle = "SEND + MORE = MONEY"
print("SEND + MORE = MONEY")
solution = solve_cryptarithmetic(puzzle)
print(solution)
