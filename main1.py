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
for i in range(10):
    X_train,X_test,y_train,y_test = train_test_split(data.iloc[:,0:10], data.cnt, test_size=1/3)
    Project_Python(X_train,X_test,y_train,y_test)
    print('=============================================================================')
# Sau khi huấn luyện với cả 2 nghi thức trên thì train_test_split cho kết quả tốt hơn

# Ket qua khi su dung KFold
'''
Cay hoi quy RMSE = 931.9624383452835
Hoi quy tuyen tinh RMSE = 499.7174562139495
=============================================================================
Cay hoi quy RMSE = 1096.33959467371
Hoi quy tuyen tinh RMSE = 801.9353148075944
=============================================================================
Cay hoi quy RMSE = 810.9036900400367
Hoi quy tuyen tinh RMSE = 1134.8438106303245
=============================================================================
Cay hoi quy RMSE = 960.2063491128937
Hoi quy tuyen tinh RMSE = 778.761379014613
=============================================================================
Cay hoi quy RMSE = 1259.0969856123404
Hoi quy tuyen tinh RMSE = 657.5428888562981
=============================================================================
Cay hoi quy RMSE = 1454.5771169109928
Hoi quy tuyen tinh RMSE = 954.5623815119274
=============================================================================
Cay hoi quy RMSE = 1487.1958535610954
Hoi quy tuyen tinh RMSE = 1161.0252044767105
=============================================================================
Cay hoi quy RMSE = 1011.8341003224504
Hoi quy tuyen tinh RMSE = 1243.5606301816717
=============================================================================
Cay hoi quy RMSE = 1160.540143492475
Hoi quy tuyen tinh RMSE = 1152.481226090318
=============================================================================
Cay hoi quy RMSE = 1669.655796699444
Hoi quy tuyen tinh RMSE = 1484.4509604036364
=============================================================================
'''
# Ket qua khi su dung train_test_split
'''
Cay hoi quy RMSE = 982.0297335320269
Hoi quy tuyen tinh RMSE = 942.3967010578215
=============================================================================
Cay hoi quy RMSE = 943.470828864376
Hoi quy tuyen tinh RMSE = 929.0583740256482
=============================================================================
Cay hoi quy RMSE = 931.0659390112418
Hoi quy tuyen tinh RMSE = 908.7518728065576
=============================================================================
Cay hoi quy RMSE = 981.0063334298654
Hoi quy tuyen tinh RMSE = 932.6149606423711
=============================================================================
Cay hoi quy RMSE = 908.0112839625281
Hoi quy tuyen tinh RMSE = 892.0465892168737
=============================================================================
Cay hoi quy RMSE = 993.530633072005
Hoi quy tuyen tinh RMSE = 816.2346723880212
=============================================================================
Cay hoi quy RMSE = 890.2183214448384
Hoi quy tuyen tinh RMSE = 888.102543133663
=============================================================================
Cay hoi quy RMSE = 996.5192927483502
Hoi quy tuyen tinh RMSE = 956.4149459091628
=============================================================================
Cay hoi quy RMSE = 904.1898058029811
Hoi quy tuyen tinh RMSE = 957.6789017005997
=============================================================================
Cay hoi quy RMSE = 904.886470553165
Hoi quy tuyen tinh RMSE = 988.9954011577056
=============================================================================
'''