import cv2
import numpy as np

def get_password_image():
    """
    웹캠을 열고 'c' 키를 누르면 관심 영역(ROI)의 이미지를 캡처, 처리하여 반환합니다.
    'ESC' 키를 누르면 종료됩니다.
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("비디오 캡처 장치를 열 수 없습니다.")
        return None

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

    captured_image = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 가져 올 수 없습니다.")
            break
                
        height, width, _ = frame.shape
        center_x, center_y = width // 2, height // 2
        
        # ROI 설정
        roi_start_y, roi_end_y = center_y - 140, center_y + 140
        roi_start_x, roi_end_x = center_x - 140, center_x + 140
        
        # ROI 영역에 사각형 그리기
        cv2.rectangle(frame, (roi_start_x, roi_start_y), (roi_end_x, roi_end_y), (0, 0, 255), 2)
        cv2.imshow("Webcam - Press 'c' to capture, 'ESC' to exit", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('c') or key == ord('C'):
            # ROI 추출
            roi = frame[roi_start_y:roi_end_y, roi_start_x:roi_end_x]
            
            # 이미지 처리
            gray_image = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            gaussian_blur = cv2.GaussianBlur(gray_image, (5, 5), 0)
            #_, otsu_thresh = cv2.threshold(gaussian_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            _, otsu_thresh = cv2.threshold(gaussian_blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            
            kernel = np.ones((5, 5), np.uint8)
            dilate = cv2.dilate(otsu_thresh, kernel, iterations=1)
            
            # 최종적으로 반환할 이미지 (MNIST와 유사한 형태: 흰색 숫자, 검은색 배경)
            # bitwise_not을 적용하여 배경을 검게, 숫자를 희게 만듭니다.
            # final_image = cv2.bitwise_not(dilate)
            
            captured_image = dilate
            
            cv2.imshow("Captured Image", captured_image)
            print("이미지가 캡처되었습니다. 다른 이미지를 원하면 'c'를 다시 누르세요. 'ESC' 키로 확정하고 종료합니다.")

        elif key == 27:  # ESC 키
            break

    cap.release()
    cv2.destroyAllWindows()
    return captured_image

if __name__ == '__main__':
    # 이 파일을 직접 실행할 경우 테스트 코드
    password_img = get_password_image()
    if password_img is not None:
        cv2.imwrite("captured_password_image.png", password_img)
        print("캡처된 이미지를 'captured_password_image.png' 파일로 저장했습니다.")
    else:
        print("이미지가 캡처되지 않았습니다.")