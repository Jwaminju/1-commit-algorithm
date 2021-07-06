def bubblesort(A):
    for i in range(1, len(A)):
        for j in range(0, len(A)-1):
            if A[j] > A[i]:
                A[j], A[i] = A[i], A[j]

