import requests
import sys
import json
import re

# 사용법 안내 (ENDPOINT 입력 확인)
# if len(sys.argv) != 2:
#     print("사용법: python script.py <ENDPOINT>")
#     print("예: python script.py \"https://us-south.ml.cloud.ibm.com/ml/v4/deployments/<deployment_id>/ai_service_stream?version=2021-05-01\"")
#     sys.exit(1)

# 입력 변수로 ENDPOINT 설정
# ENDPOINT = sys.argv[1]
ENDPOINT = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/edff89c5-9c4b-4d6b-baad-5510bb3de112/ai_service_stream?version=2021-05-01"

# API 키 설정 (IBM Cloud에서 발급받은 API 키로 대체)
API_KEY = "nWZEsxTOIpYZbvKx9aPJzTBHo8ojvPG1zG82X3tnnHB8"

# IAM 토큰 요청
try:
    token_response = requests.post(
        'https://iam.cloud.ibm.com/identity/token',
        data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
    )
    token_response.raise_for_status()  # HTTP 에러 발생 시 예외 발생
    mltoken = token_response.json()["access_token"]
except requests.exceptions.RequestException as e:
    print(f"액세스 토큰 획득 실패: {e}")
    sys.exit(1)
except (KeyError, ValueError) as e:
    print(f"액세스 토큰 파싱 실패: {e}")
    sys.exit(1)

# 요청 헤더 설정
header = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + mltoken
}

# 요청 데이터
payload_scoring = {
    "messages": [{"content": "what is gen AI", "role": "user"}]  # role을 user로 수정
}

# API 호출 및 스트리밍 응답 처리
print("Scoring response")
try:
    with requests.post(ENDPOINT, json=payload_scoring, headers=header, stream=True) as response_scoring:
        response_scoring.raise_for_status()  # HTTP 에러 발생 시 예외 발생
        for line in response_scoring.iter_lines(decode_unicode=True):
            if line:  # 빈 줄 무시
                # "data: {...}" 형식에서 JSON 데이터 추출
                match = re.match(r'^data:[ \t]*(.*)$', line)
                if match:
                    json_data = match.group(1)
                    try:
                        # JSON 파싱
                        parsed_data = json.loads(json_data)
                        # choices의 delta에서 content 추출
                        if "choices" in parsed_data:
                            for choice in parsed_data["choices"]:
                                delta = choice.get("delta", {})
                                if "content" in delta:
                                    print(delta["content"])
                    except json.JSONDecodeError as e:
                        print(f"JSON 파싱 오류: {json_data}")
                    except Exception as e:
                        print(f"예상치 못한 오류: {e}")
except requests.exceptions.RequestException as e:
    print(f"API 호출 실패: {e}")
except Exception as e:
    print(f"예상치 못한 오류: {e}")
