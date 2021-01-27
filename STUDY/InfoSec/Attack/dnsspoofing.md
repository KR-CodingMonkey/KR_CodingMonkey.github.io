
# DNS Spoofing

DNS(Domain Name Server) spoofing(DNS cache Spoofing 이라고도 함)은 DNS 서버로 보내는 질문을 가로채서 변조된 결과를 보내주는 것으로 일종의 중간자 공격이다.

![DNS-spoofing](https://user-images.githubusercontent.com/76420201/105853028-93d37800-6028-11eb-9b62-5bfb607fb803.jpg)

- 중간자 공격 MITM(Man in the middle) : 사용자를 다른 or 악의적인 IP주소로 라우팅하기 위해 사용자와 DNS서버간의 통신을 가로채는 것

- DNS 서버 손상 : DNS서버를 손상시켜 악의적인 IP주소를 반환하도록 함

<br>

## DNS Spoofing 공격 원리

1. 사용자의 컴퓨터는 보통 컴퓨터가 사용하는 IP 주소대신 사람들이 쓰기 편한 문자로 구성되어 있는 URL주소를 사용한다. 하지만 컴퓨터는 URL주소를 바로 인식할 수 없기 때문에, 사용자로부터 URL주소를 입력을 받으면 등록된 도메인 네임 시스템의 주소로 UDP프로토콜을 이용하여 질의를 보낸다.

2. 이때 중간자 공격을 받고 있는 경우에는 사용자의 컴퓨터가 보내는 질의의 내용을 수정하여 도메인 네임 시스템서버에 전송하고, 도메인 네임 시스템서버는 변경된 질의에 대한 답을 사용자의 컴퓨터로 보내고, 사용자의 컴퓨터는 질의에 나와 있는 IP 주소를 이용하여 접속을 하게 된다. 이때 이미 질의가 중간자 공격으로 인해 원래의 값이 아니기 때문에 의도치 않은 곳으로 접속될 수 있다.

<br>

## DNS Spoofing 공격 순서

**Step 1. WinXP에서 DNS 캐시 테이블을 확인**

`ipconfig /flushdns` : dns 테이플 초기화<br>
`ipconfig /displaydns` : dns 테이블 조회

<center><img src = "https://user-images.githubusercontent.com/76420201/105919614-52b78400-6079-11eb-9974-caed91c4035c.jpg" width = "70%"></center>

winXP에서 `ping google.com` google.com에 핑을 찍어보고 DNS 캐시테이블을 확인해보면 google.com IP 주소를 정상적으로 받아와서 DNS 캐시 테이블에 반영합니다.

---

**Step 2. Attacker 가상머신 -> ettercap에서 사용할 변조 DNS정보를 설정**

ettercap : 중간자 공격(Man in the Middle)을 쉽게 할 수 있도록 만들어진 프로그램

`vi /etc/ettercap/etter.dns` 파일 수정

![DNS-spoofing1](https://user-images.githubusercontent.com/76420201/105856995-2e35ba80-602d-11eb-8ac7-d121302e2b13.jpg)


www.google.com 의 주소를 공격자(Attacker)의 IP인 192.168.126.130으로 설정해줍니다.

---

**Step 3. Attacker 가상머신에서 아파치를 실행 후 브라우저를 통해 확인**

`sudo service apache2 start`<br>
`sudo service apache2 status`

![DNS-spoofing3](https://user-images.githubusercontent.com/76420201/105858772-0c3d3780-602f-11eb-8752-609bd0292fa6.jpg)

![DNS-spoofing2](https://user-images.githubusercontent.com/76420201/105858852-2414bb80-602f-11eb-9d6e-6ccf99c7c2cb.jpg)

Attacker 가상머신에서 희생자 DNS 서버를 조작해 변조된 결과를 보여주기 위한 사전 작업을 합니다.

---

**Step 4. Attacker 가상머신에서 ettercap 실행**

- Attacker 가상머신에서 ettercap을 실행해줍니다. `sudo ettercap -G`
![ettercap1](https://user-images.githubusercontent.com/76420201/105920373-98288100-607a-11eb-9bf0-ea8aaee2c905.GIF)

- 툴을 실행시키면 화면이 나오는데, 기본 설정을 확인하고 Accept 버튼 클릭
<center><img src = "https://user-images.githubusercontent.com/76420201/105920375-9959ae00-607a-11eb-8181-f988e1e8db72.GIF" width = "70%"></center>


- Scan for hosts 버튼을 클릭 ⇒ 로컬 네트워크 상에 존재하는 호스트를 검색
<center><img src = "https://user-images.githubusercontent.com/76420201/105924194-2acc1e80-6081-11eb-8f30-4bd03f330bf5.GIF" width = "70%"></center>

- Hosts List 버튼을 클릭 ⇒ 중간자로 끼어들 위치를 지정 

    게이트웨이 선택 -> Add to Target1 클릭 -> 희생자(Windows XP) 선택 -> Add to Target2 클릭

<center><img src = "https://user-images.githubusercontent.com/76420201/105924171-20aa2000-6081-11eb-9131-b1018d8d60fd.GIF"></center>

---

- MITM 메뉴 클릭 > ARP poisoning 메뉴 클릭 ⇒ 게이트웨이와 희생자의 MAC 주소를 공격자의 MAC 주소로 변조 ⇒ MITM 공격
ettercap에서 사용할 변조 DNS 정보를 설정
<center><img src = "https://user-images.githubusercontent.com/76420201/105932104-b3ea5200-608f-11eb-9a67-d8929e0bcac1.GIF" width = "70%"></center>

---

**Step 5. WinXP 가상머신에서 ARP 테이블을 확인**

<center><img src = "https://user-images.githubusercontent.com/76420201/106008896-204e6b00-60fb-11eb-8931-6a666a2377ff.GIF" width = "70%"></center>

---

**Step 6. Attacker 가상머신에서 DNS Spoofing을 실행**

<center><img src = "https://user-images.githubusercontent.com/76420201/105933307-8900fd80-6091-11eb-8740-a6906367a4da.GIF" width = "70%"></center>

![ettercap7](https://user-images.githubusercontent.com/76420201/106009036-4411b100-60fb-11eb-91fd-e7e5fca9dd09.GIF)

희생자가 DNS 서비스 요청을 하면, 공격자의 etter.dns 파일에 있는 정보를 기반으로 잘못된 DNS 정보를 반환하게 된다.

---

**Step 7. WinXP 가상머신에서 구글 접속 및 DNS 캐시 테이블 확인**

![ettercapx](https://user-images.githubusercontent.com/76420201/106010288-9bfce780-60fc-11eb-9998-d6f9d2ce888d.GIF)

![ettercap9](https://user-images.githubusercontent.com/76420201/106010283-9acbba80-60fc-11eb-9f21-58e2cb6d9bb2.GIF)
