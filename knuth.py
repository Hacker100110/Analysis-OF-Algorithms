def prefix_function(P):
    m = len(P)
    π = [0] * m  # Initialize prefix array with zeros
    π[0] = 0     # Initialize the first element of the prefix array
    i = 0        # Initialize the index for prefix function

    # Computing prefix function
    for j in range(1, m):
        while i > 0 and P[i] != P[j]:
            i = π[i - 1]  # Update i using the previously computed prefix value
        if P[i] == P[j]:
            i += 1  # Increment i if characters match
        π[j] = i  # Store the current prefix value

    return π

def kmp_matcher(T, P):
    n = len(T)
    m = len(P)
    π = prefix_function(P)  # Compute prefix function for the pattern
    i = 0                   # Initialize the index for pattern matching

    # Print prefix table
    print("Prefix table:")
    print("Index: ", list(range(m)))
    print("Value: ", π)

    print("\nMatching process:")
    for j in range(n):
        print("\nCurrent character in text:", T[j])
        print("Current state of pattern:", P[:i])

        # Matching characters and handling mismatches
        while i > 0 and P[i] != T[j]:
            i = π[i - 1]  # Shift pattern by using prefix table
            print(f"Mismatch occurred. Shifting pattern by {i}")

        if P[i] == T[j]:
            print("Character matched:", T[j])
            i += 1

        # If the entire pattern is matched, print the shift
        if i == m:
            print(f"\nPattern occurs with shift {j - m + 1}")
            i = π[i - 1]  # Continue matching from the end of the matched pattern

# Input from the user
T = input("Enter the text: ")
P = input("Enter the pattern: ")

# Call the KMP matcher function
kmp_matcher(T, P)
