"""
19.Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество нулей в нечетных столбцах, умноженное на К больше,
чем произведение чисел в нечетных строках, то поменять местами В и С симметрично, иначе В и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: A*AT – K * F-1, иначе вычисляется выражение (A-1 +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А.
"""
import time
import numpy as np

try:
    n = int(input("Количество строк и столбцов > 3: "))
    while n < 4:
        n = int(input("Количество строк и столбцов > 3: "))
    k = int(input("Значение коэффициента k: "))
    A = np.random.randint(-10.0, 10.0, (n, n), dtype='int64')
    F = np.copy(A)
    np.set_printoptions(precision=2, linewidth=200)
    print(f"----A----\n{A}\n\n----F----\n{F}\n\n")
    cond_e, cond_lines = 0, 1
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                cond_lines *= int(A[i][j])
            if i > (n // 2 - (n - 1) % 2) and j > (n // 2 - (n - 1) % 2) and j % 2 == 0 and A[i][j] == 0:
                cond_e += 1
    print(f"Количество нулей в нечетных столбцах Е = {cond_e}\nПроизведение чисел в нечетных строках = {cond_lines}\n")
    if cond_e * k > cond_lines:
        for i in range(n // 2):
            F[i] = F[i][::-1]
    else:
        for i in range(n // 2):
            for j in range(n // 2):
                F[i][j], F[n // 2 + n % 2 + i][n // 2 + n % 2 + j] = F[n // 2 + n % 2 + i][n // 2 + n % 2 + j], F[i][j]
    print(f"----F----\n{F}\n")
    if np.linalg.det(A) > sum(np.diagonal(F)):
        if np.linalg.det(F) == 0:
            print("Матрица F - вырожденная, невозможно провести вычисления")
        else:
            print(f"----A*AT – K * F-1----\n{np.matmul(A, np.transpose(A)) - np.linalg.inv(F) * k}")
    else:
        if np.linalg.det(A) == 0:
            print("Матрица A - вырожденная, невозможно провести вычисления")
        else:
            print(f"----(A-1 +G-FТ)*K----\n{(np.linalg.inv(A) + np.tril(A) - np.transpose(F)) * k}")
    print(f"Время выполнения: {time.process_time()}")

except ValueError:
    print("Ввод не является числом")
