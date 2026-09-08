#퍼셉트론, MLP
#어떤 X(독립변수)가 얼마나 중요한가. 예를 들면 타이타닉에서 성별이 생존여부에 얼마나 큰 상관관계를 가지나.
#Xor의 경우 좌표만으로 선 하나로 기준을 세워 구분하기 어려움
# y = ax + b (가중합+편향)  연산 결과를 다 더해주고 특정 기준선만큼 조정해주고, 판단..을 어뜨케 한다고..?
# 편향은 왜 필요한가?
# 구조적으로 선 두개 이상 묶어주는 작업을 해야하고, 신경망을 쌓아서 이어줘야함. 다층구조

import numpy as np


#계단함수를 엄청 심플하게 구현함
def step(x) :
    if x>0:
        return 1
    else:
        return 0

# data = 10
# result = step(data)
# print(result)

#두가지 입력값을 받아서

# a, b  = map(int, input('숫자:').split())
# x = np.array([0,0]) #입력값 x1, x2
# w = np.array([0.5,0.5]) #가중치 정하기 (random하게) x1의 가중치, x2의 가중치. 일단은 0,0으로 정함
# b = 0  #편향 정하기 원래는 컴퓨터가 random으로 정함
#
# z = np.dot(x,w)+b
# # x1,x2 1,2 / w1,w2 3,4일 경우 1*3 + 2*4 + 0= 11
# y = step(z)
# print(y)
# 최종 1,1이 1이 나오고, 나머지 값이 0으로 나오게 하는 방법 (and로 진행한 경우)
# 활성함수를 거쳐야지, 직선이 아닌 곡선 구현 가능
# 가중치 0.5 / 편향치 -0.9(인계값 조절) 같은 가중치를 주어도 편향치가 다름으로 각각의 결과를 낳는다.
# 딥러닝은 선형 모델로 만들어짐 RandomForest와는 무관


# or의 경우?
# 가중치 0.5씩 / 편향치 0 이하

def perceptron(x,w,b):
    z = np.dot(x,w)+b
    y = step(z) #활성화함수z / 판단을 도와주는 함수
    return y # x를입력해서 perceptron(신경망)을 통해 y를 출력함

def AND(x1,x2):
    y = perceptron(np.array([x1,x2]),np.array([0.5,0.5]),-0.9)
    return y

def OR(x1,x2):
    y = perceptron(np.array([x1,x2]),np.array([0.5,0.5]),-0.4)
    return y

def NAND(x1,x2):
    y = not AND(x1,x2)
    return int(y)

def XOR(x1,x2):
    t1 = AND(x1,x2)
    t2 = OR(x1,x2)
    y = AND(t1,t2) # t1, t2 둘 다 적용 처음 0, 마지막 1이 True가 되면서 XOR이 됨. (선을 두개 그어야함), 멀티레이어 다층 신경망이라고 함.
    return y

print('---AND---')
print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))
print('---OR---')
print(OR(0,0))
print(OR(1,0))
print(OR(0,1))
print(OR(1,1))
print('---NAND---')
print(NAND(0,0))
print(NAND(1,0))
print(NAND(0,1))
print(NAND(1,1))
print('---XOR---')
print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))


