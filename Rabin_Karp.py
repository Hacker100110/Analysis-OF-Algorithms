def Rabin_karp(T, P, d, q):
    n = len(T)
    m = len(P)
    h = pow(d, m - 1, q)  
    p = 0
    t_0 = 0
    sh = 0  # Initialize spurious hits counter

    for i in range(m):
        p = (d * p + ord(P[i])) % q
        t_0 = (d * t_0 + ord(T[i])) % q

    print("Matching process:")
    for s in range(n - m + 1):
        print(f"\nShift {s}:")
        print("Pattern hash:", p)
        print("Text hash:", t_0)

        if p == t_0:
            if P == T[s:s + m]:
                print(f"Pattern occurs with shift {s}")
            else:
                print("Spurious hit detected")
                sh += 1

        if s < n - m:
            t_s = (d * (t_0 - ord(T[s]) * h) + ord(T[s + m])) % q
            t_0 = t_s

    print(f"\nTotal spurious hits: {sh}")

# Input from the user
T = input("Enter the text: ")
P = input("Enter the pattern: ")
d = int(input("Enter the radix (d): "))
q = int(input("Enter the prime number (q): "))

# Call the Rabin-Karp matcher function
Rabin_karp(T, P, d, q)

