# RestTemplate
`RestTemplate`은 HTTP 클라이언트 라이브러리를 통해 높은 수준의 API를 제공한다. REST 엔드포인트를 코드 한줄로 호출하기 쉽게 해준다.
오버로드된 메소드들은 다음과 같다.

### RestTemplate methods
* [representation이란 무엇인가](https://blog.npcode.com/2017/04/03/rest%EC%9D%98-representation%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80/)

|Method group| Description|
|:-----:| ------|
|getForObject| GET method를 통해 representation을 조회 |
|getForEntity| GET method를 통해 ResponseEntity를 조회 (status, headers, body) |
|headForHeaders| HEAD method를 통해 리소스의 모든 헤더들을 조회|
|postForLocation| POST method를 통해 새로운 리소스를 생성하고 응답에 Location 헤더를 리턴|
|postForObject| POST method를 통해 새로운 리소스를 생성하고 응답에 representation을 리턴|
|postForEntity| POST method를 통해 새로운 리소스를 생성하고 응답에 representation을 리턴|
|put| PUT method를 통해 리소스를 새로 생성하거나 수정|
|patchForObject| PATCH method를 통해 리소스를 수정하고 응답의 representation을 리턴.<br>주의할 것은 JDK HttpURLConnection은 PATCH 를 지원하지 않고, Apache HttpComponents와 다른 것들은 지원함|
|delete| DELETE method를 통해 특정 URI의 리소스를 삭제|
|optionsForAllow| ALLOW method를 통해 리소스가 허용하는 HTTP method들을 조회|
|exchange| 위의 method들 보다 더 일반화되고, 덜 선택적인 버전으로 필요한 경우 추가적인 유연성을 제공함<br>HTTP 메서드, URL, 헤더 및 본문을 포함한 RequestEntity를 입력받아 ResponseEntity를 리턴<br>이러한 방법을 사용하면 `Class` 대신 `ParameterizedTypeReference`를 사용하여 제네릭 타입 응답을 지정할 수 있음|
|execute| 요청을 수행하는 가장 일반화된 방법으로, 콜백 인터페이스를 통한 요청 준비 및 응답 추출에 대한 완벽한 제어가 가능|


## 초기화
기본 생성자는 `java.net.HttpURLConnection` 라이브러리를 사용한다. `ClientHttpRequestFactory`를 사용하여 다른 HTTP 라이브러리로 바꿀 수 있다.
스프링은 `Apache HttpComponents`, `Netty`, `OkHttp`를 지원한다.
* 예)
```java
RestTemplate template = new RestTemplate(new HttpComponentsClientHttpRequestFactory());
```
각 `ClientHttpRequestFactory`는 기본 HTTP 클라이언트 라이브러리(예: 자격 증명, 연결 풀링 등)에 대한 구성 옵션을 제공한다.
주의할 점은 `java.net` 패키지의 HTTP 구현체를 사용할 경우 401 상태를 가진 응답 객체에 접근할 때 익셉션이 발생할 수 있으므로, 이럴 경우 다른 HTTP 라이브러리 사용해야 한다.

