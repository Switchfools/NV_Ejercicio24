import numpy as np
import matplotlib.pylab as plt
Lambda=np.linspace(0.1,30,200)
Normalizacion=1/(np.exp(-1/Lambda)-np.exp(-20/Lambda))
data=np.array([1.2,2.5,2.8,5.0])
def probabilidad():
    prob=np.ones(len(Lambda))
    for i in range(len(Lambda)):
        for j in range(len(data)):
            prob[i]*=((Normalizacion[i]/Lambda[i])*np.exp(-data[j]/Lambda[i]))
    return(prob)
def probLambda():
    return np.ones(len(Lambda))/len(Lambda)

ProbTotal=probabilidad()*probLambda()
ProbTotal*=1/np.sum(ProbTotal)
plt.plot(Lambda,ProbTotal)
plt.savefig('prob.png')
