# Docker-3

![docker_version](https://user-images.githubusercontent.com/76420201/104095250-38d81c00-52d9-11eb-8a97-c52fbc07c4a0.GIF){: width = "50%" height = "50%"}

## Docker run  


도커를 실행하는 명령입니다. container는 생략 가능합니다.
`docker container run [[option] IMAGE[:tag] [command]`

`docker run [option] IMAGE[:tag] [command]`

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

**공식 Docker 이미지는 [OFFICIAL] 이 [OK] 표시되어 있으므로 공식 이미지를 사용해 주는 것을 권장해드립니다.**


`docker run [image]` 라는 명령어는 이미지를 다운받고`docker pull [image]` 컨테이너를 생성하고`docker container create` 컨테이너를 실행하는`docker container start` 3가지 명령어를 동시에 처리할 수 있습니다. 이미지가 이미 존재한다면 다운로드`pull`하지 않습니다. 
![docker_run](https://user-images.githubusercontent.com/76420201/104117172-9795a800-5362-11eb-907a-9e471f31c88b.GIF)

이미지 이름 뒤에 tag를 붙이지 않으면 자동으로 latest버전을 다운로드 하게 됩니다.
`docker run ubuntu` = `docker run ubuntu:latest` 하지만 특정한 버전을 다운로드 하고 싶을때는 tag를 원하는 버전에 맞추어 입력해야 하니다. `docker run ubuntu:16.04`