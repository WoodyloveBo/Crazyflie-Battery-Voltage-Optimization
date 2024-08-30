import numpy as np
import matplotlib.pyplot as plt

data1 = np.array(range(1000, 61000,  1000))

data2 = np.array([0,0,1,3,3,3,4,5,5,6,7,8,8,9,9,10,11,11,12,13,15,15,15,16,17,18,19,20,20,21,21,22,24,24,25,26,26,27,28,29,31,31,31,32,33,34,34,35,36,37,38,38,40,40,42,42,42,43,44,44])

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
plt.title('PWM vs Thrust (60000 PWM, 4.1V)')
plt.show()