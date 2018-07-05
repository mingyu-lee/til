# 객체지향 프로그래밍
* Object Oriented Programming, OOP
*객체
   * 생활에서 일종의 물건
   * 속성(Attribute)와 행동(Action)을 가짐
* OOP는 속성은 변수, 행동은 함수로 객체의 개념을 프로그램으로 표현

## 클래스, 객체, 인스턴스
* 클래스는 객체의 구체적인 형태를 설계한 명령어의 집합, 템플릿 또는 설계도
* 객체는 속성과 행위로 구성된 사물 또는 추상적 개념들의 정보를 표현한 것
* 인스턴스는 클래스로부터 인스턴스화를 통해 구현된 객체

### 추상화 기법
* 추상화 기법의 하나로 분류/인스턴스화(classification/instantiation) 개념 존재
* 분류는 객체들을 공통적인 속성을 공유하는 개념으로 범주화
* 인스턴스화는 추상화된 범주로부터 실재하는 객체를 만드는 과정을 의미
* 인스턴스라는 말은 추상적인 개념과 구체적인 객체 사이의 관계에 초점에 맞춘 용어

### 프로그램에서의 클래스, 인스턴스
* 추상화의 과정을 거쳐 속성과 행위를 가진 객체를 클래스로 표현하며, 클래스는 변수와 메서드를 가진다
* 프로그램 언어별로 클래스를 만드는 문법을 사용하여 인스턴스를 생성하게 된다.
   * Java: ExampleClass exampleClass = new ExampleClass();
   * Python: example_class = ExampleClass()

### 문법
```
[접근지정자] [기타제어자] class 클래스명 [extends Super클래스] [implements 인터페이스…] {
	/* 필드(멤버변수) */
	/* 메서드(멤버함수) */
}
```
* 멤버: 클래스 안에 선언된 것들
#### 클래스명 작성 규칙
| 작성규칙                                                          | 예                           |
|:------------------------------------------------------------------|:-----------------------------|
|                                                                   |                              |
| 하나 이상의 문자로 이루어져야 한다                                | Car, SportsCar               |
| 첫 번째 글자는 숫자가 올 수 없다                                  | Car, 3Car(x)                 |
| '$','_' 외의 특수 문자는 사용할 수 없다                           | $car, _Car, @Car(x), #Car(x) |
| 자바 키워드(예약어)는 사용할 수 없다                              | int(x), for(x)               |
| 단일 단어 => 첫문자는 대문자 혼합 단어 => 각 단어 첫글자는 대문자 |                              |


### 예제
* Cat 클래스
```
public class Cat {
	
	/* 클래스 필드 (객체의 속성) */
	// 이름
	private String name;
	// 품종
	private String breed;
	// 나이
	private int age;
	
	/* 클래스 메서드 (객체의 행동) */
	public String cry() {
		return "냐옹";
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void setBreed(String breed) {
		this.breed = breed;
	}
	
	public void setAge(int age) {
		this.age = age;
	}
	
	public String getName() {
		return this.name;
	}
	
	public String getBreed() {
		return this.breed;
	}
	
	public int getAge() {
		return this.age;
	}
	
	// 모든 클래스의 부모인 Object 클래스의 toString 메서드 오버라이드
	@Override
	public String toString() {
		final StringBuilder sb = new StringBuilder("Cat{");
			sb.append("name='").append(name).append('\'');
			sb.append(", breed='").append(breed).append('\'');
			sb.append(", age='").append(age).append('\'');
			sb.append('}');
		return sb.toString();
	}
}
```
* Cat 클래스 인스턴스화
```
public class CatClassTest {
	public static void main(String[] args) {
		// new 연산자를 통해 Cat 클래스를 인스턴스화
		Cat nabi = new Cat();
		nabi.setName("나비");
		nabi.setBreed("페르시안");
		nabi.setAge(2);
		System.out.println(nabi);
	}
}
```
* 결과
```
Cat{name='나비', breed='페르시안', age='2'}
```
#### 예제 설명
* Cat 클래스를 만들고 클래스의 필드와 메서드를 선언
* CatClassTest 클래스에서 Cat 클래스를 new 연산자를 통해 인스턴스화하여 인스턴스를 생성 후 nabi라는 변수에 레퍼런스 저장
* 이 때 new 연산자를 통해 생성된 인스턴스는 힙(heap) 메모리 영역에 저장되며 nabi 변수는 메모리 레퍼런스(주소)를 가지고 있다.
* setter(세터) 메서드를 통해 name, breed, age를 세팅 후 오버라이드한 toString 메서드를 통해 필드값들을 출력한다.

## 구성 멤버
### 필드(field)
* 객체의 고유 데이터, 상태 정보를 저장하는 곳
* 생성자와 메소드 전체에서 사용되며 객체가 소멸되지 않는 한 객체와 함께 존재
* 초기화 하지 않으면 각 자료형의 기본값으로 초기화 됨
* 필드선언
   * 생성자 선언과 메소드 선언의 앞 뒤 어떤 곳에서도 필드 선언 가능
   * 단, 생성자와 메소드 내부에서는 선언될 수 없음 (생성자,메소드 내부의 변수는 지역변수)
* 필드사용
   * 필드 값을 읽고 변경하는 작업
   * 클래스 내부에서는 단순히 필드 이름으로 읽고 변경
   * 클래스 외부에서는 클래스로부터 객체 생성 후 사용 (일반적으로 직접 접근 못하게 캡슐화)
