def gauss_algorithm(A, B):
    x = [0.0] * 4
 
    for i in range(3):
        if A[i][i] == 0:
            if not perestanovka(A, B, i):
                return None
 
        for j in range(i + 1, 4):
            M = A[j][i] / A[i][i]
            for k in range(i, 4):
                A[j][k] = A[j][k] - M * A[i][k]
            B[j] = B[j] - M * B[i]
 
    if A[3][3] != 0:
        x[3] = B[3] / A[3][3]
        for i in range(2, -1, -1):
            S = 0
            for j in range(i + 1, 4):
                S = S + A[i][j] * x[j]
            x[i] = (B[i] - S) / A[i][i]
    else:
        return None
 
    return x
 
 
def perestanovka(A, B, i):
    for j in range(i, 4):
        if A[j][i] != 0:
            A[i], A[j] = A[j], A[i]
            B[i], B[j] = B[j], B[i]
            return True
    return False
