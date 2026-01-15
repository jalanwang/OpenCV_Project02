import sys
from login import login, load_trained_model

def main():
    # 초기 설정
    model_file = 'my_first_DNN_model.keras'
    model = load_trained_model(model_file)
    if model is None:
        print(f"기본 모델({model_file})을 찾을 수 없습니다. 1번 메뉴에서 모델을 로드해주세요.")
    
    target_password = [6] # 팩토리 디폴트

    while True:
        print("\n" + "="*30)
        print(f'1: 로드할 학습 데이타 이름: (기본값: {model_file})')
        print(f'2: 패스워드 변경 (현재: {target_password}')
        print("3: login 프로세스 진행")
        print("0: 종료")
        print("="*30)
        
        user_input = input("메뉴를 선택하세요: ").strip() # 공백 제거

        if user_input == '1':
            filename = input(f"학습 데이터 파일 이름 (기본값: {model_file}): ")
            if not filename.strip():
                filename = model_file
            
            loaded_model = load_trained_model(filename)
            if loaded_model:
                model = loaded_model
                model_file = filename
                print(f"모델 '{model_file}' 로드 완료.")
            else:
                print("모델 로드 실패. 기존 모델을 유지합니다.")

        elif user_input == '2':
            pw_input = input(f"설정할 패스워드를 공백으로 구분하여 입력하세요 \
                             \n (예: 1 2 3 4). 현재 패스워드: {target_password} ")
            try:
                temp_password = [int(x) for x in pw_input.split()]
                if not temp_password:
                    raise ValueError
                target_password = temp_password
                print(f"패스워드가 설정되었습니다: {target_password}")
            except ValueError:
                print("잘못된 입력입니다. 숫자를 공백으로 구분해서 입력해주세요.")

        elif user_input == '3':
            if model:
                print(f"로그인 프로세스를 시작합니다. (설정된 비밀번호: {target_password})")
                login(model, target_password)
            else:
                print("모델이 로드되지 않았습니다. 1번 메뉴를 이용해주세요.")

        elif user_input == '0':
            print("종료합니다.")
            break

if __name__ == "__main__":
    main()