import random
import numpy 
import statistics

# Q1
iterations = 10^5
p = [0.4, 0.45, 0.48]
insertCount = 0

ET = numpy.zeros(3, dtype = float)
EM = numpy.zeros(3, dtype = float)
PMgeTen = numpy.zeros(3, dtype = float)
stdevT = numpy.zeros(3, dtype = float)
stdevM = numpy.zeros(3, dtype = float)
stdevPMgeTen = numpy.zeros(3, dtype = float)

# new probability
for pi in p:
    numBets = 0
    currentGame = 0
    T_pi = numpy.zeros(10^5, dtype = int)
    M_pi = numpy.zeros(10^5, dtype = int)
    MgeTen = []

    # new iteration
    for x in range(iterations):
        funds = 5
        maxFunds = 5
        
        # new game
        while funds > 0:
            currentGame = random.random()
            
            # if player wins
            if currentGame <= pi:
                funds = funds + 1
                numBets = numBets + 1

            # if player loses
            else:
                funds = funds - 1
                numBets = numBets + 1
            
            # independent of win or loss
            numBets = numBets + 1    
            if funds > maxFunds:
                maxFunds = funds
                
            # store before next iteration
            if funds == 0:
                T_pi[x] = numBets
                M_pi[x] = maxFunds
                
    # find where M >= 10
    for x in range(iterations):
        if M_pi[x] >= 10:
            MgeTen.append(M_pi[x])

    ET[insertCount] = numpy.mean(T_pi)
    EM[insertCount] = numpy.mean(M_pi)
    PMgeTen[insertCount] = numpy.mean(MgeTen) / len(MgeTen)
    stdevT[insertCount] = statistics.stdev(T_pi, ET[insertCount])
    stdevM[insertCount] = statistics.stdev(M_pi, EM[insertCount])
    stdevPMgeTen[insertCount] = statistics.stdev(MgeTen, PMgeTen[insertCount])
    insertCount = insertCount + 1
    
print("u_1(p = 0.4) = " + str(ET[0]) + ", u_1(p = 0.45) = " + str(ET[1]) + ", u_1(p = 0.48) = " + str(ET[2]) + " std.dev(u_1(n = 0.4)) = " + str(stdevT[0]) + " std.dev(u_1(n = 0.45)) = " + str(stdevT[1]) + " std.dev(u_1(n = 0.48)) = " + str(stdevT[2]))
print("u_2(p = 0.4) = " + str(EM[0]) + ", u_2(p = 0.45) = " + str(EM[1]) + ", u_2(p = 0.48) = " + str(EM[2]) + " std.dev(u_2(n = 0.4)) = " + str(stdevT[0]) + " std.dev(u_2(n = 0.45)) = " + str(stdevT[1]) + " std.dev(u_2(n = 0.48)) = " + str(stdevT[2]))
print("u_3(p = 0.4) = " + str(PMgeTen[0]) + ", u_3(p = 0.45) = " + str(PMgeTen[1]) + ", u_3(p = 0.48) = " + str(PMgeTen[2]) + " std.dev(u_3(n = 0.4)) = " + str(PMgeTen[0]) + " std.dev(u_2(n = 0.45)) = " + str(PMgeTen[1]) + " std.dev(u_2(n = 0.48)) = " + str(PMgeTen[2]))

print(ET)
print(EM)
print(PMgeTen)