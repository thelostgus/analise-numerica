import numpy as np

def best_line(x, y):
    n = len(x)
    # soma das coordenadas x
    sum_x = sum(x)
    # soma das coordenadas x**2
    sum_x2 = sum(xi ** 2 for xi in x)
    # soma das coordenadas y
    sum_y = sum(y)
    #soma das coordenadas x*y
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Matriz dos coeficientes
    A = [[n, sum_x], [sum_x, sum_x2]]
    # Matriz dos termos independentes
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

# exemplo:
x = [0.0382, 0.2395, 0.3262, 0.3681, 0.5801, 0.6793, 0.7602, 0.945, 1.0753, 1.098, 1.2065, 1.3299, 1.4623, 1.6355, 1.7759, 1.8552, 1.9772, 2.1618, 2.2135, 2.3062, 2.4164, 2.5609, 2.7081, 2.8558, 2.9233, 3.026, 3.1635, 3.3097, 3.4591, 3.5911, 3.6933, 3.8451, 3.8639, 4.0274, 4.186, 4.2235, 4.3646, 4.4951, 4.5795, 4.7215, 4.9276, 5.0489, 5.1189, 5.2249, 5.4002, 5.4664, 5.6276, 5.7144, 5.802, 5.9631, 6.0683, 6.1546, 6.3164, 6.4471, 6.6136, 6.6565, 6.7903, 6.8943, 6.9962, 7.1752, 7.3419, 7.4308, 7.5346, 7.6683, 7.7349, 7.9356, 7.9854, 8.1637, 8.2787, 8.3186, 8.4439, 8.5676, 8.7406, 8.8826, 9.0228, 9.1215, 9.2252, 9.3073, 9.4858, 9.5893, 9.6846, 9.8071, 9.9925]
y = [0.3431, -0.1279, -0.1427, 0.0085, 0.0067, -0.528, -0.2992, -0.945, -1.0262, -0.9696, -1.0538, -0.8867, -1.3004, -1.8203, -0.4407, -2.0467, -1.8827, -1.7603, -2.3692, -2.9779, -1.9815, -2.4368, -2.7502, -3.2268, -3.0448, -3.4931, -3.1892, -2.8154, -3.9743, -3.4933, -2.6248, -4.3506, -4.4329, -4.3757, -4.5181, -4.6618, -4.6921, -5.0849, -5.1824, -5.4117, -4.6762, -4.744, -5.854, -6.0708, -6.2602, -5.9753, -6.3761, -6.1914, -6.3765, -5.9588, -6.7512, -6.9682, -7.3685, -7.5151, -9.2083, -7.3639, -7.7149, -7.7313, -7.8246, -8.1785, -8.2321, -8.7502, -10.1989, -8.5593, -9.7594, -8.8888, -9.0262, -7.9236, -9.406, -9.6232, -8.4589, -10.4553, -10.0968, -10.1906, -10.4323, -10.5228, -10.704, -12.5212, -9.7862, -11.6202, -11.5537, -11.392, -12.4425]

a0, a1 = best_line(x, y)

print(f'{a0} e {a1}')