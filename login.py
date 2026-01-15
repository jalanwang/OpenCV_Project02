# tensorflow 로드
import tensorflow as tf
from tensorflow import keras #tf.keras로 사용하기에 번거러워서 별도 임포트
from show_me_your_password import get_password_image, init_webcam
import cv2
import numpy as np

# 테스트 번호/ 잘 안되는 번호를 채택. 이건 단독으로 실행할 때 사용
CORRECT_PASSWORD = [6,6]

def preprocess_image(img):
    """
    캡처된 이미지를 모델 입력에 맞게 전처리합니다.
    (28x28 크기 조정, 정규화)
    """
    # 모델 입력은 (28, 28) 크기이므로 리사이즈합니다.
    resized_img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
    # 모델 입력을 위해 차원을 확장하고 (28, 28) -> (1, 28, 28, 1)
    # 값을 0~1 사이로 정규화합니다.
    preprocessed = resized_img.reshape(1, 28, 28, 1).astype('float32') / 255.0
    return preprocessed

def get_input_sequence(model, password_length=len(CORRECT_PASSWORD)):
    """
    웹캠을 설정하고 지정된 횟수만큼 이미지 입력을 받아 예측된 숫자 리스트를 반환합니다.
    """
    cap = init_webcam()
    if cap is None:
        return None

    entered_password = []
    print(f"비밀번호 {password_length}자리를 순서대로 입력하세요.")

    for i in range(password_length):
        print(f"{i+1}번째 숫자를 보여주고 'c'를 누르세요.")
        # cap 객체를 전달하여 카메라를 재사용
        result = get_password_image(cap, index=i)

        if result is not None:
            filename = result[0]
            captured_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            # 이미지를 모델에 맞게 전처리
            preprocessed_img = preprocess_image(captured_image)
            
            # 모델로 숫자 예측
            prediction = model.predict(preprocessed_img)
            predicted_digit = np.argmax(prediction)
            entered_password.append(predicted_digit)
            print(f"인식된 숫자: {predicted_digit}")
        else:
            print("이미지를 받아오지 못했습니다. 로그인을 다시 시도하세요.")
            cap.release()
            cv2.destroyAllWindows()
            return None

    cap.release()
    cv2.destroyAllWindows()
    return entered_password

def check_password(entered_password, correct_password=CORRECT_PASSWORD):
    """
    입력된 비밀번호가 맞는지 확인합니다.
    """
    # 비밀번호 확인
    if entered_password == correct_password:
        print("\n로그인 성공!")
        print('='*30)
        print(f'Hello Supervisor!')
        print('Welcome to the secure system.')
        print('='*30)
        
    else:
        print(f"\n로그인 실패. 입력된 비밀번호: {entered_password}")

def login(model, correct_password=CORRECT_PASSWORD):
    entered_password = get_input_sequence(model, len(correct_password))
    if entered_password is not None:
        check_password(entered_password, correct_password)

def load_trained_model(model_path):
    try:
        return keras.models.load_model(model_path)
    except Exception as e:
        print(f"모델 로드 에러: {e}")
        return None

def main():
    try:
        model = keras.models.load_model('./my_first_DNN_model.keras')
        # model.summary() # 모델 구조 확인이 필요하면 주석 해제
        login(model)
    except Exception as e:
        print(f"모델을 불러오는 데 실패했습니다: {e}")
        print("my_first_DNN_model.keras 파일이 현재 디렉토리에 있는지 확인하세요.")


if __name__ == '__main__':
    main()

def signup():
    pass