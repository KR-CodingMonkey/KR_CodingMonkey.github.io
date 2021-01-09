# Docker-3

## 컨테이너 실행하기 

도커를 실행하는 명령입니다.
'docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]'

자주 사용하는 옵션입니다.
| Option  | Description  |
| ------- | -------- |
| --name | 컨테이너 이름 부여 |
| -d, --detach | detach mode, 백그라우드에서 실행한다|
| -p[호스트 포트번호:컨테이너 번호] 포트, --publish | port forwarding, 호스트와 컨테이너의 포트를 연결 |
| -e | 환경변수 설정 |
| -rm | 컨테이너 종료시 컨테이너 자동 삭제 |
| -it | 콘솔에 결과를 출력하는 옵션, -i -> 컨테이너 표준출력을 연다 -t -> tty를 확보한다 |
