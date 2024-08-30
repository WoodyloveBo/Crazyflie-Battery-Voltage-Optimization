import numpy as np
import matplotlib.pyplot as plt

data1 = np.array(range(1000, 61000,  1000))

data2 = np.array([0,0,1,1,2,3,4,4,4,6,6,7,8,10,10,11,12,12,13,14,16,16,16,17,19,19,21,21,23,24,25,26,27,28,29,31,31,31,32,34,35,37,38,39,40,41,42,43,44,44,46,46,47,48,48,49,50,49,49,49])

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
plt.title('PWM vs Thrust (60000 PWM, 3.7V)')
plt.show()