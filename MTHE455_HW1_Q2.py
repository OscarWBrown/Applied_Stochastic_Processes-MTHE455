import random
import numpy
import statistics

# Q2
iterations = 10**5
n =[10, 20]
insertCount = 0

ET = numpy.zeros(2, dtype = float)
EX = numpy.zeros(2, dtype = float)
stdevT = numpy.zeros(2, dtype = float)
stdevX = numpy.zeros(2, dtype = float)

# new number of coupons
for ni in n:

    X = numpy.zeros(iterations, dtype = int)
    T = numpy.zeros(iterations, dtype = int)

    # new iteration
    for i in range(iterations):
        cn = numpy.zeros(ni, dtype = int)
        turns = 0
        all_cn = 0
        max_c = 0

        # new game 
        while all_cn < ni:
            turns = turns = turns + 1
            c = random.randint(0, ni - 1)
            all_cn = 0
            cn[c] = cn[c] + 1
            max_c = 0

            # check if all types of coupons have been found
            for j in range(ni):
                if cn[j - 1] > 0:
                    all_cn = all_cn + 1

                if j == ni:
                    break
                else:
                    if cn[j - 1] > cn[j]:
                        max_c = cn[j - 1]
                    else:
                        max_c = cn[j]

        X[i] = max_c
        T[i] = turns

    ET[insertCount] = numpy.mean(T)
    EX[insertCount] = numpy.mean(X)
    stdevT[insertCount] = statistics.stdev(T, ET[insertCount])
    stdevX[insertCount] = statistics.stdev(X, EX[insertCount])
    insertCount = insertCount + 1

print("u_1(n = 10) = " + str(ET[0]) + ", u_1(n = 20) = " + str(ET[1]) + " std.dev(u_1(n = 10)) = " + str(stdevT[0])  + " std.dev(u_1(n = 20)) = " + str(stdevT[1]))
print("u_2(n = 10) = " + str(EX[0]) + ", u_2(n = 20) = " + str(EX[1]) + " std.dev(u_2(n = 10)) = " + str(stdevX[0])  + " std.dev(u_2(n = 20)) = " + str(stdevX[1]))