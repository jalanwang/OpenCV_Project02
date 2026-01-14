import cv2
import numpy as np

# VideoCapture 객체를 'cap'으로 변경
cap = cv2.VideoCapture(0)

# 웹캠 성능 향상을 위해 해상도를 640x480으로 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 비디오 스트리밍 포맷을 MJPEG로 설정
# 참고: 모든 웹캠이 이 설정을 지원하지는 않을 수 있습니다.
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


while True:
    # cap.read()의 결과를 ret, frame으로 받음
    ret, frame = cap.read()
    if not ret:
        print("프레임을 가져 올 수 없습니다.")
        break
    
    # 원본 프레임을 좌우 반전
    flip_frame = frame #cv2.flip(frame, 1)

    height, width, _ = flip_frame.shape
    center_x = width // 2
    center_y = height // 2
    
    # 관심 영역(ROI) 설정
    roi_start_y = center_y - 150
    roi_end_y = center_y + 150
    roi_start_x = center_x - 150
    roi_end_x = center_x + 150
    roi = flip_frame[roi_start_y:roi_end_y, roi_start_x:roi_end_x]

    # 관심 영역에 사각형 그리기
    cv2.rectangle(flip_frame, (roi_start_x, roi_start_y), (roi_end_x, roi_end_y), (0, 0, 255), 2)
    cv2.imshow("Webcam", flip_frame)

    # 키 입력을 한 번만 받도록 수정
    key = cv2.waitKey(1) & 0xFF

    # 'c' 또는 'C' 키를 눌렀을 때
    if key == ord('c') or key == ord('C'):
        # ROI를 그레이스케일로 변환
        gray_image = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        
        # gray_image는 이미 좌우 반전된 flip_frame에서 왔으므로 추가 반전이 필요 없음
        # gray_image = np.flip(gray_image, 1) 
        
        cv2.imwrite("gray_image.png", gray_image)
        
        # 가우시안 블러 처리
        gaussian_blur = cv2.GaussianBlur(gray_image, (5, 5), 0)
        
        # 오츠 이진화 처리
        _, otsu_thresh = cv2.threshold(gaussian_blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        #여기서 흑백 반전 처리했다.
        cv2.imwrite("otsu_image.png", otsu_thresh)
        cv2.imshow("Otsu Image", otsu_thresh)
        
        #### Morphological Transformations ####
        # 커널 생성
        kernel = np.ones((5, 5), np.uint8)
        dilate=cv2.dilate(otsu_thresh, kernel, iterations=1) # 확장. 가는 글씨를 크게함. 반복 횟수가 커질수록 굵어짐
        
        #바탕이 검은 색
        cv2.imshow("Dilation Image", dilate)
        cv2.imwrite("digit_binary_image.png", dilate)

        #이미지 자르기
        img=cv2.imread("digit_binary_image.png", cv2.IMREAD_UNCHANGED)
        h,w=img.shape[:2]
        crop_size=280
        ccx, cy= w//2, h//2
        half=crop_size//2
        x1, x2= ccx-half, ccx+half
        y1, y2= cy-half, cy+half
        # 경계면 설정
        x1= max(0, x1)
        y1= max(0, y1)
        x2= min(w, x2)
        y2= min(h, y2)

        cropped_img= img[y1:y2, x1:x2]

        cv2.imshow("Cropped Image", cropped_img)        
        reversed_img=cv2.bitwise_not(cropped_img)

        cv2.imwrite("IMAGE_FOR_TEST.png", reversed_img)

    # ESC 키(ASCII 27)를 눌렀을 때 종료
    if key == 27:  
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()