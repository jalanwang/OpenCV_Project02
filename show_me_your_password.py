import cv2
import numpy as np
import tkinter as tk

def get_password_image():
    """
    웹캠을 열고 'c' 키를 누르면 관심 영역(ROI)의 이미지를 캡처, 처리하여 반환합니다.
    'ESC' 키를 누르면 종료됩니다.
    """
    # 화면 해상도 얻기
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("비디오 캡처 장치를 열 수 없습니다.")
        return None

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

    window_name = "Webcam - Press 'c' to capture, 'ESC' to exit"
    cv2.namedWindow(window_name)
    
    # 윈도우를 화면 중앙으로 이동
    x = (screen_width - frame_width) // 2
    y = (screen_height - frame_height) // 2
    cv2.moveWindow(window_name, x, y)

    captured_image = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 가져 올 수 없습니다.")
            break
                
        height, width, _ = frame.shape
        center_x, center_y = width // 2, height // 2
        
        # ROI 설정
        roi_start_y, roi_end_y = center_y - 70, center_y + 70
        roi_start_x, roi_end_x = center_x - 70, center_x + 70
        
        # ROI 영역에 사각형 그리기
        cv2.rectangle(frame, (roi_start_x, roi_start_y), (roi_end_x, roi_end_y), (0, 0, 255), 2)
        cv2.imshow(window_name, frame)

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
            
            # 이미지 가장자리를 14픽셀씩 잘라냅니다.
            h, w = dilate.shape[:2]
            cropped_img = dilate[14:h-14, 14:w-14]

            captured_image = cropped_img
            
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
        # 이미지 가장자리를 14픽셀씩 잘라냅니다.
        h, w = password_img.shape[:2]
        cropped_img = password_img[14:h-14, 14:w-14]
        
        cv2.imwrite("captured_password_image.png", cropped_img)
        print("캡처된 이미지를 'captured_password_image.png' 파일로 저장했습니다.")
    else:
        print("이미지가 캡처되지 않았습니다.")