# 클래스

```
class Person(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__ (self):
    return "Hello, My name is %s. I'm %s years old" % (self.name, self.age)
  def eat(self, food):
    print("I eat food")
		
# __init__ 호출
hong = Person("홍길동", 32)

# __str__ 호출
print(hong)
Hello, My name is 홍길동. I'm 32 years old

# eat 호출
hong.eat("pizza")
I eat food


```

## 문법

### ①class ②Person③[(object)]:
* ① class 예약어
* ② class 이름
* ③ 상속할 부모 클래스 (생략가능), 기본적으로 모든 클래스는 object 클래스를 상속한다

### def ①__init__(②self, ③name, age):
* ① 생성자: 클래스 인스턴스화할 때 초기화 함수, 생성자에 맞는 아규먼트를 넘겨줘야 인스턴스화 가능
* ② 생성되는 객체 자기자신으로 첫번째 파라미터에 명시적으로 선언하나 호출시에는 생략된다
* ③ 생성자 파라미터

### def ①__str__(self)
* ① 문자열화 함수로써 인스턴스 자체를 출력할 때 형식을 지정해준다

