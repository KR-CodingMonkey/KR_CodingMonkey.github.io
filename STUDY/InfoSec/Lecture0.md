
# 용어정리


<details markdown="1">
<summary><b>Heartbleed</b></summary>

<br/>
HeartBleed란 OpenSSL 1.0.1 버전에서 발견된 매우 위험한 취약점 입니다. OpenSSL을 구성하고 있는 TLS/DTLS의 HeartBeat 확장규격에서 발견된 취약점으로, 해당 취약점을 이용하면 서버와 클라이언트 사이에 주고받는 정보들을 탈취할 수 있습니다.

[more..](https://blog.alyac.co.kr/76)

</details>

---

<details markdown="1">
<summary><b>MTBF, MTTR, MTTF</b></summary>

<br/>
**MTBF**(Mean Time Between Failure) : 평균 고장 시간 간격<br/>
**MTTR**(Mean Time To Repair) : 평균 수리 시간<br/>
**MTTF**(Mean Time to Failure) : 평균 고장시간<br/>

![Image](https://user-images.githubusercontent.com/76420201/104976336-570feb80-5a40-11eb-943f-20656fe1861c.png)

MTTR 은 평균적으로 걸리는 수리시간을 말합니다.<br/>
MTTF는 평균 고장시간으로 첫 사용부터 고장시간까지를 의미합니다.<br/>
MTBF는 MTBF = MTTR + MTTF 입니다.<br/>

[more..](https://m.blog.naver.com/sigmagil/222000246303)

</details>

---

<details markdown="1">
<summary><b>OSINT</b></summary>

<br/>
공개출처정보(open source intelligence, OSINT)는 공개된 출처에서 얻은 정보들을 말한다. 혹은 오픈소스 인텔리전스 또는 공개정보, 공개된 정보, 공개소스정보, 오픈소스정보 등으로도 불린다.

[more..](https://mrrootable.tistory.com/90)

</details>

---

<details markdown="1">
<summary><b>NTP서버</b></summary>

<br/>
Network Time Protocol의 약자로 Network 상에 연결된 장비와 장비 간에 시간 정보를 동기화하기 위한 프로토콜

[more..](https://aorica.tistory.com/46)

</details>

---

<details markdown="1">
<summary><b>ESM</b></summary>

<br/>
통합보안관리(Enterprise Security Management, ESM) 전산환경의 장애 발생 시 중앙에서 원격으로 통제하여 처리 및 조치를 취할 수 있도록 전산환경의 성능이나 보안의 취약성을 종합 관리하여 시스템의 안전성을 높여주는 시스템

[more..](https://m.blog.naver.com/PostView.nhn?blogId=on21life&logNo=221388898666&proxyReferer=https:%2F%2Fwww.google.com%2F)

</details>

---

<details markdown="1">
<summary><b>CVE, CWE, CCE, CVSS</b></summary>


```note
**취약점**(Vulnerability)이란, **정보시스템이나 소프트웨어 상에 존재하는 보안상의 약점**을 말한다.

기업에서 해킹이나 서비스 장애, 데이터 유출, 변조, 삭제 등이 일어난 경우, 이러한 시스템 상의 취약점을 악용하여 피해가 발생하게 된다.
```

CVE(Common Vulnerabilities and Exposures): 컴퓨터 하드웨어 또는 소프트웨어 결함이나 체계, 설계상의 취약점

CWE(Common Weakness Enumeration): 다양한 언어 (C, C++, C#, Python..) 및 아키텍쳐, 디자인 설계, 코딩 등의 개발단계에서 발생가능한 취약점

CCE(Common Configuration Enumeration): 사용자에게 허용된 권한 이상의 동작을 허용하거나, 범위 이상의 정보 열람, 변조, 유출을 가능하게 하는 시스템 설정 상의 취약점

CVSS(Common Vulnerability Scoring System): CVSS는 공통 취약점 등급 시스템으로 해석할 수 있으며, 취약점 위험도를 계산할 수 있는 개방형 프레임워크이다. 취약점의 위험도 평가를 위해 취약점의 접근 경로, 복잡성, 인증 여부, 사용자 인터페이스, 기밀성, 무결성, 가용성 등 여러 항목을 사용한다. 점수를 계산할 수 있는 사이트는 NIST(National Institute of Standards and Technology)에서 관리하고 있는 NVD에서 제공하고 있다.<br/>

[more..](https://m.blog.naver.com/lhi5693/221676723094)

</details>


---

<details markdown="1">
<summary><b>Snort</b></summary>

<br/>
스노트(snort)는 오픈소스 네트워크 침입 탐지 시스템이다. 또한, 침입 탐지 시스템 IDS의 대명사로 사용된다.<br/>

[more..](https://nan491.tistory.com/entry/VMware-Snort%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0-%EC%8B%A4%EC%8A%B5%ED%95%98%EA%B8%B0-1)

</details>

---

<details markdown="1">
<summary><b>시큐어코딩(secure coding)</b></summary>

<br>
소프트웨어(SW)를 개발함에 있어 개발자의 실수, 논리적 오류 등으로 인해 SW에 내포될 수 있는 보안취약점(vulnerability)을 배제하기 위한 코딩 기법을 뜻 한다. 

[more..](https://m.blog.naver.com/PostView.nhn?blogId=gs_info&logNo=220707616924&proxyReferer=https:%2F%2Fwww.google.com%2F)

</details>

---

<details markdown="1">
<summary><b>APT(Advanced Persistent Threat) 공격</b></summary>

<br>
APT는 ‘지능형 지속 공격(Advanced Persistent Threat)’의 약자로, 오랜 기간에 걸친 지속적인 해킹 시도를 통해 개인정보와 같은 중요한 데이터를 유출하는 형태의 공격을 의미합니다.

[more..](https://www.samsungsemiconstory.com/1912)

</details>

---

<details markdown="1">
<summary><b>Zero day attack</b></summary>

<br>
제로 데이 공격(또는 제로 데이 위협, Zero-Day Attack)은 컴퓨터 소프트웨어의 취약점을 공격하는 기술적 위협으로, 해당 취약점에 대한 패치가 나오지 않은 시점에서 이루어지는 공격을 말한다. 이러한 시점에서 만들어진 취약점 공격(익스플로잇)을 제로 데이 취약점 공격이라고도 한다.

제로 데이 공격 대상물이 되는 프로그램은 공식적으로 패치가 배포되기 전에 감행된다. 이런 프로그램들은 보통 대중들에게 공개되기 전 공격자들에게로 배포된다. 단어의 어원은 공격이 감행되는 시점에서 유래한 것이다. 제로 데이 공격 대상물은 대중과 프로그램 배포자들이 잘 모르는 것이 보통이다

[more..](https://ko.wikipedia.org/wiki/%EC%A0%9C%EB%A1%9C_%EB%8D%B0%EC%9D%B4_%EA%B3%B5%EA%B2%A9)

</details>

---

<details markdown="1">
<summary><b>쇼단(Shodan)</b></summary>

<br>
쇼단(Shodan) 검색엔진은 “보안취약점을 가진 시스템”을 찾아 내어, 보안을 강화하기 위한 수단으로 개발되었지만, “보안취약점을 가진 시스템”을 찾아 주는 기능을 가지고 있기 때문에, “어둠의 구글” , “해커들의 놀이터” 라는 별칭이 따라 붙고 있습니다.

[more..](https://m.blog.naver.com/PostView.nhn?blogId=aepkoreanet&logNo=221384830952&proxyReferer=https:%2F%2Fwww.google.com%2F)

</details>

---

<details markdown="1">
<summary><b>Censys</b></summary>

<br>
censys는 인터넷과 연결된 수많은 호스트와 네트워크 정보를 조회할 수 있는 검색 엔진이다. 전 세계 인터넷 상 40억개의 달하는 IP주소를 5분 이내에 스캔해 외부 인터넷과 연결된 수 많은 시스템들에 대한 정보를 조회하는 ZMap과 ZGrab을 통해 핑(ping) 작업을 하여, 어떠한 형태의 디바이스들이 응답했는지 인지하고, 암호화 방식을 사용했는지, 어떤 형태로 구성되었는지 해당 소프트웨어에 대한 세부적인 부분들을 파악 할 수 있다.

[more..](https://blog.naver.com/chogar/220962239041)

</details>

---

<details markdown="1">
<summary><b>EDR(Endpoint Detection and Response)</b></summary>

<br>
아직까지 일반적인 클라이언트에서 가장 많이 활용화 되고 있는 것은 단연 일반적인 백신이다. 그러나 사이버 공격은 나날이 지능화 되어 가고 있기 때문에, 기존의 백신으로는 제로데이 공격, APT 공격을 비롯한 현 공격 추세에 적절한 솔루션이라고 말하기에는 무리가 있다. 그래서 이러한 한계점을 어느정도 보완할 수 있는 클라이언트 보안 솔루션이 바로 EDR이다. Endpoint Detection and Response 단어 그 자체에서도 알 수 있듯이, 엔드포인트 위주의 보안 솔루션을 일컫는다.

EDR이란 클라이언트 자체에서의 보안을 말하는데, 클라이언트에 설치되어 특정한 행동이나 이상징후가 보이면 바로 탐지 그리고 그것에 대한 대응을 한다. 이러한 특징을 가지는 것에 대표는 백신이라고 할 수 있다. 그러나 백신과 다른 이유는 백신이 시그니처와 패턴 위주로 악성 공격을 탐지한다고 하면, EDR은 머신러닝과 인공지능을 활용해 탐지를 한다. 그렇다고 EDR이 패턴과 시그니처 탐지를 안 한다고 한다면 그것 또한 아니다. 클라이언트에 깔려 있는 EDR의 에이전트는 클라이언트의 거의 모든 행동을 관찰하고 분석하며, 그러한 관찰한 내용들을 서버에 있는 DB와 대조를 하고, 일치하는 것이 없으면 머신러닝과 인공지능을 이용해 위협을 대응해 가기 시작한다. (예를 들어 클라이언트가 메일을 보고 행위를 취할 때 메일을 분석하고 위협을 차단하거나 문서를 읽을 때 적절한 문서인지 판단하는 역할을 한다.)

[more..](https://www.somansa.com/introduce/newsevent/why_endpoint_detection_and_response_solution/)

</details>

---

<details markdown="1">
<summary><b>Cyber Kill Chain(사이버 킬 체인)</b></summary>

<br>
APT에 대응하기 위해 록히드 마틴사가 제시한 방법으로, 공격자의 공격 단계 중 하나만 사전에 확실히 제거해도 실제 공격까지 이어질 수 없다는 점에 착안한 방어전략이다.

[more..](https://www.itworld.co.kr/news/100774)

</details>

---

<details markdown="1">
<summary><b>슬래머 웜(SQL Slammer)</b></summary>

<br>
슬래머 웜은 다양한 인터넷 호스트에 서비스 거부 공격(DoS)을 실시하는 웜으로, 개인컴퓨터보다는 네트워크에 더 위협적인 웜이다. 2003년 등장해 10분 만에 7만 5,000대의 컴퓨터를 감염시킬 정도로 확산속도가 빨랐다. 이메일이나 메신저로 전파되던 기존 웜과는 달리, 시스템의 취약점이 발견되지마자 웜 코드가 실행됐기 때문이다. 미처 보안패치를 실시할 시간적 여유가 없다보니 피해규모가 커질 수밖에 없었다. 특히 국내에서 1.25 인터넷 대란을 일으키며 큰 피해를 입혔다.

[more..](https://it.donga.com/8222/)

</details>

---

<details markdown="1">
<summary><b>스턱스넷(Stuxnet)</b></summary>

<br>
스턱스넷(Stuxnet)은 2010년 6월에 발견된 웜 바이러스이다. 마이크로소프트 윈도우를 통해 감염되어, 지멘스 산업의 소프트웨어 및 장비를 공격한다. 이 웜이 산업시설을 공격하는 최초의 악성 소프트웨어는 아니지만,[2] 산업시설을 감시하고 파괴하는 악성 소프트웨어로는 최초이다.

이 웜은 마이크로소프트 윈도가 설치된 임의의 컴퓨터에 감염되지만, 지멘스의 SCADA 시스템만을 감염시켜 장비를 제어하고 감시하는 특수한 코드를 내부에 담고 있다.[3][4] 스턱스넷은 장비를 프로그램하는 데 사용되는 PLC를 감염시켜 장비의 동작을 변경한다

[more..](https://it.donga.com/8222/)

</details>

---

<details markdown="1">
<summary><b>디페이스(Deface)</b></summary>

<br>
deface는 외관을 훼손한다는 뜻이며 2가지 종류의 공격으로 분류됩니다.

1. Website Defacement<br/>
실제적으로 Web Site에 침투하여, 홈페이지 화면의 내용을 변경시키는 공격입니다. Web Site 관리자의 ID/PW를 탈취하여, 관리자 권한으로 Web site의 Source code를 해커의 입맛에 맞게 수정하는것입니다.

2. Re-Direct 공격<br/>
Web Site 내용은 건드리지 않고, 도메인 이름을 IP 주소로 변경하는 현 DNS시스템의 취약점을 이용하는것 입니다.<br/>
해커는 미리 Fake-Site를 만들어놓습니다. 사용자는 정확한 도메인 주소를 입력하였는데, 엉뚱한 Fake-Site로 접속한다는 것입니다.

[more..](https://it.donga.com/8222/)

</details>

---

<details markdown="1">
<summary><b>VPN(Virtual Private Network)</b></summary>

<br>   
VPN(Virtual Private Network)는 의미 그대로 가상 사설망을 의미한다. VPN은 인터넷과 같은 공중망을 마치 전용회선처럼 사용해 보안성을 향상하면서도 사설망을 이용하지 않았기 때문에 비용문제까지 해결한 네트워크라고 보면 된다.

공중망을 통해 데이터가 송수신되더라도 정보 유출이 없도록 라우터 체계를 비공개하고, 데이터를 암호화하고, 사용자 인증 기능을 추가하는 등 다양한 방법으로 보안 기능을 제공한다.

- 사설망(Private Networt): 특정 조직 내에서만 사용되는 네트워크로 인증된 사용자만이 사용 가능하며 보안성이 우수하지만 설치비용이나 관리비용이 든다는 단점이 존재

- 공중망(Public Network): 인터넷처럼 모두에게 공개된 네트워크로 보안성이 취약함

[more..](https://liveyourit.tistory.com/3)

</details>

---

<details markdown="1">
<summary><b>VPN 터널링</b></summary>

<br>   
터널링이란 연결해야 할 두 지점간에 마치 터널이 뚫린 것처럼 통로를 생성하는 것을 말한다. 그리고 이 터널은 터널링을 지원하는 프로토콜을 사용하여 구현되고 있으며 사설망과 같은 보안 기능을 제공하게 된다.

![vpn_tunneling](https://user-images.githubusercontent.com/76420201/105048769-42b70780-5aaf-11eb-89b6-972a59bce1e2.GIF)

[more..](https://liveyourit.tistory.com/3)

</details>

