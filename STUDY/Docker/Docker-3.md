# Docker-3

![docker_version](https://user-images.githubusercontent.com/76420201/104095250-38d81c00-52d9-11eb-8a97-c52fbc07c4a0.GIF){: width = "50%" height = "50%"}

## Docker Image

### 이미지 검색
`docker search [image]`
### 이미지 다운로드
`docker pull [image:tag]`

컨테이너를 실행하기 위해서는 [Docker hub](https://hub.docker.com/) 사이트에서 이미지를 검색 또는 콘솔에서 `docker search [image]`입력하고 버전을 확인 후 `docker pull [image:tag]` 커맨드로 다운받아야 한다. 

![docker_image_search](https://user-images.githubusercontent.com/76420201/104095269-4ab9bf00-52d9-11eb-836e-c274f111eff1.GIF)
**공식 Docker 이미지는 [OFFICIAL] 이 [OK] 표시되어 있으므로 공식 이미지를 사용해 주는 것을 권장한다.**
<br/>

### 이미지 리스트
`docker image ls` `docker images`

로컬에 다운받아 놓은 이미지 목록을 보기위해서 `docker image ls` 또는 `docker images` 명령어를 사용한다.
![docker_images](https://user-images.githubusercontent.com/76420201/104117522-3f13da00-5365-11eb-9b06-96aa3b2da7e0.GIF)

### 이미지 삭제 
`docker image rm [IMAGE ID]` `docker rmi [IMAGE ID]`

이미지를 삭제하려면 `docker images`로 해당 이미지의 ID를 확인하고 `docker rmi [Image ID]`명령을 실행하면 된다.
![docker_rmi](https://user-images.githubusercontent.com/76420201/104117663-5dc6a080-5366-11eb-8bc4-4898c3ca9155.GIF)

