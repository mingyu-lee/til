# Map & Reduce

## Map Function
* Sequence 자료형 각 element에 동일한 function을 적용함
* 매핑(사상)
* 두 개 이상의 list에도 적용 가능함, if filter도 사용가능
* Python 3는 iteration을 생성하므로 list를 붙여줘야 list 사용 가능
* generator: 실행시점의 값을 생성, 메모리 효율적
```
ex = [1,2,3,4,5]
f = lambda x: x ** 2
print(list(map(f, ex)))
[1, 4, 9, 16, 25]

f = lambda x, y: x + y
>>> print(list(map(f, ex, ex)))
[2, 4, 6, 8, 10]

# generator
print((map(lambda x: x+x, ex)))
<map object at 0x0000024E2ACD53C8>

```
## Reduce Function
* map function과 달리 list에 똑같은 함수를 적용해서 통합

```
from functools import reduce
print(reduce(lambda x,y: x*y, [2,2,2,2,2]))

32
```

## Summary
* Lambda, map, reduce는 간단한 코드로 다양한 기능을 제공
* 그러나 코드의 직관성이 떨어져서 lambda나 reduce는 python3에서 사용을 권장하지 않음
* Legacy 라이브러리나 다양한 머신러닝 코드에서 여전히 사용 중



