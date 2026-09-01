'''
머신러닝 - 지도학습
분류 경계선 하나로 분류 해줌.

'''
from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# X,y = load_breast_cancer(as_frame=True, return_X_y=True)
X,y = load_iris(as_frame=True, return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)


score = pipe.score(X_test, y_test)
accu_score = accuracy_score(y_test, y_pred) #

print('score:',score) # 모델 종류에 따라 자동 계산, LogisticRegression의 경우 accuracy_score()함수를 자동계산해줌
print('accu_score:',accu_score) ## score나 accuracy_score나 같음
