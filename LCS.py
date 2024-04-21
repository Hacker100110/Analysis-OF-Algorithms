def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return ""
    if b[i][j] == "↖":
        return print_lcs(b, X, i - 1, j - 1) + X[i - 1]
    elif b[i][j] == "↑":
        return print_lcs(b, X, i - 1, j)
    else:
        return print_lcs(b, X, i, j - 1)

def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0] * (n + 1) for _ in range(m + 1)]
    b = [[""] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "↖"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "←"

    # Print the Dynamic Programming Matrix
    print("Dynamic Programming Matrix:")
    print("    " + " ".join(f"{char:^3}" for char in Y))
    for i in range(m + 1):
        if i == 0:
            print("   " + " ".join(f"{'':^3}" for _ in range(n + 1)))
        else:
            print(f"{X[i - 1]} ", end="")
            for j in range(n + 1):
                print(f"{c[i][j]}{b[i][j]:^3}", end="  ")
            print()

    # Retrieve the LCS and its length
    lcs = print_lcs(b, X, m, n)
    lcs_length = len(lcs)

    return lcs, lcs_length

# Take inputs from the user
X = list(input("Enter the first sequence: "))
Y = list(input("Enter the second sequence: "))

# Find the Longest Common Subsequence and its length
lcs, length = lcs_length(X, Y)
print("Longest Common Subsequence:", lcs)
print("Length of LCS:", length)

