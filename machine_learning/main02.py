# 선형 Regression, 다항, 비선형

# 지도 학습 (문제랑 정답을 알려줌)
    # 노이즈 : 지금 알 필요가 없음
    # 회귀를 쓰는 이유 : 연속되는 값을 예측할 때
    # 과소적합 vs 과적합 (덜하거나 과하거나)

# 규제 (과적합을 눌러주는 작업)

# 선형 모델을 만들어서 규칙을 줘서 결과가 나오게.

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. 지도 학습
# y = 3x + 2

x = np.linspace(1,100,108)

y = 3 * x + 2

#X행을 만들어 줌
x = x.reshape(-1,1) #2차원, 숫자, 행으로 옮-기기

#학습
m = LinearRegression()
m.fit(x, y)

print('coef_:', m.coef_)  #가중치, X절편
print('intercept_:', m.intercept_)  # y절편

# y = ax + a2x + a3x (a = 키, a2 = 나이, a3 = 연봉일 경우 가중치에 대한 계수가 다르게 나올 것임)
# 가중치가 크니까 계수가 크게 나와서 연관성이 있다고 판단하면 X, 스케일링이 필요함 (모든 x값들이 특정 분포 범위에서 유지할 수 있게 만들어 줌)
# 모델이 규칙을 찾아서 선을 그어서 예측을 함. 머신러닝된 모델이 오차를 확인하고 오차가 가장 적은 쪽에 선을 그어줌.
# 기울기, 경사에 따라 적용할 수 있도록 최소 제곱법을 통해 오차를 찾아서 적절한 선을 그어주면 됨.


# 다항회기