'''
머신러닝 - 지도학습
분류 경계선 하나로 분류 해줌.

'''
import numpy as np
from sklearn.datasets import load_breast_cancer, load_iris, load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# ===== 로지스틱회귀 =====
X,y = load_breast_cancer(as_frame=True, return_X_y=True)
# X,y = load_iris(as_frame=True, return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
#
# pipe.fit(X_train, y_train)
#
# y_pred = pipe.predict(X_test)
#
#
# score = pipe.score(X_test, y_test)
# accu_score = accuracy_score(y_test, y_pred) #
#
# print('score:',score) # 모델 종류에 따라 자동 계산, LogisticRegression의 경우 accuracy_score()함수를 자동계산해줌
# print('accu_score:',accu_score) ## score나 accuracy_score나 같음
#
# proba = pipe.predict_proba(X_test)
# print('proba:',proba)
# print('proba type:',type(proba))


# === KNN ===
# KDR?
# 인접이 많으면 어떤 판단을 해야할지 모름. K값이 너무 커서 과소적합이 발생하지 않도록 해야할 필요가 있음.
# KNN에서는 학습에서 해야할 것들이 없음. lazy learning이라고 지칭. 훈련시간 별로 안들고, 예측은 시간이 걸림

# KNeighborsClassifier 함수에서 주요하게 쓰이는 옵션에 대해서도 설명, 노션 정리 부탁해

# X,y = load_wine(return_X_y=True)
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# pipe = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors = 5))
#
# pipe.fit(X_train, y_train)
#
# y_pred = pipe.predict(X_test)
#
# sc = pipe.score(X_test, y_test)
# asc = accuracy_score(y_test, y_pred)
#
# print(f'Score:  {sc:.2f}')
# print(f'Accuracy: {asc:.2f}')


# === Supporter Vector Machine (svm) ==== (와인 데이터)
# 경계선을 넓은 도로 형태로 만들어 줌. 거리기반. 커널을 만들어 주면 3차원으로 공간감을 줘서 구분을 해줌. (추가 설명 쉽게 부탁해).
# 커널을 통해서 곡선형 분석도 가능
# 하이퍼 파라미터는 'C'이며 마진의 넓이를 뜻함. C가 작아지면 마진이 넓어짐(과소적합 발생위험). C값을 올려두면 마진(도로폭)이 타이트해짐 (너무 좁으면 과적합 발생위험)
# Support Vector 분류/회귀가 다 있음.
# 경계선에 새로운 데이터가 들어올 때 조정됨. 그 외에 중간에 들어온 데이터 값들은 학습에 영향을 주지 않음. (경계선이 끌려가지 않음)

# pipe = make_pipeline(StandardScaler(), SVC()) #C, Kernal #SVC suppoter Ventor Classifier, #kernel='rdf', 문자열이 되어야한다고? 뭔소리지

# pipe = make_pipeline(StandardScaler(), ())
#
# pipe.fit(X_train, y_train)
#
# y_pred = pipe.predict(X_test)
#
# sc = pipe.score(X_test, y_test)
# asc = accuracy_score(y_test, y_pred)
#
# print(f'Score:  {sc:.2f}')
# print(f'Accuracy: {asc:.2f}')


# === 모델별 성능 비교 ==== (유방암 데이터)

# 내가 했던 것
# for m in [LogisticRegression(max_iter=500), KNeighborsClassifier(n_neighbors=3), SVC()] :
#     pipe = make_pipeline(StandardScaler(), m)
#     pipe.fit(X_train, y_train)
#     y_pred = pipe.predict(X_test)
#     score = pipe.score(X_test, y_test)
#     accu_score = accuracy_score(y_test, y_pred)
#     print(f'{type(m).__name__} - score:{score:.2f}, accu_score:{accu_score:.2f}')

# 강의에서 들은 것
models = {'LogisticRegression': make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
    , 'KNeighborsClassifier': make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
    , 'SVC': make_pipeline(StandardScaler(), SVC())}

for model_name, model_pipeline in models.items():
    model_pipeline.fit(X_train, y_train)
    y_pred = model_pipeline.predict(X_test)
    score = model_pipeline.score(X_test, y_test)
    accu_score = accuracy_score(y_test, y_pred)
    print(f'{model_name} - score:{score:.2f}, accu_score:{accu_score:.2f}')


