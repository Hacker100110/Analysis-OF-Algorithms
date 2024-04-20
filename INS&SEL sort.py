import time
def main():
    n=int(input("Enter number of elements:"))
    A=[]
    print('Enter Elements:')
    for i in range(n):
        elements=int(input(f"Enter element{i+1}:"))
        A.append(elements)

    print("Original Array:",A)
    AS=A
    print("Selection Sort:")
    st=time.time()
    for i in range(n):
        j=i
        for k in range(i+1,n):
            if AS[k]<AS[j]:
                j=k
        AS[i],AS[j]=AS[j],AS[i]
        print(f'After step{i+1}:',AS)
    stime=time.time()-st

    AI=A
    print("Insertion Sort:")
    st=time.time()
    for j in range(1, n):
        key=AI[j]
        i=j-1
        while i>=0 and A[i]>key:
          AI[i+1]=AI[i]
          i -=1
        AI[i+1]=key     
        print(f'After step{j}:',AI)
    Itime=time.time()-st

     # Display final sorted arrays and time complexity
    print("\nFinal Sorted Array using Selection Sort:", AS)
    print("Time complexity of Selection Sort: {:.4f} seconds".format(stime))
    print("\nFinal Sorted Array using Insertion Sort:", AI)
    print("Time complexity of Insertion Sort: {:.4f} seconds".format(Itime))

if __name__ == "__main__":
    main()
