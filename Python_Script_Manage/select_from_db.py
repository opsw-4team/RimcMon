import requests

def get_user_data():
    url = "http://opsw4.dothome.co.kr/select_from_user_data.php" # PHP API URL

    try:
        # GET 요청 보내기
        response = requests.get(url)
        
        # 응답 상태 확인
        if response.status_code == 200:
            # JSON 데이터 파싱
            data = response.json()
        else:
            print(f"요청 실패: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")

    return data
