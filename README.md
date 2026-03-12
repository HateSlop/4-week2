# hateslop 4기 실습 · Week 2

hateslop 4기 실습 2주차 폴더입니다.

## 개요

- 실습용 저장소 (Python, API 연동 등)
- `API/`: OpenAI 등 외부 API 호출 예제
- `GITHUB/`: GitHub 사용·기여 관련 문서
- `ASSIGNMENT/`: 주차별 과제 제출 및 안내

## 저장소 구조

```
week2/
├── .gitignore
├── README.md           # 프로젝트 개요
├── requirements.txt    # Python 의존성
├── API/                # API 연동 모듈
│   ├── README.md
│   └── api_call.py
├── GITHUB/             # GitHub 관련 문서
│   └── README.md
└── ASSIGNMENT/         # 주차별 과제
    └── README.MD       # 과제 상세 안내
```

## 시작하기

### 환경 설정

1. 가상환경 생성 및 활성화  
   `python -m venv .venv` 후 `.venv/bin/activate` (Windows는 `.venv\Scripts\activate`)

2. 의존성 설치  
   `pip install -r requirements.txt`

3. 환경 변수 설정  
   프로젝트 루트에 `.env` 파일을 만들고 필요한 키 설정 (예: `OPENAI_API_KEY`).  
   실제 키는 `.env`에만 두고 커밋하지 마세요.

### 실행

- OpenAI 연동 예제: `API/` 폴더의 `api_call.py` 참고 및 해당 디렉터리에서 실행  
- 상세 API 사용법은 `API/README.md`를 참고하세요.

## 과제 (Assignment)

이번 주차 과제는 API 키 관리와 PR 요청 실습입니다. 상세한 내용은 아래 문서를 참고하여 진행해 주세요.
- [과제 상세 안내 및 제출 방법](./ASSIGNMENT/README.MD)

## 문서

- [API 모듈 설명 및 사용법](./API/README.md)
- [GitHub 사용 및 기여 안내](./GITHUB/README.md)
- [주차별 과제 안내](./ASSIGNMENT/README.MD)

## 라이선스 및 기여

저장소 라이선스와 기여 방법은 `GITHUB/README.md`를 참고해 주세요.
