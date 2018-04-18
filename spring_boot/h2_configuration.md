# H2 Database
* Java로 작성된 RDBMS로 Java 애플리케이션에 임베드하거나 클라이언트-서버 모드에서 구동할 수 있음
* SQL 표준 일부 지원
* 인메모리(in-memory) 테이블과 디스크 기반 테이블 생성 가능
* 테이블은 영구/일시적으로 관리
* 트랜잭션 처리
* 테이블 수준의 잠금과 다중 버전 동시성 제어(MVCC) 구현
* [H2 홈페이지](http://www.h2database.com)

## 인덱스 타입
* 인메모리 테이블: 해시 테이블 또는 트리
* 디스크 테이블: B 트리

## 역사
* 1996년 - Thomas Mueller Hypersonic SQL 개발
* 2001년 - Hypersonic SQL 프로젝트 중단되고 HSQLDB 그룹이 Hypersonic SQL 기반으로 HSQLDB 개발
* 2004년 5월 - Thomas Mueller H2 개발 시작
* 2005년 12월 - 첫판 출시
* ※ H2는 Hypersonic 2를 나타내지만 Hypersonic SQL과 HSQLDB와 소스 코드를 공유하지 않는다.

## 스프링에서 사용시 편의성
* 가볍고 빠르며 사용이 쉽다.
* 개발 환경에서 사용시 편리하다.
* JPA/Hibernate와 연동이 가능하다.

# Spring Boot H2 시작

## 의존성

### Maven
```
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
</dependency>
```

## Spring 설정
* Java Config 설정 방식
* `application.properties` 설정 방식 (간단하므로 프로퍼티 설정 선호)

### Java Config 설정
```
import org.h2.server.web.WebServlet;
import org.springframework.boot.web.servlet.ServletRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class WebConfig {

    @Bean
    public ServletRegistrationBean h2servletRegistration() {
        ServletRegistrationBean registrationBean = new ServletRegistrationBean(new WebServlet());
        registrationBean.addUrlMappings("/h2-console/*");
        return registrationBean;
    }
}
```
* addUrlMappings의 인자가 H2 데이터베이스 콘솔 접속 주소

### application.properties 설정
```
# H2
spring.h2.console.enabled=true
spring.h2.console.path=/h2-console

```
* spring.h2.console.path의 값이 H2 데이터베이스 콘솔 접속 주소

## H2 콘솔
* 기본적인 스프링부트 애플리케이션 시작의 경우 http://localhost:8080/h2-console
