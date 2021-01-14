# python 프로그램 배포

Windows에서 작업한 python파일을 리눅스에서 Dockerfile로 만드는 방법은 여러가지 있습니다.<br/>
저는 제가 만든 python 파일을 저의 github사이트에 올려놓고 Dockerfile안에서 `git clone`하는 방식으로 만들었습니다.

이 방식의 장점은 python파일을 수정했을때 다시 build를 하고 새로운 이미지를 배포하지 않아도 된다는 겁니다.<br/>

다른방법으로는 리눅스 자체에 `git clone`으로 파일을 다운로드한 후 `copy`라는 커멘드로 Dockerfile에 복사하셔도 됩니다.

---

## Dockerfile

```linux
# Dockerfile 생성
touch Dockerfile

# Dockerfile 작성
vi Dockerfile
```

```Dockerfile
# Base Image 73MB
FROM centos:centos7

# Change working Dir
RUN mkdir /app/
WORKDIR /app/

# To use python & git clone
RUN yum install -y python3
RUN yum install -y git

# Clone
RUN pip3 install pymysql
RUN git clone https://github.com/KR-CodingMonkey/e_commerce_app.git /app/

# Set ENV
ENV  PYTHONIOENCODING=UTF-8
CMD ["python3", "e_commerce_app_linux.py"]
```

윈도우 환경에서 작성한 Python파일을 깃허브에 업로드 해놓고 Linux에서 Dockerfile을 생성 했습니다.<br/>
`ENV PYTHONIOENCODING=UTF-8` 이 코드는 Linux에 설치된 Python환경에서 한국어가 깨짐을 방지한 것입니다.

---

도커파일 빌드를 해봅시다.
```
docker build -t myapp_test:0.1 .
```

<img src="https://user-images.githubusercontent.com/76420201/104558559-59f88e00-5686-11eb-8051-e8de728c7673.GIF" width="70%"><br/>
이미지가 정상적으로 생성이 되었으니 실행해봅시다. 

```
docker run -it --rm myapp_test:0.1
```

`docker run` 시 주의해야 할점은 `-it` 옵션을 꼭 붙여줘야 합니다!!

