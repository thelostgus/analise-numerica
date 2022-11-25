import numpy as np
# import scipy as sp

def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    B = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return np.linalg.solve(A, B)

x = [-4.9978, -4.8163, -4.7185, -4.5002, -4.4565, -4.3005, -4.1283, -4.04, -3.8167, -3.6781, -3.6214, -3.4749, -3.3418, -3.22, -3.1169, -2.9393, -2.7365, -2.5859, -2.4627, -2.3759, -2.2577, -2.1025, -1.9967, -1.7868, -1.6732, -1.5993, -1.3787, -1.2786, -1.2329, -0.9789, -0.9682, -0.8073, -0.6332, -0.4996, -0.3779, -0.1926, -0.0912, 0.0445, 0.1935, 0.3185, 0.4997, 0.5787, 0.7592, 0.8398, 0.9263, 1.1166, 1.2497, 1.3646, 1.4621, 1.7059, 1.7616, 1.9392, 2.077, 2.1565, 2.2467, 2.4662, 2.6057, 2.7542, 2.8028, 3.0101, 3.07, 3.1955, 3.347, 3.5706, 3.6554, 3.7798, 3.8791, 4.0349, 4.1833, 4.3635, 4.5078, 4.5984, 4.73, 4.917, 4.9371, 5.0775, 5.2526, 5.4516, 5.4708, 5.6144, 5.7741, 5.9248]
y = [1.323, 1.852, 2.532, 2.5964, 3.8887, 3.6131, 3.6962, 3.8171, 4.3085, 3.863, 4.4604, 4.9136, 5.7432, 5.2984, 4.3222, 5.9587, 6.4509, 5.6363, 5.5632, 5.5645, 6.1779, 5.5796, 5.8718, 5.4132, 5.5904, 5.4527, 5.4194, 5.2523, 5.655, 5.4045, 5.065, 5.0021, 4.9179, 4.7267, 4.905, 4.5891, 4.3182, 6.5275, 4.6021, 3.746, 4.3852, 4.6097, 3.8744, 4.0009, 3.7415, 5.598, 3.6757, 3.8837, 3.9177, 3.8404, 3.6905, 2.963, 4.008, 3.3615, 4.5781, 4.2575, 4.189, 3.9707, 3.5433, 3.2097, 3.9746, 4.0725, 3.5261, 4.5842, 4.3464, 3.9192, 4.8547, 4.3538, 5.0406, 5.8472, 6.8666, 6.6912, 6.4029, 8.6321, 7.3694, 7.9167, 8.4377, 9.2179, 9.8867, 9.1575, 10.6755, 11.5766]

a0, a1, a2, a3 = best_poly(x, y, 3)

print(f'{a0} , {a1 }, {a2 }, {a3 }')