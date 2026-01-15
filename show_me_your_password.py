import cv2
import numpy as np

def init_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("비디오 캡처 장치를 열 수 없습니다.")
        return None
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    return cap

def get_password_image(cap=None, index=0):
    """
    웹캠을 열고 'c' 키를 누르면 관심 영역(ROI)의 이미지를 캡처, 처리하여 반환합니다.
    'ESC' 키를 누르면 종료됩니다.
    cap 인자가 주어지면 해당 비디오 캡처 객체를 사용합니다.
    index 인자는 저장될 파일명의 접미사로 사용됩니다.
    """
    own_cap = False
    if cap is None:
        cap = init_webcam()
        own_cap = True
        if cap is None: return None

    captured_image = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 가져 올 수 없습니다.")
            break
        
        # 원본 프레임을 좌우 반전
        frame = cv2.flip(frame, 1)
        display_frame = frame.copy()

        height, width, _ = display_frame.shape
        center_x, center_y = width // 2, height // 2
        
        # ROI 설정
        roi_start_y, roi_end_y = center_y - 84, center_y + 84
        roi_start_x, roi_end_x = center_x - 84, center_x + 84
        
        # ROI 영역에 사각형 그리기
        cv2.rectangle(display_frame, (roi_start_x, roi_start_y), (roi_end_x, roi_end_y), (0, 0, 255), 2)
        cv2.imshow("Webcam - Press 'c' to capture, 'ESC' to exit", display_frame)

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
            #dilate = cv2.dilate(otsu_thresh, kernel, iterations=1)
            #erosion = cv2.erode(otsu_thresh, kernel, iterations=1)
                        
            # 최종적으로 반환할 이미지 (MNIST와 유사한 형태: 흰색 숫자, 검은색 배경)
            # bitwise_not을 적용하여 배경을 검게, 숫자를 희게 만듭니다.
            # final_image = cv2.bitwise_not(dilate)
            # otsu_thresh 자체가 이미 반전된 상태이므로 추가 반전 불필요
            
            #captured_image = cv2.flip(erosion, 1)  # 좌우 반전 적용
            captured_image = otsu_thresh

            #원본화상을 찍기 변하게 하기 위해서 좌우 반전해서 읽었기 때문임
            captured_image = cv2.flip(captured_image, 1)  # 좌우 반전 적용
            
            # 바운딩 박스 계산 및 이미지 자르기
            contours, _ = cv2.findContours(captured_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                c = max(contours, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(c)
                
                padding = 20
                x = x - padding
                y = y - padding
                w = w + (padding * 2)
                h = h + (padding * 2)

                # 정사각형으로 보정
                center_x = x + w // 2
                center_y = y + h // 2
                max_side = max(w, h)
                w = max_side
                h = max_side
                x = center_x - (w // 2)
                y = center_y - (h // 2)

                # 이미지 범위 벗어나는 것 방지 (음수 인덱스 방지)
                if x < 0: x = 0
                if y < 0: y = 0
                
                # 이미지 자르기
                captured_image = captured_image[y:y+h, x:x+w]

            print("이미지가 캡처되었습니다.")
            break

        elif key == 27:  # ESC 키
            break

    if own_cap:
        cap.release()
        cv2.destroyAllWindows()
    
    if captured_image is not None:
        filename = f"captured_password_image_{index}.png"
        cv2.imwrite(filename, captured_image)
        return [filename]
    return None

if __name__ == '__main__':
    # 이 파일을 직접 실행할 경우 테스트 코드
    result = get_password_image()
    if result is not None:
        filename = result[0]
        password_img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        cv2.imshow("Final Bounded Image", password_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print(f"캡처된 이미지를 '{filename}' 파일로 저장했습니다.")
    else:
        print("이미지가 캡처되지 않았습니다.")