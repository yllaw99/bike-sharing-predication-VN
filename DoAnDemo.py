import numpy as np
import matplotlib.pyplot as plt

X1 = np.array([0.23,0.46,0.45,0.62,0.64,0.64,0.61,0.61,0.54,0.33]) #temp
X2 = np.array([0.44,0.61,0.89,0.74,0.71,0.59,0.85,0.94,0.91,0.69]) #Hum
Y = np.array([1204,3117,4036,4978,5515,5923,5895,5345,5117,3940])


def LR(X1, X2, Y, eta, lanlap, theta0, theta1, theta2):
    m = len(X1) #So luong phan tu
    for k in range(0, lanlap):
        print('lan lap thu ', k)
        for i in range(0, m):
            h_i = theta0 + theta1*X1[i] + theta2*X2[i]
            #theta0
            theta0 = theta0 + eta*(Y[i] - h_i)*1
            print('theta0 = ',round(theta0,1))
            #theta1
            theta1 = theta1 + eta*(Y[i] - h_i)*X1[i]
            print('theta1 = ',round(theta1,1))
            #theta2
            theta2 = theta2 + eta*(Y[i] - h_i)*X2[i]
            print('theta2 = ', round(theta2,1))
    return [round(theta0, 3), round(theta1, 3), round(theta2, 3)]


#Toc do hoc 0.5, theta0=0, theta1=1
theta = LR(X1, X2, Y, 0.5, 5, 0, 1, 2)
X1_pred = 0.15
X2_pred = 0.45
Y1 = theta[0] + theta[1]*X1_pred + theta[2]*X2_pred
print(round(Y1,1)) #1089
# plt.plot(X1, Y1, color="red")
# plt.plot(X, Y, "ro", color="blue")
# plt.xlabel("Gia tri thuoc tinh X theo do am")
# plt.ylabel("Gia tri nhan Y")
# plt.show()
