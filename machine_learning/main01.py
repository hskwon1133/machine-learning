from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# df = pd.DataFrame({
#     'age' : [20, 30, np.nan, 40, 50],
#     'score' : [100, np.nan, 80, 70, np.nan]
# })

# df['age']=df['age'].fillna(df['age'].mean()).astype(int)
# df['score']=df['score'].fillna(df['score'].mean()).astype(int)

#결측치를 알아서 잘 채워줌
# imputer = SimpleImputer(strategy='median').set_output(transform='pandas')
# result = imputer.fit_transform(df)
# print(result)
# print(type(result))

#스케일링
#standard scale (std 활용, 주요하게 쓰임)
#MinMax Scale (min, max활용)
#거리기반 알고리즘에 스케일링은 꼭 필요함. 값이 한쪽이 너무 크면, 크게 잡아먹기 때문에 비슷한 수준의 스케일링이 필요함.
#랜덤포레스트의 경우는 스케일링 의미가 없음.
# X = np.array([[1.0, 100.0],
#               [2.0, 300.0],
#               [3.0, 500.0],
#               [4.0, 700.0]])
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# print(X_scaled)

# 범주형 인코딩 (순위가 X)
# df = pd.DataFrame({"color": ["red", "green", "blue", "green"]})
# result = pd.get_dummies(df, columns =['color'], drop_first = True) # , axis=1
# result = df['color'].map({"red":1, "green":2, "blue":3, "green":4}) #순위, 계층 (크기가 상관이 있을 때) 쓰이면 좋음
# print(result)

#범주형 인코디 (순위가 O)
# df = pd.DataFrame({
#     "size": ["소", "대", "중", "소"],
#     "grade" : ["Bronze", "Gold", "Silver", "Bronze"]
# })
# result = df['size'].map({'소': 1, '중':2, '대':3}, ) #map은 dict, series 형식을 받음.
# temp=['소', '중', '대']
# temp1=["Bronze", "Silver","Gold"]
# enc = OrdinalEncoder(categories= [temp, temp1])
# df[['size', 'grade']] = enc.fit_transform(df[['size', 'grade']])
# print(df)


#파생컬럼, 중복제거, 시계열 인덱싱

#===누수없이 전처리===
# 데이터 준비
X,y = load_iris(as_frame = True,  return_X_y=True)
print(X.head())

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# 전처리
scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test) # test에 fit 적용 X
# print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

# 모델
knn = KNeighborsClassifier(n_neighbors=3) #n_neighbors 숫자는 무조건 홀수. 짝수는 동률이 나오기 때문에

# 파이프라인 (전처리 + 학습) sklearn이 만들어 준 전처리/학습 내용을 파이프라인에서 진행 가능, fit_transform
pipe = make_pipeline(scaler,knn)

# 학습
pipe.fit(X_train,y_train)

# 예측
y_pred = pipe.predict(X_test)

# 평가?
print(y_pred)
acc_score = accuracy_score(y_test, y_pred)
print('accuracy_score:', acc_score)