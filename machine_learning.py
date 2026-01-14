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


#import numpy as np
#import matplotlib.pyplot as plt

