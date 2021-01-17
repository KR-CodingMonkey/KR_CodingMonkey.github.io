# Dockerfile 명령어

`docker build -t [image:tag] .`<br/>
- `docker build`를 하게되면 현재 디렉토리안에 있는 Dockerfile 내용을 바탕으로 이미지가 생성된다.
- [image:tag] tag명을 붙이지 않으면 자동으로 latest
- 마지막에 점(.)은 Dockerfile의 경로를 지정한다. 파일 이름이 Dockerfile이 아닌 경우 --file(또는 -f) 옵션을 사용해서 파일 이름을 지정한다.

|명령어|용도|
|------|----|
|FROM	|base 이미지 설정|
|WORKDIR	|작업 디렉터리 설정|
|RUN	|이미지 빌드 시 커맨드 실행|
|ENTRYPOINT	|이미지 실행 시 항상 실행되야 하는 커맨드 설정|
|CMD	|이미지 실행 시 디폴트 커맨드 또는 파라미터 설정|
|EXPOSE	|컨테이너가 리스닝할 포트 및 프로토콜 설정|
|COPY/ADD	|이미지의 파일 시스템으로 파일 또는 디렉터리 복사|
|ENV	|환경 변수 설정|
|ARG	|빌드 시 넘어올 수 있는 인자 설정|


[Dockerfile 명령어 정리](https://www.daleseo.com/dockerfile/) 여기 잘 나와 있네요.