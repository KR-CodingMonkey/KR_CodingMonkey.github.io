 
# 보안 솔루션 종류


<details markdown="1">
<summary><b>방화벽(firewall)</b></summary>

<br>   
- 침입 차단 시스템
- 가장 기본적으로 사용되는 솔루션
- 외부 네트워크와 내부 네트워크 사이에서 지나다니는 패킷을 **미리 정한 정책/규칙(RuleSet)**에 따라 차단하거나 보내주는 기능을 하는 H/W 또는 S/W

### 장비에 따른 분류

---

1) 소프트웨어 기반 방화벽
- 일반적인 호스트 pc에 설치하는 sw형태의 프로그램
- 오픈소스 sw로는 iptables, ipfire, presense, endian, monowall ...

2) 하드웨어 기반 방화벽
- 네트워크 장비 기반
- 자체적인 보안기능을 수행하도록 제작된 하드웨어
- 필터링 기술의 한계가 있음

3) 멀티코어 프로세서 기반 방화벽
- 소프트웨어 방화벽과 하드웨어 방화벽의 장점을 혼합한 형태의 방화벽
- 소프트웨어(유연성)
- 하드웨어(처리속도) 

### 기술적 분류

---

1) Packet Filter Firewall

- 1세대 방화벽 : 스크리닝 라우터
- OSI 7 layer의 3계층(네트워크) 4계층(전송)에서 동작
- 패킷 필터링

 

2) Application Layer Gateway(=ALG)

- 2세대 방화벽 : Proxy
- OSI 7 LAYER의 application 계층
- 실제 데이터까지 보고 필터링

 

3) Circuit Gateway

- 2세대 방화벽 → Proxy
- OSI 7 layer의 session layer에서 동작함
- 클라이언트와 서버가 세션 연결을 맺어야하기 때문에 외적으로 S/W가 필요하다
- 현재는 잘 쓰이지 않는다.

 

4) Stateful Inspection

- 3세대 방화벽 -> 상태 정밀 검사
- OSI 7 layer의 네트워크, 전송 계층에서 동작
- 필터링 속도 개선 (속도 향상)
: 방화벽에서 상태추적테이블을 생성하여 l3,l4 정보를 기억하여 정책 검사를 한번만 수행함.
즉, 필터링을 한번 통과하면 지속적으로 통과시킴
: 동적으로 보안정책을 수정하며 실제 접속상태를 감시하여 통신상태에 따라 허용/거부 수행

 

5) Dynamic Packet Filtering

- 보안 정책을 동적으로 수정가능
- 세션 정보를 기록/유지함 능동적인 보안관리 가능

6) hybrid 방식

- 대부분의 firewall 방식
- 패킷 필터링 + application gateway 방식 혼합
- 사용자의 편의성 별로, 기업환경 별로 유연성있게 방화벽 구성 가능
- 관리 시 복잡함

[more..](https://liveyourit.tistory.com/3)

</details>

---
<details markdown="1">
<summary><b>IDS(Intrusion Detection System)</b></summary>

<br>   
- 침입 탐지 시스템
- 네트워크를 통한 공격을 탐지하기 위한 장비
- 방화벽이 차단하지 못한 해킹, 악성코드의 활동 탐지
- 설치위치에 따라 호스트기반(HIDS), 네트워크기반(NIDS)으로 나뉜다

[more..](https://liveyourit.tistory.com/3)

</details>
---

<details markdown="1">
<summary><b>IPS(Intrusion Prevention System)</b></summary>

<br>   
- 침입 탐지+차단 시스템
- IDS+Firewall 네트워크 기반의 솔루션을 논리적으로 결합한 시스템
- 방화벽의 rule 차단은 공격에 대한 차단율이 낮다는 점을 보완하기 위해 만들어짐
- 보통 비정상적인 트래픽에 대해 능동적으로 분석하고 차단한다.

[more..](https://liveyourit.tistory.com/3)

</details>

---

<details markdown="1">
<summary><b>UTM (Unified Threat Management)</b></summary>

<br>   
- 통합 위협 관리
- 하나의 장비에서 여러 보안기능을 통합적으로 제공
- 개별 장비보다는 기능이 떨어질 수 있다.
- 제공되는 기능 (방화벽,web filter, waf, vpn, ids, ips...)

[more..](https://liveyourit.tistory.com/3)

</details>

---

<details markdown="1">
<summary><b>DLP(Data Loss Prevention)</b></summary>

<br>
- 데이터 유출 방지 솔루션이라고 하며 기업내의 다양한 주요 정보를 보호하며 외부 유출을 차단 또는 방지하기 위한 장비.


[more..](https://www.itworld.co.kr/news/157362)

</details>

---

<details markdown="1">
<summary><b>WAF (WEB APPLICATION FIREWALL)</b></summary>

<br>   
- 웹 방화벽

[more..](https://liveyourit.tistory.com/3)

</details>

---

<details markdown="1">
<summary><b>VPN (Virtual Private Network)</b></summary>

<br>   
- 가상 사설망
- 인터넷을 전용선처럼 사용할 수있게 함
- 본사와 자사간 전용망을 설치한것과같은 효과
- 기존의 사설망의 고비용 부담 해소
- 터널링 + 암호화

[more..](https://liveyourit.tistory.com/3)

</details>

---

<details markdown="1">
<summary><b>NAC (Network Access Control)</b></summary>
<br/>   
- ip 관리 시스템에서 발전한 솔루션
- 네트워크에 연결된 여러 단말의 정보를 수집, 수집된 정보를 바탕으로 단말들을 분류함
- 분류한 그룹의 보안위협정도에 따라 제어 수행
- 보통 일반 PC들을 컨트롤하기 위해 만들어짐

- 접근 제어/인증
  - 내부 직원 역할 기반의 접근 제어
  - 네트워크의 모든 IP 기반 장치 접근 제어

- PC 및 네트워크 장치 통제(무결성 체크)
  - 백신 관리
  - 패치 관리
  - 자산 관리(비인가 시스템 자동 검출)

- 해킹, 웜, 유해 트래픽 탐지 및 차단
  - 유해 트래픽 탐지 및 차단
  - 해킹 행위 차단, 완벽한 증거 수집 능력

[more..](https://liveyourit.tistory.com/3)

</details>

---

<details markdown="1">
<summary><b>ESM(Enterprise Security Management)</b></summary>

<br>   
- Gui를 통해 각종 시스템 및 장비의 상태, 성능, 장애여부 등을 모니터링하고 관리하기 위한 시스템
- 회사의 비즈니스 안정성 확보, 자원최적화, 가치 향상

[more..](https://liveyourit.tistory.com/3)

</details>