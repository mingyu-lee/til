
## 튜플 (tuple)
* 값의 변경이 불가능한 리스트
* 선언 시 "[]"(대괄호)가 아닌 "()"(괄호)를 사용
* 리스트의 연산, 인덱싱 슬라이싱 등을 동일하게 사용

## 집합 (Set)
* 값을 순서없이 저장, 중복을 허용하지 않는 자료형
* set 객체 선언을 이용하여 객체 생성
* 수학의 집합의 연산 가능

## 사전 (Dictionary)
* 데이터를 저장할 때 구분 값을 함께 저장
* 예) 주민등록 번호, 제품 모델 번호
* 구분을 위한 데이터 고유 값을 Identifier 또는 Key 라고함
* Key 값을 활용하여, 데이터 값(Value)를 관리함
* key와 value를 매칭하여 key로 value를 검색
* {key1: value1, key2: value2, key3: value3 … }

### 문법
```
dict = {} # dict 생성
# dict 여러 키:값 입력
dict = { "key1": "value1", "key2": "value2", "key3": "value3" }

# dict 입력
dict["key4"] = "value4"
dict["key5"] = "value5"

dict
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}

dict.items() # dict 데이터 출력
dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4'), ('key5', 'value5')])

dict.keys() # dict key 만 출력
dict_keys(['key1', 'key2', 'key3', 'key4', 'key5'])

dict.values() # dict value 만 출력
dict_values(['value1', 'value2', 'value3', 'value4', 'value5'])

# 반복문 활용
for k, v in dict.items():
   print(, v)

key1 value1
key2 value2
key3 value3
key4 value4
key5 value5

# 포함 여부 확인
"key1" in dict.keys()
True

"k" in dict.keys()
False

"value5" in dict.values()
True

"v5" in dict.values()
False

```
