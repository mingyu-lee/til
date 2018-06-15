# 객체 지향 프로그램
* Object-Oriented Programming, OOP
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
* 추상화의 과정을 거쳐 속성과 행위를 가진 객체를 클래스로 표현하며, 클래스는 변수와 메소드를 가진다
* 프로그램 언어별로 클래스를 만드는 문법을 사용하여 인스턴스를 생성하게 된다.
   * Java: ExampleClass exampleClass = new ExampleClass();
   * Python: example_class = ExampleClass()

## 예시
```
class Cat():
  # 클래스 초기화
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  # 함수 cry
  def cry(self):
    print('miaow')

  # 함수 move
  def move(self):
    print('move')

# 인스턴스화
my_cat = Cat('nabi', 'Persian', 1)

# 인스턴스의 레퍼런스를 가진 my_cat 변수를 통해 인스턴스의 cry 함수 호출
my_cat.cry()

# cry 함수 실행 결과
miaow

my_cat.move()

move

```
