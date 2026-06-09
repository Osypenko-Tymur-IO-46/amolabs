from aitken import aitken
 
def get_error_table(eval_func, x_nodes, y_nodes, x):
    exact = eval_func(x)
    table = []
 
    for k in range(1, len(x_nodes) + 1):
        approx = aitken(x_nodes, y_nodes, x, k)
        abs_err = abs(exact - approx)
        rel_err = abs_err / abs(exact) if exact != 0 else 0.0
        table.append((k, approx, abs_err, rel_err))
    return exact, table
 
def get_error_curve(eval_func, x_nodes, y_nodes, X):
    Y_exact = [eval_func(x) for x in X]
    Y_interp = [aitken(x_nodes, y_nodes, x) for x in X]
    return [abs(y - yi) for y, yi in zip(Y_exact, Y_interp)]
 

