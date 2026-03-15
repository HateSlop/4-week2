from pathlib import Path
def load_env(env_path: Path) -> dict:
    env_vars = {}

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()

        if not line or line.startswith("#"):
            continue

        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        env_vars[key.strip()] = value.strip().strip('"').strip("'")

    return env_vars


def mask_value(value: str) -> str:
    if not value:
        return "(empty)"
    if len(value) <= 8:
        return "*" * len(value)
    return f"{value[:4]}...{value[-4:]}"


def main():
    env_path = Path(__file__).resolve().parent / ".env"

    if not env_path.exists():
        print(".env 파일을 찾을 수 없습니다.")
        return

    env_vars = load_env(env_path)

    if not env_vars:
        print("읽을 수 있는 환경변수가 없습니다.")
        return

    print("[환경변수 출력 결과]")
    for key, value in env_vars.items():
        print(f"{key}={mask_value(value)}")


if __name__ == "__main__":
    main()
