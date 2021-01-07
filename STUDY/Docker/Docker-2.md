# Docker-2

## Docker 설치

Docker는 Linux 커널 기능을 사용하기 때문에 보통은 Linux 배포판 상에서 작동합니다. 하지만 개발 환경에서 이용하기 위한 클라이언트 PC용 툴을 제공하고 있습니다. macOS용, Windows용으로도 제공 됩니다. 이것은 Windows 10 이후에 이용 가능하게 된 것으로, x64용 가상화 시스템인 'Hyper-V'를 사용하고 있습니다. Hyper-V는 Windows 10 pro, Enterprise, Education에서만 작동하고 Home 버전에서는 작동하지 않습니다(Hyper-V 를 따로 설치하면 Home버전에서도 이용 가능). 또한 OS의 설정에서 Hyper-V를 유효화하면 VirtualBox 등과 같은 다른 가상화 툴은 사용할 수 없으므로 주의해야 합니다.

Linux에 Docker 설치하는 방법도 버전마다 다르지만, 여기서는 CentOS 설치 방법에 대해서 다루겠습니다.
