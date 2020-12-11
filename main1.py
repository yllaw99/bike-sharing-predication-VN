import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

# Đọc dữ liệu từ file
data = pd.read_csv("D:\day.csv")

#bỏ bớt các cột không cần thiết trong bài này
drop1 = ['casual', 'registered', 'instant', 'dteday']
data = data.drop(drop1, axis=1)

def Project_Python(X_train,X_test,y_train,y_test):
    # CÂY HỒI QUY
    regressor = DecisionTreeRegressor(random_state = 0)
    regressor.fit(X_train, y_train)
    # Dự đoán
    y_pred = regressor.predict(X_test)
    # Đánh giá
    err = np.sqrt(mean_squared_error(y_test, y_pred))
    print('Cay hoi quy RMSE =',err) 
   

    # HỒI QUY TUYẾN TÍNH
    fit_LR = LinearRegression().fit(X_train, y_train)
    # Dự đoán
    pred_test = fit_LR.predict(X_test)
    # Đánh giá
    rmse = np.sqrt(mean_squared_error(y_test,pred_test))
    print('Hoi quy tuyen tinh RMSE =', rmse) 
 
 

# Sử dụng KFold phân chia tập dữ liệu để huấn luyện
kf = KFold(n_splits = 10)
for train_index, test_index in kf.split(data.iloc[:,0:10]):
    X_train, X_test = data.iloc[:,0:10].iloc[train_index], data.iloc[:,0:10].iloc[test_index]
    y_train, y_test = data.cnt.iloc[train_index], data.cnt.iloc[test_index]
    Project_Python(X_train,X_test,y_train,y_test)
    print('=============================================================================')

print("///////////////////////////////////////////////////////////////////////////////////////////////////")

# Sử dụng nghi thức train_test_split phân chia tập dữ liệu để huấn luyện
for i in range(1):
    X_train,X_test,y_train,y_test = train_test_split(data.iloc[:,0:10], data.cnt, test_size=1/3)
    Project_Python(X_train,X_test,y_train,y_test)
    print('=============================================================================')
# Sau khi huấn luyện với cả 2 nghi thức trên thì train_test_split cho kết quả tốt hơn