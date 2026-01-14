# tensorflow 로드
import tensorflow as tf
print(tf.__version__) #2.20.0
# version 앞뒤로 두 개의 밑줄을 사용한다

from tensorflow import keras #tf.keras로 사용하기에 번거러워서 별도 임포트

# MNIST 데이터를 학습용, 테스트 데이터로 구분하여 읽어옴
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

'''
# 데이터셋의 크기 확인
#print('train_images.shape =', train_images.shape) #(60000, 28, 28)
#print('test_images.shape =', test_images.shape) #(10000, 28, 28)
#print('train_labels.shape =', train_labels.shape) #(60000,)
#print('test_labels.shape =', test_labels.shape) #(10000,)
'''

'''
# 학습용 이미지 데이터의 첫번째 이미지 출력
num = train_images[0] #6만장 중 첫번째 이미지
for i in range(28):
    for j in range(28):
        print('{:4d}'.format(num[i][j]), end='')
    print()
print(train_labels[0]) #정답은? 5
'''

# 입력값 전처리 : 0에서 1사이의 값으로 입력 데이터를 가공함
(train_images, test_images) = (train_images / 255, test_images / 255)

# 신경망 모델 구성
model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)), #입력층: 28x28 크기의 2차원 배열임
    keras.layers.Flatten(), #28x28 2차원 배열을 784 1차원 배열로 변환. 뉴런 연결을 위해 필요
    keras.layers.Dense(1024, activation='relu'), #뉴런 활성화는 relu 사용
    keras.layers.Dense(512, activation='relu'), #뉴런 활성화는 relu 사용
    keras.layers.Dense(256, activation='relu'), #뉴런 활성화는 relu 사용
    keras.layers.Dense(128, activation='relu'), #뉴런 활성화는 relu 사용
    keras.layers.Dense(64, activation='relu'), #뉴런 활성화는 relu 사용
    keras.layers.Dense(10, activation='softmax') #출력이 2개 이상에서는 softmax 사용
])
model.summary()   # 모델의 구조를 요약하여 살펴보자

# 모델 컴파일 : 손실함수와 최적화 알고리즘 설정
model.compile(optimizer='adam', #최적화 알고리즘
              loss='sparse_categorical_crossentropy', #답을 one-hot 인코딩으로 바꾸지 않고 사용하겠다는 의미임.
               # [0 0 1 0 0 0 0 0 0 0 0] 이런식으로 바꾸지 않음
              metrics=['accuracy']) #정확도를 지표로 삼음

model.fit(train_images, train_labels, epochs=5) #모델 학습. 5회 반복

# 모델 평가
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\n테스트 정확도:', test_acc)

# 모델 저장
#model.save('mnist_model.keras') #모델 파일명 지정하여 저장
model.save('my_first_DNN_model.keras') #모델 파일명 지정하여 저장
# 윗 학습모델의 스코어가 더 높다. 그래서 위에걸로 사용한다.

#import numpy as np
#import matplotlib.pyplot as plt

