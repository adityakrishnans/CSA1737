import itertools

def solve_crypt():
    letters = ('S','E','N','D','M','O','R','Y')
    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        # Leading letters cannot be zero
        if sol['S'] == 0 or sol['M'] == 0:
            continue

        SEND = 1000*sol['S'] + 100*sol['E'] + 10*sol['N'] + sol['D']
        MORE = 1000*sol['M'] + 100*sol['O'] + 10*sol['R'] + sol['E']
        MONEY = 10000*sol['M'] + 1000*sol['O'] + 100*sol['N'] + 10*sol['E'] + sol['Y']

        if SEND + MORE == MONEY:
            return sol, SEND, MORE, MONEY

    return None, None, None, None


# ---- DRIVER CODE ----
solution, SEND, MORE, MONEY = solve_crypt()

if solution:
    print("Solution Found:")
    print("Letter Assignments:", solution)
    print(f"\nSEND  = {SEND}")
    print(f"MORE  = {MORE}")
    print(f"MONEY = {MONEY}")
else:
    print("No solution exists.")
