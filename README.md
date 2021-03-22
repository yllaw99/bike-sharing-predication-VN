<p align="center">
  <img height="300px" src="https://github.com/yllaw99/bike-sharing-predication-VN/blob/main/attributes.PNG"/>
 </p>
<p align="center">Attributes</p>
<p align="center">
  <img height="300px" src="https://github.com/yllaw99/bike-sharing-predication-VN/blob/main/average%20RMSE.PNG"/>
 </p>
<p align="center">RMSE Evaluate 10 loops average</p>

# Mô tả - Description:
- Áp dụng các giải thuật được học trên lớp Nguyên Lý Máy Học để dự đoán số lượng xe đạp sẽ được thuê dựa vào các yếu tố cho trước - Using algorithms that i'd learned on Machine Learning class to predict rental bike based on attributes given in CSV  file
- Tập dữ liệu dưới dạng CSV từ [Kaggle](https://www.kaggle.com/lakshmi25npathi/bike-sharing-dataset) - Dataset CSV file is taken from [Kaggle](https://www.kaggle.com/lakshmi25npathi/bike-sharing-dataset)
- Tiền xử lý - Dataset pre-processing:
      Bỏ bớt 4 cột dữ liệu - Drop 4 data columns.
      Chỉ sử dụng tập dữ liệu [day.csv] - Only use [day.csv] dataset.
- Model:
      [DecisionTreeRegressor] & [Linear Regression].
- Test:
      Sử dụng [Mean Square Error] để đánh giá độ chính xác - [Mean Square Error] is used for evaluating the prediction accuracy.

# Yêu cầu - Requirements
      1) python Pandas version `0.20.3` install using:- ' pip install pandas '
      2) python Nupmy version `1.14.2` install using:-  ' pip install numpy '
      3) python Scikit learn lib `3.2.5` install:-      ' pip install sklearn '

# Lưu ý - Notes
- File [main1.py] là file dùng toàn bộ dữ liệu trong file CSV - [main1.py] is the main code file using all data in CSV dataset
- File [demo.py] là file chỉ dùng 10 dòng dữ liệu để báo cáo - [demo.py] is only use 10 rows in dataset for presentation

# Góp ý - Issues
Liên hệ mình qua [Facebook](https://facebook.com/yllaw99)
Contact me via [Facebook](https://facebook.com/yllaw99)

# Người hướng dẫn - Mentor
- Cô [Trần Nguyễn Minh Thư](#Miss-Tran-Nguyen-Minh-Thu)
- [Can Tho University]

# Đồng tác giả - Co-Author:
- Edit Code: Đặng Văn Tường
- Main code: Phạm Trí Minh
- Presentation: Đặng Văn Tường
- Prepare ppt file: Nguyễn Hùng Thuận
