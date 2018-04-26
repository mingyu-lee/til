# Split
* String Type의 값을 나눠서 List 형태로 반환
```
numbers = 'one two three four five six seven'

# 빈칸을 기준으로 문자열 나누기
print(numbers.split())
['one', 'two', 'three', 'four', 'five', 'six', 'seven']

cities = 'Seoul,Incheon,Busan,Gwangju,Daegu'

# 콤마(,)를 기준으로 문자열 나누기
print(cities.split(','))
['Seoul', ' Incheon', ' Busan', ' Gwangju', ' Daegu']

# Unpacking (언팩킹)
a, b, c, d, e = cities.split(',')
print(a)
Seoul
print(d)
Gwangju
```

# Join
* String List들의 원소를 합쳐 String 반환
```
numbers = 'one two three four five six seven'.split()

number_string = ''.join(numbers)
print(number_string)
onetwothreefourfivesixseven

# 공백으로 연결
number_string = ' '.join(numbers)
print(number_string)
one two three four five six seven
```

