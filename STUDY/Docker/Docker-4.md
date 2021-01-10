# Docker-4.md

## 컨테이너 실행하기  

도커를 실행하는 명령입니다. container는 생략 가능합니다.

### 컨테이너 실행
`docker container run [option] [image:tag] [command]`<br/>
`docker run [option] [image:tag] [command]`

| Option  | Description |
| ------- | -------- |
| --name | 컨테이너 이름 부여 |
| -d, ---detach | detach mode, 백그라우드에서 실행한다|
| -p [Host Port:Container Port], ---publish | Port forwarding, 호스트와 컨테이너의 포트를 연결 |
| -e | 환경변수 설정 |
| -rm | 컨테이너 종료시 컨테이너 자동 삭제 |
| -it | 콘솔에 결과를 출력하는 옵션, -i -> 컨테이너 표준출력을 연다 -t -> tty(디바이스)를 확보한다 |


`docker run [image]` 라는 명령어는 이미지를 다운받고`docker pull [image]` 컨테이너를 생성하고`docker container create` 컨테이너를 실행하는`docker container start` 3가지 명령어를 동시에 처리할 수 있습니다. 이미지가 이미 존재한다면 다운로드`pull`하지 않습니다. 
![docker_run](https://user-images.githubusercontent.com/76420201/104117172-9795a800-5362-11eb-907a-9e471f31c88b.GIF)

이미지 이름 뒤에 tag를 붙이지 않으면 자동으로 latest버전을 다운로드 하게 됩니다.
`docker run ubuntu` = `docker run ubuntu:latest` 하지만 특정한 버전을 다운로드 하고 싶을때는 tag를 원하는 버전에 맞추어 입력해야 합니다. ex) `docker run ubuntu:16.04`


### 컨테이너 리스트

`docker container ls`<br/>
`docker ps`

`docker run`명령어를 입력하면 컨테이너 생성되고 실행됩니다. `docker ps`명령어를 통해서 현재 가동중인 컨테이너 목록을 확인할 수 있습니다. `docker ps -a`와 같이 `-a`옵션을 부여하게 되면 실행 중/정지 중인 모든 컨테이너를 표시합니다.

![docker_ps_a](https://user-images.githubusercontent.com/76420201/104118439-86519900-536c-11eb-8412-40aaa86f368c.GIF)

이와 같이 하나의 이미지로 여러개의 컨테이너를 실행할 수 있습니다. 주의해야 할 점은 서로 다른이름을 부여해줘야 한다는 것입니다. 이름이 중복되면 에러메세지가 출력됩니다.

### 컨테이너 삭제 
`docker container rm [Container ID]`
`docker rm [Container ID]`

정지 상태인 컨테이너를 삭제할 때 `docker rm [Container ID]`명령어를 입력하시면 됩니다. [Container ID]입력 하실때  ID 전체를 쓰지 않아도 구분할 수 있을정도만 써주시면 됩니다. 실행중인 컨테이너는 삭제되지 않습니다. 또한, 정지 중인 모든 컨테이너를 삭제하려면 `docker container prune`명령어를 입력하시면 됩니다.
