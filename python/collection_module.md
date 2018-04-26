# Collections Module
* List, Tuple, Dict에 대한 Python Built-in 확장 자료 구조(모듈)
* 편의성, 실행 효율 등을 사용자에게 제공
* deque, Counter, OrderedDict, defaultdict, namedtuple

## deque
* Stack과 Queue를 지원하는 모듈
* List에 비해 효율적인 자료 저장 방식을 지원함
* rotate, reverse 등 Linked List의 특성을 지원함
* 기존 List 의 함수를 모두 지원함
* 효율적 메모리 구조로 처리 속도 향상
```
from collections import deque

deque_list = deque()
for I in range(5):
	deque_list.append(i)
print(deque_list)

deque_list.appendleft(10) # list 왼쪽에 추가
print(deque_list)

```

## OrderedDict
* 데이터를 입력한 순서대로 dict를 반환함
```
from collections import OrderedDict

d = collections.OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
for k, v in d.items():
   print(k, v)

a 1
b 2
c 3

```

## defaultdict
* dict type의 값에 기본 값을 지정, 신규값 생성시 사용하는 방법
```
from collections import defaultdict

d = defaultdict(lambda: 0)
print(d["first"])
0
```
### 활용처
* 하나의 지문에 각 단어들이 몇 개나 있는지 세고 싶을 경우
* Text-mining 접근법: Vector Space Model

## Counter
* Sequence type의 data element들의 개수를 dict 형태로 반환
* Dict type, Key arguments 방식으로 생성 가능
* Set의 연산들을 지원(집합)
```
from collections import Counter

c = Counter()
c = Counter('hello')
print(c)
Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

c = Counter({'a': 3, 'b': 1}) # Mapping 방식 생성
c = Counter(a=3, b=1) # Keyword arguments 방식 생성

print(c)
Counter({'a': 3, 'b': 1})

print(list(c.elements()))
['a', 'a', 'a', 'b']
```

# namedtuple
* Tuple 형태로 Data 구조체를 저장하는 방법
* 저장되는 data의 variable을 사전에 지정해서 저장함

```
from collections import namedtuple

Location = namedtuple('Location', ['latitude', 'longitude'])

loc = Location(37.566, 126.987) 
```
