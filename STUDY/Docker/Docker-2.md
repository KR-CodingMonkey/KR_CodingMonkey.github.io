# Docker-2

## Docker 설치

Docker는 Linux 커널 기능을 사용하기 때문에 보통은 Linux 배포판 상에서 작동합니다. 하지만 개발 환경에서 이용하기 위한 클라이언트 PC용 툴을 제공하고 있습니다. macOS용, Windows용으로도 제공 됩니다. 이것은 Windows 10 이후에 이용 가능하게 된 것으로, x64용 가상화 시스템인 'Hyper-V'를 사용하고 있습니다. Hyper-V는 Windows 10 pro, Enterprise, Education에서만 작동하고 Home 버전에서는 작동하지 않습니다(Hyper-V 를 따로 설치하면 Home버전에서도 이용 가능). 또한 OS의 설정에서 Hyper-V를 유효화하면 VirtualBox 등과 같은 다른 가상화 툴은 사용할 수 없으므로 주의해야 합니다.

Linux에 Docker 설치하는 방법도 버전마다 다르지만, 여기서는 CentOS에서의 설치 방법에 대해서 다루겠습니다.


## 사전 준비
- Root 계정 변경
```
su -
```

- SELinux 설정
```
setenforce 0
sestatus
sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
```

- 방화벽 해제
```
systemctl stop firewalld && systemctl disable firewalld
systemctl stop NetworkManager && systemctl disable NetworkManager
```

- SWAP 비활성화
```
swapoff -a && sed -i '/ swap / s/^/#/' /etc/fstab
```

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

- CentOS update
```
yum update
```

- Host 파일 수정
```
vi /etc/hosts
192.168.56.10 ansible-server
192.168.56.11 jenkins-server
192.168.56.12 tomcat-server
192.168.56.13 docker-server

ping jenkins-server 
```

## Docker 설치, 실행

- Docker 설치

```
yum install -y yum-utils device-mapper-persistent-data lvm2 
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum update && yum install docker-ce
useradd dockeradmin

passwd dockeradmin <-- password: dockeradmin
usermod -aG docker dockeradmin
systemctl enable --now docker && systemctl start docker
```

- Docker Compose 설치
```
curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose -version 
```

- Docker 설치 확인
```
docker run hello-world
```
