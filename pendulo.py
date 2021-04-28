import numpy as np 
from matplotlib import pyplot as plt 
from sklearn.metrics import mean_squared_error
import matplotlib.patches as mpatches

x_0 = 0
angulo_0 =90
h=0.000005 
n=2000000
g=9.81
l=0.31

tiempo = np.zeros(n)
x = np.zeros(n)
angulo = np.zeros(n)
x[0] = x_0
angulo[0] = angulo_0*np.pi/180.0

for i in range(n-1):
    tiempo[i+1] = tiempo[i] + h
    x[i+1] = x[i] + h*-(g/l)*np.sin(angulo[i])
    angulo[i+1] = angulo[i] + h*x[i]

#====================================================
expe=(3*np.exp(0*tiempo))*np.sin(2*tiempo+1.5)
teo=angulo
#====================================================

plt.xlabel('tiempo(s)',size=14)
plt.ylabel('Ángulo (rad)',size=14)
plt.title('Péndulo plano',size=14)
plt.plot(tiempo,teo,lw=3,color='blue')
plt.plot(tiempo, expe,lw=3,color='red')
#Leyenda
id_xc= mpatches.Patch(color='red', label='Experimental')
id_xp= mpatches.Patch(color='blue', label='Teórico')
plt.legend(handles=[id_xc, id_xp])

plt.show()

rmse = mean_squared_error(expe, teo, squared=False)
print(rmse)
