import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

# Đọc dữ liệu từ file
data = pd.read_csv("D:\Coding_WorkSpace\ML\Bike-Sharing-Dataset\day.csv")

#bỏ bớt các cột không cần thiết trong bài này
drop1 = ['casual', 'registered', 'instant', 'dteday']
data = data.drop(drop1, axis=1)

def Regressor_Algorithm(X_train,X_test,y_train,y_test):
    # CÂY HỒI QUY
    regressor = DecisionTreeRegressor(random_state = 0)
    regressor.fit(X_train, y_train)
    # Dự đoán
    y_pred = regressor.predict(X_test)
    # Đánh giá
    err = np.sqrt(mean_squared_error(y_test, y_pred))
    print('Cay hoi quy RMSE =', round(err,0))
    # HỒI QUY TUYẾN TÍNH
    fit_LR = LinearRegression().fit(X_train, y_train)
    # Dự đoán
    pred_test = fit_LR.predict(X_test)
    # Đánh giá
    rmse = np.sqrt(mean_squared_error(y_test,pred_test))
    print('Hoi quy tuyen tinh RMSE =', round(rmse,0))

# Sử dụng nghi thức hold-out phân chia tập dữ liệu để huấn luyện
# Lặp 10 lần để so sánh 2 giải thuật
for i in range(10):
    X_train,X_test,y_train,y_test = train_test_split(data.iloc[:,0:10], data.cnt, test_size=1/3)
    Regressor_Algorithm(X_train,X_test,y_train,y_test)
    print('=====================================================')