---
sort: 6 
---


# TroubleShooting

## Linux Python 한글 깨짐

python 2.x 버전에서 많이 일어나는 문제인데 python3 를 설치했음에도 한글 깨짐이 발생했다.

해결법은 환경변수를 설정해주면 됩니다.

Dockerfile 빌드시 `ENV PYTHONIOENCODING=UTF-8`을 추가해주거나 추가하지 않고 이미지를 생성했다면
`docker run` 명령어를 실행할때 `-e PYTHONIOENCODING=UTF-8` 옵션을 부여하면 해결됩니다.

---

## DB데이터 commit 데이터 사라짐

---
## Linux msvcrt.getch() 모듈 지원안함

---
## docker run -it 옵션