
# HTTP(HyperText Transfer Protocol)

- 요청 (request) / 응답(response)
- Stateless = Sessionless => 요청과 요청 간의 관계를 알 수 없다

보안하기 위해서 **Cookie, Session** 개념이 발생

http1 

개행 문자 = 줄 바꿈 문자 = CR(carriage return) + LF(Line feed)




제어문자와 특수문자는 고유한 이름을 줍니다. 이것이 CR LF

요청과 응답은 라인단위로 의미가 있고, 라인의 끝은 개행문자가 나온다

- Request

시작 방식(method) URI HTTP/1.1
헤더 Host: localhost:8080
            :
        connection : keep-alive

본문 (방식에 따라 있을 수도 있고, 없을 수도 있음)

방식(method)

GET
POST
DELETE
PUT
OPTIONS
HEAD


URI(Uniform Resource Identifier)

HTTP2 이미지

스킴 (scheme) = 프로토콜
호스트 = 도메인 = IP주소
경로 => 해당 호스트의 웹 루트 디렉토리

http://www.exam.com/data/upload/mypic.jpg

www.exam.com 호스트의 웹 루트 디렉터리를 기준으로 해당 리소스를 제공

**/var/www/html/**data/upload/mypic.jpg

리퀘스트 해더

1. 헤더의 끝은 empty line (내부코드로 보면 개행 문자가 2번연속 나온다)

2. 

response 헤더

실질적으로 브라우저가 내용을 보는 내용은 응답 본문에 있다.