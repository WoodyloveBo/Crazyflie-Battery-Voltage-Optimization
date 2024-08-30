import numpy as np
import matplotlib.pyplot as plt

data1 = np.array(range(1000, 61000,  1000))

data2 = np.array([0,0,1,1,2,3,3,4,5,5,6,7,8,9,10,11,12,12,13,14,15,16,17,17,18,18,19,20,20,21,22,23,23,24,25,25,26,26,27,28,29,30,31,32,33,34,35,36,36,37,38,39,40,41,42,42,43,44,44,44])

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
plt.title('PWM vs Thrust (60000 PWM, 3.9V)')
plt.show()