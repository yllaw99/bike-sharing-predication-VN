import numpy as np
import matplotlib.pyplot as plt

X1 = np.array([0.44,0.61,0.89,0.74,0.71,0.59,0.85,0.94,0.91,0.69]) #Hum
X2 = np.array([0.23,0.46,0.45,0.62,0.64,0.64,0.61,0.61,0.54,0.33]) #temp
Y = np.array([1204,3117,4036,4978,5515,5923,5895,5345,5117,3940])


def LR(X1, X2, Y, eta, lanlap, theta0, theta1, theta2):
m = 10 #So luong phan tu
    for k in range(0,lanlap):
        tong0 = 0
        tong1 = 0
        tong2 = 0
        for i in range(0,m):
            h_i = theta0 + theta1 * X1[i] + theta2 * X2[i]
            tong0 = tong0+(Y[i]-h_i)*1
            tong1 = tong1+(Y[i]-h_i)*X1[i]
            tong2 = tong2+(Y[i]-h_i)*X2[i]

        theta0 = theta0+eta*(tong0/m)
        theta1 = theta1+eta*(tong1/m)
        theta2 = theta2+eta*(tong2/m)
        print("Lan lap ",k," theta0 = ",round(theta0,3)," theta1 = ", round(theta1,3)," theta2 = ", round(theta2,3))
    return [theta0,theta1,theta2]

#Toc do hoc 0.5, theta0=0, theta1=1
theta = LR(X1, X2, Y, 0.2, 1, 0, 1, 2)
X1_pred = 0.69
X2_pred = 0.33
X3 = np.array([5])
Y1 = theta[0] + theta[1]*X1_pred + theta[2]*X2_pred
# print(round(Y1,1)) #1089
plt.plot(X3, Y1, color="red")
plt.plot(X1, Y, "ro", color="blue")
plt.plot(X2, Y, "ro", color="yellow")
plt.xlabel("Gia tri thuoc tinh X theo do am")
plt.ylabel("Gia tri nhan Y")
plt.show()

