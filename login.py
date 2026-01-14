# tensorflow 로드
import tensorflow as tf
from tensorflow import keras #tf.keras로 사용하기에 번거러워서 별도 임포트
from show_me_your_password import get_password_image

def main():
    loaded =keras.models.load_model('./my_first_DNN_model.keras')
    print(loaded.summary())
    login()

if __name__ == '__main__':
    main()


def login():
    pass_img = []
    captured_image = get_password_image()
    if captured_image is not None:
        pass_img.append(captured_image)
        print("이미지를 성공적으로 받아왔습니다.")
        # 저장된 이미지를 확인하고 싶다면 아래 주석을 해제하세요.
        # import cv2
        # cv2.imshow("Received Image", pass_img[0])
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    else:
        print("이미지를 받아오지 못했습니다.")

def signup():
    pass

