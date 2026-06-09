def aitken(x_nodes, y_nodes, x, k=None):
    n = len(x_nodes) if k is None else k
    P = [[0.0] * n for _ in range(n)]
    for i in range(n):
        P[i][0] = y_nodes[i]
 
    for j in range(1, n):
        for i in range(n - j):
            denom = x_nodes[i] - x_nodes[i + j]
            if denom == 0:
                return float('nan')
            P[i][j] = ((x - x_nodes[i + j]) * P[i][j - 1] - (x - x_nodes[i]) * P[i + 1][j - 1]) / denom

    return P[0][n - 1]
 
