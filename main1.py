import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

data = pd.read_csv("./Bike-Sharing-Dataset/day_copy.csv")

#bỏ bớt các cột không cần thiết trong bài này
drop1 = ['casual', 'registered', 'instant', 'dteday']
data = data.drop(drop1, axis=1)

'''col = ['season','yr','mnth','holiday','weekday', 'workingday', 'weathersit']
dummy_data = pd.get_dummies(data=data, columns=col)'''
X_train,X_test,y_train,y_test = train_test_split(data.iloc[:,0:10], data.cnt, test_size=1/3, random_state=100)
#print(X_train.shape) #(487,10)
#print(X_test.shape) #(244,10)
#print(y_train.shape) #(487,)
#print(y_test.shape) #(244,)

# CÂY HỒI QUY
'''regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, y_train)
    # Dự đoán
y_pred = regressor.predict(X_test)
    # Đánh giá
err = np.sqrt(mean_squared_error(y_test, y_pred))
print('RMSE =',err) #RMSE = 961.68
'''
# HỒI QUY TUYẾN TÍNH
'''fit_LR = LinearRegression().fit(X_train, y_train)
    # Dự đoán
pred_test = fit_LR.predict(X_test)
    # Đánh giá
rmse = np.sqrt(mean_squared_error(y_test,pred_test))
print('RMSE =', rmse) #RMSE = 874.84
'''
