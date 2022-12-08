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

"""
    Integrasi Romberg
    Dalam analisis numerik, metode Romberg (Romberg 1955) digunakan untuk memperkirakan integral tertentu.
 Dengan menerapkan ekstrapolasi Richardson (Richardson 1911) berulang kali pada aturan trapesium atau
 aturan persegi panjang (aturan titik tengah).  Estimasi menghasilkan larik segitiga.  Metode Romberg adalah
 rumus Newton–Cotes – metode ini mengevaluasi integral pada titik-titik yang berjarak sama.  Integran harus
 memiliki turunan kontinu, meskipun hasil yang cukup baik dapat diperoleh jika turunannya hanya sedikit.  
 Jika memungkinkan untuk mengevaluasi integrand pada titik-titik yang berjarak tidak sama, maka metode lain 
 seperti kuadratur Gaussian dan kuadratur Clenshaw–Curtis umumnya lebih akurat.
    
"""
import numpy as np
import math

# Deklarasi Variabel Global
func = []
arrEr = []
arrSol = []
answer = 0.0
I = np.zeros((50,50))

# Untuk mendapatkan nilai f(x)
def f(x):
    total = 0
    for i in range(0, len(func)):
        total = func[i] * x**i
    return total

# Jawaban real
def integral(a,b):
    for i in range(0, len(func)):
        func[i] = func[i]/(i+1)
    func.insert(0,0)
    integral = f(b) - f(a)
    return integral

# Rumus trapezoid
def trapezoidRule(numberOfTrapezoid, lower, upper):
    val = 0
    total = 0
    step = (upper - lower) / numberOfTrapezoid
    for i in range(1, numberOfTrapezoid - 1):
        val = val + f(lower + i * step)
    total = (step / 2) * (f(lower) + 2 * val + f(upper))

    return total

# Integrasi Romberg dengan error
def rombergIntegrationError(error_margin, lower, upper):
    er = 100
    ite = 0
    numberOfTrapezoid = 1
    I[1,1] = trapezoidRule(numberOfTrapezoid, lower, upper)
    arrSol.append(I[1,1])
    arrEr.append(-1)
    while er > error_margin:
        numberOfTrapezoid = 2 ** ite
        I[ite + 1, 1] = trapezoidRule(numberOfTrapezoid, lower, upper)
        for Iy in range(2, ite + 2):
            Ix = 2 + ite - Iy
            I[Ix,Iy] = ((4 ** (Iy-1) * I[Ix+1, Iy-1] - I[Ix, Iy - 1]) / (4 ** (Iy - 1) - 1))

        er = abs((I[1, ite+1] - I[2, ite]) / I[1, ite+1]) * 100
        arrEr.append(er)
        arrSol.append(I[1,ite+1])
        ite += 1

    approx = I[1, ite]
    return approx

# Integrasi romberg dengan iterasi
def rombergIntegrationIteration(iteration, lower, upper):
    numberOfTrapezoid = 1
    I[1,1] = trapezoidRule(numberOfTrapezoid, lower, upper)
    arrSol.append(I[1,1])
    arrEr.append(-1)
    for ite in range(iteration):
        numberOfTrapezoid = 2 ** ite
        I[ite + 1, 1] = trapezoidRule(numberOfTrapezoid, lower, upper)
        for Iy in range(2, ite + 2):
            Ix = 2 + ite - Iy
            I[Ix,Iy] = ((4 ** (Iy-1) * I[Ix+1, Iy-1] - I[Ix, Iy - 1]) / (4 ** (Iy - 1) - 1))

        er = abs((I[1, ite + 1] - I[2, ite]) / I[1, ite + 1]) * 100
        arrEr.append(er)
        arrSol.append(I[1,ite+1])


    approx = I[1, ite + 1]
    return approx

# Fungsi utama : input output dll
def main():
    print("")
    print("Misal : x^3 + 2x^2 + 7 --> derajat fungsi 3")
    degree = int(input("Input derajat fungsi: ")) + 1

    for i in range(degree):
        print("Koefisien x^", i, ": ", end="")
        inp = (int(input()))
        func.append(inp)

    upper_bound = int(input("\nInput batas awal: "))
    lower_bound = int(input("Input batas akhir: "))
    print("")

    print("w/error or w/iteration")
    flag = int(input("error = 1, iteration = 2 --->  "))

    if(flag == 1):
        error_margin = float(input("Input error margin: "))
        approx = rombergIntegrationError(error_margin,lower_bound,upper_bound)
    elif(flag == 2):
        iteration = int(input("Input jumlah iterasi: "))
        approx = rombergIntegrationIteration(iteration,lower_bound,upper_bound)

    print("")

    answer = integral(lower_bound,upper_bound)
    print("     Iterasi\t|\tRelative Error\t\t|\tHasil Integral\t|\tAbsolute Error")
    print("----------------+-------------------------------+-----------------------+---------------------")
    for i in range(len(arrEr)):
        print("\t%d\t|\t%f\t\t|\t%f\t|\t%f\n" % (i, arrEr[i], arrSol[i], abs((answer-arrSol[i]) / answer) * 100))
    print("Aproksimasi akhir : ", approx)
    print("Jawaban Real : ", answer, "\n")

if __name__ == '__main__':
    main()
