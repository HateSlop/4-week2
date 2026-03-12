# GitHub 실습 · Fork → PR → Merge

메인 레포를 포크한 뒤, **본인 이름 폴더**를 만들고 Push → Pull Request → Merge까지 진행하는 실습입니다.

## 실습 순서

### 1. 메인 레포 포크

- GitHub에서 **메인(원본) 저장소** 페이지로 이동
- 우측 상단 **Fork** 버튼 클릭 → 본인 계정에 포크된 레포가 생성됨

### 2. 포크한 레포 클론

```bash
git clone https://github.com/<본인-계정>/<저장소명>.git
cd week2
```

> 메인 레포 URL이 아니라 **본인이 포크한 레포 URL**을 사용하세요.

### 3. 본인 이름으로 폴더 만들기

- 저장소 루트에 **본인 이름(또는 닉네임) 폴더** 생성  
  예: `GITHUB/홍길동/`, `GITHUB/kim-dev/` 등
- 폴더 안에 파일을 넣어도 되고, 빈 폴더만 만들어도 됨 (실습 목적은 Push·PR·Merge 확인)

```bash
mkdir -p GITHUB/<본인이름>
# 필요하면 파일 추가 후
git add GITHUB/<본인이름>
git commit -m "Add folder: <본인이름>"
```

### 4. 포크한 레포에 Push

```bash
git push origin main
```

(기본 브랜치가 `main`이 아닌 경우 해당 브랜치 이름으로 push)

### 5. 메인 레포로 Pull Request 보내기

- GitHub에서 **본인 포크 레포** 페이지로 이동
- **Compare & pull request** 버튼이 보이면 클릭 (또는 Pull requests → New pull request)
- **base: 메인레포/main** ← **compare: 본인포크/main** 인지 확인
- 제목·설명 작성 후 **Create pull request**

### 6. Merge 확인

- 메인 레포 관리자가 PR을 **Merge**하면, 메인 레포에 본인 이름 폴더가 반영됨
- 메인 레포에서 해당 PR이 Merge된 것과, 본인 폴더가 보이는지 확인하면 실습 완료

## 정리

| 단계 | 하는 일 |
|------|--------|
| 1 | 메인 레포 **Fork** |
| 2 | 포크한 레포 **Clone** |
| 3 | **본인 이름 폴더** 생성 후 commit |
| 4 | 포크 레포에 **Push** |
| 5 | 메인 레포로 **Pull Request** 생성 |
| 6 | 관리자 **Merge** 후 메인 레포에서 반영 확인 |

## 유의사항

- **API 키·비밀**: `.env` 등 API 키는 절대 커밋하지 마세요.
- PR 전에 메인 레포의 최신 `main`을 pull 받아서 conflict 없이 올리면 좋습니다.

## 문서

- 프로젝트 개요: 루트 [README.md](../README.md)
- API 모듈: [API/README.md](../API/README.md)
