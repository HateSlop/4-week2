# API 모듈

OpenAI 연동 예제를 담당하는 모듈입니다.

## 구성

| 파일 | 설명 |
|------|------|
| `api_call.py` | OpenAI **Responses API** 호출 예제. `gpt-4o-mini`로 입력 문자열에 대한 응답을 받아 `response.output_text`를 출력합니다. |

## 환경 변수

`.env` 파일에 다음을 설정하세요.

- `OPENAI_API_KEY`=OpenAI API 키 (필수)

## api_call.py 동작

- `python-dotenv`로 `.env`를 로드하고, `os.getenv("OPENAI_API_KEY")`로 클라이언트 생성
- `client.responses.create(model="gpt-4o-mini", input="...")` 호출
- `response.output_text`와 `response` 객체를 출력

**실행**: 프로젝트 루트에서 `python API/api_call.py` 또는 `API` 디렉터리에서 `python api_call.py`

## 의존성

- `openai`
- `python-dotenv`

프로젝트 루트의 `requirements.txt`에 포함되어 있습니다.
