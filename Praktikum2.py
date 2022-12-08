# Kelompok C13
# 1. Clarissa Luna Maheswari (5025211003)
# 2. Rule Lulu Damara (5025211050)
# 3. Ghifari Maaliki Syafa Syuhada (5025211158)

"""
    Skema pengintegrasian romberg

1 trapesium            (1,1)--> (1,2)--> (1,3)--> (1,4) -> Estimasi paling akurat
                              /        /        /
2 trapesium            (2,1)--> (2,2)--> (2,3)-
                              /        /
4 trapesium            (3,1)--> (3,2)-
                             /
8 trapesium            (4,1)-
     .
     .
     .
2^n trapesium

"""

import numpy as np
import math

# Deklarasi Variabel Global
func = []
arrEr = []
arrSol = []
n = 0
I = np.zeros((1000,1000))

# Untuk mendapatkan nilai f(x)
def f(x):
    total = 0
    length = len(func)
    for i in range(0, length):
        total = func[i] * x**i
    return total

# Rumus trapezoid
def trapezoidRule(h, a, b):
    val = 0
    total = 0
    length = len(func)
    for i in range(1, length + 1):
        val = val + f(a + i * h)
    total = (h / 2) * (f(a) + 2 * val + f(b))

    return total

# Integrasi Romberg dengan error
def rombergIntegrationError(error_margin,a,b):
    er = 100
    ite = 0
    h = b - a
    I[1,1] = trapezoidRule(h, a, b)
    while er > error_margin:
        h /= 2
        I[ite + 1, 1] = trapezoidRule(h, a, b)
        for Iy in range(2, ite + 2):
            Ix = 2 + ite - Iy
            I[Ix,Iy] = ((4 ** (Iy-1) * I[Ix+1, Iy-1] - I[Ix, Iy - 1]) / (4 ** (Iy - 1) - 1))

        er = abs((I[1, ite+1] - I[2, ite]) / I[1, ite+1]) * 100
        arrEr.append(er)
        arrSol.append(I[1,ite+1])
        ite += 1

    print("\nJawaban akhir : ", I[1, ite])

    return ite

# Integrasi romberg dengan iterasi
def rombergIntegrationIteration(iteration,a,b):
    h = b - a
    I[1,1] = trapezoidRule(h, a, b)
    for i in range(iteration):
        h /= 2
        I[i + 1, 1] = trapezoidRule(h, a, b)
        for Iy in range(2, i + 2):
            Ix = 2 + i - Iy
            I[Ix,Iy] = ((4 ** (Iy-1) * I[Ix+1, Iy-1] - I[Ix, Iy - 1]) / (4 ** (Iy - 1) - 1))

        er = abs((I[1, i+1] - I[2, i]) / I[1, i+1]) * 100
        arrEr.append(er)
        arrSol.append(I[1,i+1])


    print("\nJawaban akhir : ", I[1, i+1])

# Fungsi utama : input output dll
def main():
    print("")
    print("Misal : x^3 + 2x^2 + 7 --> derajat fungsi 3")
    n = int(input("Input derajat fungsi: ")) + 1

    for i in range(n):
        print("Koefisien x^", i, ": ", end="")
        inp = (int(input()))
        func.append(inp)

    a = int(input("\nInput batas awal: "))
    b = int(input("\nInput batas akhir: "))
    print("")

    print("w/error or w/iteration")
    flag = int(input("error = 1, iteration = 2 --->  "))

    if(flag == 1):
        error_margin = float(input("Input error margin: "))
        iteration = rombergIntegrationError(error_margin,a,b)
    elif(flag == 2):
        iteration = int(input("Input jumlah iterasi: "))
        rombergIntegrationIteration(iteration,a,b)

    print("Iterasi\t\t|\tError\t\t\t|\tHasil Integral")
    print("----------------+---------------+-------------------------------------")
    for i in range(iteration):
        print("\t%d\t|\t%f\t\t|\t%f\t" % (i+1, arrEr[i], arrSol[i]))

if __name__ == '__main__':
    main()
