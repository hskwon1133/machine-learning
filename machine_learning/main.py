#개요
#머신러닝이란?
#규칙을 직접적으로 넣어주는 프로그램이 아니라 예시를 넣어주고 니가 그 규칙 알아서 찾아가렴 이라고 명령
import pickle

import numpy as np
#지도학습/비지도학습/강화학습
#회귀, 분류, 분포 등
#특징, 레이블 / 훈련, 테스트용 만들기
#학습진행, 예측, 평가  (fit, predict, score(r1,r2)

#1.100점일 경우 의심 필요 ( test용 dataset을 학습에 넣는 실수를 할 수 있음 )
# random_state(42)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

data = fetch_california_housing()

print(data.DESCR)
X = data.data
y = data.target


X = pd.DataFrame(X, columns=data.feature_names)
y = pd.DataFrame(y, columns=['target'])

df = X.copy() # df의 단독의 객체를 만들어야함.
df['target'] = y

df.to_csv('california_housing.csv')
df.describe().to_csv('california_housing_desc.csv', index=False)

# df.hist(figsize=(12,8), grid=False, bins=20)
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
pipe = make_pipeline(scaler,LinearRegression())
pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print('R2 score:', r2)
print('MAE:', mae)
print('RMSE:', rmse)
