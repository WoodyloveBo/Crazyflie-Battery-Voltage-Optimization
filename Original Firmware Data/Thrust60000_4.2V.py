import numpy as np
import matplotlib.pyplot as plt

data1 = np.array(range(1000, 61000,  1000))

data2 = np.array([0,0,1,2,2,3,3,4,5,6,7,7,8,9,10,11,11,12,12,13,14,15,16,17,18,18,19,20,21,22,23,23,24,25,25,27,27,27,28,30,30,31,32,33,33,35,35,35,36,36,37,37,38,39,40,40,41,41,41,41])

coefficients = np.polyfit(data1, data2, 2)
print("polyfit:", coefficients)

poly_func = np.poly1d(coefficients)

data1_fit = np.linspace(min(data1), max(data1), 100)
data2_fit = poly_func(data1_fit)

plt.scatter(data1, data2, label='Weight(Thrust)')
plt.plot(data1_fit, data2_fit, label='PWM', color='red')
plt.xlabel('PWM(16bit = 65536 value)')
plt.ylabel('Thrust(g)')
plt.legend()
plt.title('PWM vs Thrust (60000 PWM, 4.2V)')
plt.show()