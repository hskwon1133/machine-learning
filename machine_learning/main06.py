#비지도학습(군집화, 차원축소)
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 군집화
# ===== K Means + elbow =====
# iris = load_iris()
# X = iris.data
# scaler = StandardScaler()
# scaler.fit(X)
# X_scaled = scaler.transform(X)
#
# for k in range(2,9):
#     m = KMeans(n_clusters=k, n_init = 10, random_state=42)
#     m.fit(X_scaled)
#     y_pred = m.predict(X_scaled)
#     sil_score = silhouette_score(X_scaled, y_pred)
#     print(f'[{k}] 응집도 : {m.inertia_}, 실루엣 : {sil_score}')

# 차원축소 + 주성분분석(PCA)
# iris = load_iris()
# X = iris.data
# scaler = StandardScaler() #스케일러 학습 진행
# scaler.fit(X)
# X_scaled = scaler.transform(X)
#
# m = PCA(n_components=2) # 2차원까지 줄이겠다라는 뜻
# m.fit(X_scaled)
# X_2d = m.transform(X_scaled) #fit_transform
#
# print(f'X: {X.shape}')
# print(f'X_2d: {X_2d.shape}')
# print(f'X: {X}')
# print(f'X_2d: {X_2d}')

# 차원축소 + 주성분분석(PCA) + 군집합(K-Means)
# iris = load_iris()
# X = iris.data
# scaler = StandardScaler()
# scaler.fit(X)
# X_scaled = scaler.transform(X)
#
# model_km = KMeans(n_clusters=3, n_init=10,  random_state=42) # 3개 종류로 구분 ( 그전에는 best를 찾아야함. for문으로), n_init은 중심점
# model_km.fit(X_scaled) #가까운 선 연결하고, 중심점 이동하고 하는 학습을 진행함 (어떤 타입으로 그룹을 나눌지)
# labels = model_km.predict(X_scaled)  # 학습기준 예측 진행
#
# #pca를 사용해서 그림으로 볼것임
# model_pca = PCA(n_components=2)
# model_pca.fit(X_scaled)
# X_2d = model_pca.transform(X_scaled)
#
# x_data = X_2d[:,0] #채널0
# y_data = X_2d[:,1] #채널1
#
# plt.figure(figsize=(8,6))
# plt.scatter(x_data, y_data, c=labels, s=30, cmap='viridis')
# plt.show()

#