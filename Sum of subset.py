def SOS(s, k, r, m, w, x):
    if s == m:
        print("Solution found at:",STFT(x, w))
        return
    if k < len(w):
        if s + w[k] <= m:
            SOS(s + w[k], k + 1, r - w[k], m, w, x + [w[k]])
    if s + r - w[k] >= m and k + 1 < len(w) and s + w[k+1] <= m:
        SOS(s, k + 1, r - w[k], m, w, x)

def STFT(x, w):
    fixed_tuple=[]
    for weight in w:
        if weight in x:
            fixed_tuple.append(1)
        else:
            fixed_tuple.append(0)
    return tuple(fixed_tuple)

def main():
    n=int(input("Enter the number of elements:"))
    w = []
    for i in range(n):
        weight=int(input("Enter weighht{}:".format(i + 1)))
        w.append(weight)
    m = int(input("Enter target sum:"))
    total_sum = sum(w)
    x = []
    print("\nStep by Step iteraion:")
    SOS(0, 0, total_sum, m, w, x)
    
if __name__=='__main__':
    main()