## URIs
대부분의 `RestTemplate` 메소드는 `String` vararg 또는 Map<String, String>을 통해 URI 템블릿과 URI 템플릿 변수를 허용한다.
```java
/* String vararg */
String result = restTemplate.getForObject(
        "http://example.com/hotels/{hotel}/bookings/{booking}", String.class, "42", "21");

/* Map<String, String> */
Map<String, String> vars = Collections.singletonMap("hotel", "42");

String result = restTemplate.getForObject(
        "http://example.com/hotels/{hotel}/rooms/{hotel}", String.class, vars);
```
URI 템플릿은 자동으로 인코딩된다.
```java
restTemplate.getForObject("http://example.com/hotel list", String.class);

// 요청 url: "http://example.com/hotel%20list"
```
`RestTemplate`의 `uriTemplateHandler` 속성을 사용하여 URI 인코딩 방법을 지정할 수 있다 또는 `java.net.URI`를 사용하여 이를 사용하는 `RestTemplate` 메소드에 인자로 전달할 수 있다.
* 참고: [URI 관련 문서](https://docs.spring.io/spring/docs/5.1.0.RC1/spring-framework-reference/web.html#mvc-uri-building)

## Headers
exhcnage() 메소드를 사용하여 요청 헤더를 지정할 수 있다.
```java
String uriTemplate = "http://example.com/hotels/{hotel}";
URI uri = UriComponentsBuilder.fromUriString(uriTemplate).build(42);

RequestEntity<Void> requestEntity = RequestEntity.get(uri)
        .header(("MyRequestHeader", "MyValue")
        .build();

ResponseEntity<String> response = template.exchange(requestEntity, String.class);

String responseHeader = response.getHeaders().getFirst("MyResponseHeader");
String body = response.getBody();
```
`ResponseEntity`를 반환하는 `RestTemplate` 의 여러 메소드를 통해 응답 헤더를 얻을 수 있다.

## Body
`RestTemplate` 메서드에 전달되고 반환되는 객체는 `HttpMessageConverter`의 도움으로 raw content로 변환된다.

POST 메서드에서 입력된 객체는 요청 body에 직렬화된다.
```java
URI location = template.postForLocation("http://example.com/people", person);
```
요청의 `Content-Type` 헤더를 명시적으로 설정할 필요는 없다.  대부분의 경우 소스 객체 타입에 따라 호환되는 메시지 컨버터를 찾을 수 있고, 선택한 메시지 컨버터가 적절히 content-type을 설정한다.
필요한 경우 `exchange` 메서드를 사용하여 `Content-Type` 요청 헤더를 명시적으로 제공할 수 있으며, 이는 선택된 메시지 컨버터에 영향을 미칠 수 있다.

GET 메서드에서는 응답의 body가 출력 객체로 역직렬화된다.
```java
Person person = restTemplate.getForObject("http://example.com/people/{id}", Person.class, 42);

```
요청의 `Accept` 헤더는 명시적으로 설정할 필요가 없다. 대부분의 경우 `Accept` 헤더를 예상 응답 유형에 따라 호환되는 메시지 컨버터를 찾을 수 있다. 이 컨버터는 `Accept` 헤더를 채우는데 도움이 된다.
필요한 경우 `exchange` 메서드를 사용하여 `Accept`헤더를 명시적으로 제공할 수 있다.

기본적으로 `RestTemplate`은 선택적인 변환 라이브러리가 있는지 확인하는데 도움이 되는 클래스패쓰 검사에 따라 모든 내장 메시지 컨버터들을 등록한다. 또, 명시적으로 메시지 컨버터를 설정할 수 있다.

## Message Conversion
`spring-web` 모듈은 `InputStream`과 `OutputStream`을 통해 HTTP 요청 및 응답의 body를 읽고 쓰는 역할을 맡은 `HttpMessageConverter`를 포함한다. `HttpMessageConverter`는 클라이언트 측(예, `RestTemplate`)과 서버 측 (예, `Spring MVC REST controllers`)에서 사용된다.

주요 미디어(MIME) 유형에 대한 구체적인 구현은 프레임워크에서 제공되며 기본적으로 클라이언트 측 `RestTemplate` 및 서버측 `RequestMethodHandlerAdapter`에 등록된다.
[(메시지 구성 참조)](https://docs.spring.io/spring/docs/5.1.0.RC1/spring-framework-reference/web.html#mvc-config-message-converters)

`HttpMessageConverter`의 구현은 다음 섹션에 기술되어있다. 모든 컨버터들이 기본 미디어 타입을 사용하지만 `supportedMediaTypes` 빈 프로퍼티 설정으로 오버라이드 할 수 있다.

### HttpMessageConverter 구현체 목록
|MessageConverter| Description|
|:-----:| ------|
|StringHttpMessageConverter| HTTP 요청 및 응답으로부터 문자열(String)을 읽고 쓸 수 있는 구현체<br>기본적으로 모든 텍스트 미디어 타입들 `(text/*)`을 지원하며, `text/plain` `Content-Type`으로 작성한다. |
|FormHttpMessageConverter| HTTP 요청 및 응답으로부터 form 데이터를 읽고 쓸 수 있는 구현체<br>기본적으로 `application/x-www-form-urlencoded` 미디어 타입을 지원한다.<br>Form 데이터는 `MultiValueMap<String, String>`읽고 작성된다.|
|ByteArrayHttpMessageConverter| HTTP 요청 및 응답으로부터 바이트 배열을 읽고 쓸 수 있는 구현체<br>기본적으로 모든 미디어 타입 `(*/*)`을 지원하며, `application/octet-stream` `Content-Type`으로 작성한다.<br> 이 컨버터는 `supportedMediaTypes` 속성을 설정하고 `getContentType(byte[])`를 오버라이드하여  재정의할 수 있다|
|MarshallingHttpMessageConverter| `org.springframework.oxm` 패키지의 스프링의 마샬러(Marshaller)와 언마샬러(Unmarshaller) 추상화를 사용하여 XML을 읽고 쓸 수 있는 구현체<br>이 컨버터는 사용하기 전에 마샬러와 언마샬러를 필요로 한다.<br>이들은 생성자 또는 빈 프로퍼티를 통해 주입될 수 있다.<br>기본적으로 `text/xml`과 `application/xml`을 지원한다|
|MappingJackson2HttpMessageConverter| `Jackson` 라이브러리의 `ObjectMapper`를 사용하여 JSON을 읽고 쓸 수 있는 구현체<br>JSON 매핑은 필요에 따라 `Jackson`이 제공하는 어노테이션을 통해 커스터마이징 될 수 있다<br>추가 제어가 필요할 경우 특히, 특정 유형에 대해 커스텀 JSON 직렬화/역직렬화를 제공해야 하는 경우 ObjectMapper 속성을 통해 커스텀 ObjectMapper를 주입할 수 있다.<br>기본적으로 `application/json`을 지원한다|
|MappingJackson2XmlHttpMessageConverter| `Jackson XML`의 XmlMapper를 사용하여 XML을 읽고 쓸 수 있는 구현체<br>`Jackson`이 제공하는 어노테이션을 또는 JAXB를 사용하여 필요에 따라 XML 매핑은 커스터마이징 될 수 있다<br>추가 제어가 필요한 경우, 특히 특정 유형에 대해 커스텀 XML 직렬화/역직렬화를 제공해야하는 경우 ObjectMapper 속성을 통해 커스텀 XmlMapper를 주입할 수 있다<br>기본적으로 `application/xml`을 지원한다|
|SourceHttpMessageConverter| HTTP 요청 및 응답으로부터 `javax.xml.transform.Source`를 읽고 쓸 수 있는 구현체<br>`DOMSource`, `SAXSource`, `StreamSource`만 지원된다.<br>기본적으로 `text/xml`과 `application/xml`를 지원한다|
|BufferedImageHttpMessageConverter| HTTP 요청 및 응답으로부터 `java.awt.image.BufferedImage`를 읽고 쓸 수 있는 구현체<br>`Java I/O API`에서 지원하는 미디어 타입을 읽고 쓴다|

## Jackson JSON Views
객체 속성의 일부만 직렬화하도록 Jackson JSON View를 지정할 수 있다.
* 예)
```java
MappingJacksonValue value = new MappingJacksonValue(new User("eric", "7!jd#h23"));
value.setSerializationView(User.WithoutPasswordView.class);

RequestEntity<MappingJacksonValue> requestEntity =
    RequestEntity.post(new URI("http://example.com/user")).body(value);

ResponseEntity<String> response = template.exchange(requestEntity, String.class);
```

## Multipart
multipart 데이터를 전송하기 위해 multipart 내용을 대표하는 Objects 또는 내용과 헤더를 대표하는 `HttpEntity`를 값으로 가지는 `MultiValueMap<String, ?>`를 제공할 필요가 있다.
`MultipartBodyBuilder`는 multipart 요청을 만들어주는 편리한 API를 제공한다.

```java
MultipartBodyBuilder builder = new MultipartBodyBuilder();
builder.part("fieldPart", "fieldValue");
builder.part("filePart", new FileSystemResource("...logo.png"));
builder.part("jsonPart", new Person("Jason"));

MultiValueMap<String, HttpEntity<?>> parts = builder.build();
```
대부분의 경우 각 part에 `Content-Type`를 지정할 필요가 없다. `Content-Type`은 직렬화 하도록 선택한 `HttpMessageConverter` 또는 파일 확장자에 기반한 `Resource`의 경우에 자동으로 결정된다.
필요한 경우 오버로드된 builder 메소드를 통해 각 part에 사용할 `MediaType`을 명시적으로 제공할 수 있다.

`MultiValueMap`이 준비되면, `RestTemplate`에 인자를 넘겨줄 수 있다.
```java
MultipartBodyBuilder builder = ...;
template.postForObject("http://example.com/upload", builder.build(), Void.class);
```
`MultiValueMap`이 일반적인 form 데이터를 나타낼수 있는(예: `application/x-www-form-urlencoded`) String이 아닌 값을 가질 경우, `Content-Type`을 `multipart/form-data`로 지정할 필요 없다.
이는 ㅇ항상 `HttpEntity` 래퍼를 보장하는 `MultipartBodyBuilder`를 사용하는 경우에 해당된다.




## 참고
* [Spring Rest Client Documentation](https://docs.spring.io/spring/docs/5.1.0.RC1/spring-framework-reference/web.html#webmvc-client)
* [Spring RestTemplate](https://docs.spring.io/spring/docs/5.1.0.RC1/spring-framework-reference/integration.html#rest-client-access)