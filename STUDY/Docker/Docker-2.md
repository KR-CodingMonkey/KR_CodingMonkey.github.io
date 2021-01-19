# Docker 설치

Docker는 Linux 커널 기능을 사용하기 때문에 보통은 Linux 배포판 상에서 작동한다. 하지만 개발 환경에서 이용하기 위한 클라이언트 PC용 툴을 제공하고 있다. macOS용, Windows용으로도 제공 된다. 이것은 Windows 10 이후에 이용 가능하게 된 것으로, x64용 가상화 시스템인 'Hyper-V'를 사용하고 있다. Hyper-V는 Windows 10 pro, Enterprise, Education에서만 작동하고 Home 버전에서는 작동하지 않는다(Hyper-V 를 따로 설치하면 Home버전에서도 이용 가능). 또한 OS의 설정에서 Hyper-V를 유효화하면 VirtualBox 등과 같은 다른 가상화 툴은 사용할 수 없으므로 주의해야 한다.

Linux에 Docker 설치하는 방법도 버전마다 다르지만, 여기서는 CentOS 7버전에서의 설치 방법에 대해서 서술할 것이다.
<br/>


## 사전 준비
- Root 계정 변경
```
su -
```
![1](https://user-images.githubusercontent.com/76420201/104091810-3f5b9900-52c3-11eb-89fc-39671df5ba65.GIF)

- SELinux 설정
```
setenforce 0
sestatus
sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
```
![2](https://user-images.githubusercontent.com/76420201/104091826-57cbb380-52c3-11eb-87ec-b5c57bcea286.GIF)


- 방화벽 해제
```
systemctl stop firewalld && systemctl disable firewalld
systemctl stop NetworkManager && systemctl disable NetworkManager
```
![3](https://user-images.githubusercontent.com/76420201/104091835-61edb200-52c3-11eb-8935-6805e31d6695.GIF)

- SWAP 비활성화
```
swapoff -a && sed -i '/ swap / s/^/#/' /etc/fstab
```
![4](https://user-images.githubusercontent.com/76420201/104091841-6914c000-52c3-11eb-8a8d-f70eca34a7a6.GIF)


- Iptables 커널 옵션 활성화
```
cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
```
```
sysctl --system
```
<img src = "https://user-images.githubusercontent.com/76420201/104091846-72059180-52c3-11eb-9776-ae6de36e500b.GIF" width = "70%">


- 쿠버네티스를 위한 yum repository 설정
```
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF
```
![5 6](https://user-images.githubusercontent.com/76420201/104091963-4b942600-52c4-11eb-9392-d5e7d4bea817.GIF)


- CentOS update
```
yum update
```
<img src = "https://user-images.githubusercontent.com/76420201/104091907-e6403500-52c3-11eb-9870-9d7218e3795d.GIF" width = "70%">

![6-2](https://user-images.githubusercontent.com/76420201/104091957-459e4500-52c4-11eb-8528-4532e90734be.GIF)

<br/>

## Docker 설치 & 실행

- Docker 설치
```
yum install -y yum-utils device-mapper-persistent-data lvm2 
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum update && yum install docker-ce
```
![7-1](https://user-images.githubusercontent.com/76420201/104092313-84cd9580-52c6-11eb-830f-79d1dd680b09.GIF)
![7-2](https://user-images.githubusercontent.com/76420201/104092316-87c88600-52c6-11eb-9e35-6fdf85b7d09a.GIF)
![7-3](https://user-images.githubusercontent.com/76420201/104092321-8a2ae000-52c6-11eb-87d4-d138f0039474.GIF)

{:.m-5}
```
systemctl enable --now docker && systemctl start docker
```
>> ![8](https://user-images.githubusercontent.com/76420201/104092354-cb22f480-52c6-11eb-83b3-0c2641826632.GIF)

- Docker Compose 설치
```
curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose -version 
```
![9-1](https://user-images.githubusercontent.com/76420201/104092363-d37b2f80-52c6-11eb-8370-3edd28fe10ff.GIF)
![9-2](https://user-images.githubusercontent.com/76420201/104092365-d4ac5c80-52c6-11eb-8bfc-7e1af092ded2.GIF)


- Docker 설치 확인
```
docker run hello-world
```
<img src = "https://user-images.githubusercontent.com/76420201/104092372-df66f180-52c6-11eb-9b3b-87ea199c7f68.GIF" width = "70%">

docker run 커맨드로 'hello-world'라는 이미지를 실행시킨 결과이다다. 이와 같이 뜬다면 정상적으로 설치를 완료된 것이다.