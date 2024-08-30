import numpy as np
import matplotlib.pyplot as plt

data1 = np.array(range(1000, 51000,  1000))

data2 = np.array([0, 1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12 ,13, 13, 14, 14, 15, 16, 17, 17, 18, 19, 20, 21, 22, 23, 23,24, 25, 26, 26, 27, 28, 29, 30, 30, 32, 33, 33, 34, 35, 36, 36, 37, 37, 37])

coefficients = np.polyfit(data1, data2, 2)
print("polyfit:", coefficients)

poly_func = np.poly1d(coefficients)

data1_fit = np.linspace(min(data1), max(data1), 100)
data2_fit = poly_func(data1_fit)

plt.scatter(data1, data2, label='Original Data')
plt.plot(data1_fit, data2_fit, label='2nd Order Polynomial Fit', color='red')
plt.xlabel('PWM(16bit = 65536 value)')
plt.ylabel('Thrust(g)')
plt.legend()
plt.title('PWM vs Thrust (50000 PWM)')
plt.show()
0
0
0
0
1
1
3
3
4
5
6
6
7
7
8
9
10
11
12
14
14
15
16
17
18
19
21
21
23
24
25
26
26
27
28
30
32
33
34
35
36
37
39
40
42
44
46
47
49
51
53
55
57
59
62
64
66
67
68
70
71