---
### 생성자(Constructor)
* new 연산자로 호출되는 특별한 중괄호 블록
* 객체 생성 시 초기화 담당
* 필드를 초기화하거나 메소드를 호출해서 객체를 사용할 준비
* 클래스 이름으로 되어 있고 리턴 타입이 없다
* 생성자 선언
   * 생성자를 선언 안해도 기본적으로 컴파일시 디폴트 생성자가 생성됨
   * 생성자는 메소드와 비슷한 모양을 가지나, 리턴 타잆이 없고 클래스 이름과 동일
   * 클래스에 생성자가 명시적으로 선언되어 있을 경우 반드시 선언된 생성자를 호출해서 객체를 생성
   * 하나라도 인자값을 가진 다른 생성자를 호출할 경우 디폴트 생성자는 자동으로 생성되지 않으므로 디폴트 생성자를 호출하기 위해선 디폴트 생성자도 명시적으로 선언해줘야 함
* 필드 초기화
   * 필드를 선언할 때 초기값을 주면 동일한 클래스로부터 생성되는 객체들은 모두 같은 데이터를 가짐
   * 객체 생성 시점에 외부에서 제공되는 다양한 값들로 초기화 되어야 한다면 생성자에서 초기화 해야 함
* 관례적으로 필드와 동일한 이름을 갖는 매개변수 사용
   * 이 경우 필드와 매개변수 이름이 동일하므로 생성자 내부에서 해당 필드에 접근할 수 없다
   * why? 동일한 이름의 매개 변수가 사용 우선순위가 높다. 따라서 this 를 사용한다.
   * this는 객체 자신의 참조
```
public class Cat {
	private String name;
	public setName(String name) {
		// 필드 name과 매개변수 name의 이름이 같다
		// name = name
		this.name = name
	}
	
}
```
* 생성자 오버로딩
   * 매개변수를 달리하는 생성자를 여러 개 선언하는 것
   * 오버로딩 시 주의점은 매개 변수의 타입과 개수 그리고 선언된 순서가 똑같을 경우 매개 변수 이름만 바꾸는 것은 오버로딩이라고 볼 수 없음
* 다른 생성자 호출(this())
   * 생성자 오버로딩이 많아질 경우 생성자 간의 중복된 코드 발생
   * 이 경우 필드 초기화한 내용은 한 생성자에만 집중적으로 작성하고 나머지 생성자는 초기화 내용을 가지고 있는 생성자를 호출하는 방법으로 개선
   * 생성자에서 다른 생성자 호출할 때 this() 코드 사용
   * this()는 자신의 다른 생성자를 호출하는 코드, 반드시 생성자 첫줄에서만 허용
```
public Cat(String name, String breed) {
        this.name = name;
        this.breed = breed;
}

public Cat(String name, String breed, int age) {
        this(name, breed);
        this.age = age;
}

```
* 생성자 매개변수가 많아질 경우 빌더 패턴 고려
   * [Effective Java #2 생성자 매개변수가 많은 경우에 빌더 사용 고려에 관한 백기선님 요약글](https://github.com/keesun/study/blob/master/effective-java/item2.md)

* 생성자 관련 디자인패턴: static 팩토리 메서드 사용 참고
   * [Effective Java #1 생성자 대신 static 팩토리 메서드를 사용에 관한 백기선님 요약글](https://github.com/keesun/study/blob/master/effective-java/item1.md)
---
### 메서드(Method)
* 객체의 동작에 해당하는 중괄호 블록
* 메서드 호출 => 중괄호 블록 내 모든 코드 실행
* 용도
   * 필드 읽고 수정
   * 다른 객체 생성해서 다양한 기능 수행
   * 객체 간의 데이터 전달 수단
   * 이외 다양한 행동 구현
* 메서드 선언
```
[접근제한자] [기타제어자] 반환자료형 메서드명(매개변수) {    [return 리턴값;]}
```
   * 메서드 선언부 = 메서드 시그너처
* 리턴 타입
   * 메서드가 실행 후 리턴하는 값의 타입
   * 메서드 실행 후 결과를 호출한 곳에 넘겨줄 경우에는 리턴 값이 있어야 함
   * 리턴 값의 타입은 선언부의 반환자료형과 동일해야 함
   * 리턴 타입이 있다고 해서 반드시 리턴값을 변수에 저장할 필요 없음
   * void 타입의 경우 리턴문 없이 사용 가능

* 매개 변수의 수를 모를 경우
   * 매개 변수를 배열 타입으로 선언
   * … 으로 선언후 리스트 나열
```
public int sum(int ... args) {
        return IntStream.of(args).sum();
}
```
* 메서드 호출
* 메서드는 클래스 내/외부의 호출에 의해 실행
   * 클래스 외부에서 호출할 경우 우선 클래스로부터 객체 생성
   * 클래스 참조변수 = new 클래스(매개값);   * 참조변수.메서드(매개값); (리턴값 없거나, 받지 않을 경우)   * 타입 변수 = 참조변수.메서드(매개값); (리턴값 받고 싶을 때)
* 메서드 오버로딩
   * 클래스 내에 같은 이름의 메서드를 여러 개 선언하는 것
   * 매개 변수의 타입, 개수, 순서 중 하나가 달라야 한다 (시그니처가 달라야 한다)

