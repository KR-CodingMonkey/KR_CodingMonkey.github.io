# Docker-3

![docker_version](https://user-images.githubusercontent.com/76420201/104095250-38d81c00-52d9-11eb-8a97-c52fbc07c4a0.GIF)

## 컨테이너 실행하기 
도커를 실행하는 명령입니다.

`docker run [option] IMAGE[:tag] [command]`

자주 사용하는 옵션입니다.

| Option  | Description |
| ------- | -------- |
| --name | 컨테이너 이름 부여 |
| -d, ---detach | detach mode, 백그라우드에서 실행한다|
| -p [Host Port:Container Port], ---publish | Port forwarding, 호스트와 컨테이너의 포트를 연결 |
| -e | 환경변수 설정 |
| -rm | 컨테이너 종료시 컨테이너 자동 삭제 |
| -it | 콘솔에 결과를 출력하는 옵션, -i -> 컨테이너 표준출력을 연다 -t -> tty(디바이스)를 확보한다 |

컨테이너를 실행하기 위해서는 [Docker hub](https://hub.docker.com/) 사이트에서 이미지를 검색 또는 콘솔에서 `docker search [image]`입력하고 버전을 확인 후 `docker pull [image:tag]` 커맨드로 다운받아야 합니다. 

![docker_image_search](https://user-images.githubusercontent.com/76420201/104095269-4ab9bf00-52d9-11eb-836e-c274f111eff1.GIF)

**공식 Docker 이미지는 [OFFICIAL] 이 [OK] 표시되어 있으므로 공식이미지를 사용해주는것을 권장해드립니다.**