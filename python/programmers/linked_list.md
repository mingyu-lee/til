# 연결 리스트 (Linked Lists)
* 연결 리스트는 각 원소들을 줄줄이 엮어서 관리하는 방식

## 추상적 자료구조(Abstract Data Structures)
* Data
  * 예: 정수, 문자열, 레코드...
* A set of operations
  * 삽입, 삭제, 순회
  * 정렬, 탐색


## 기본적 연결 리스트
* Node: 링크드 리스트 구성 요소
  * data: 원소
  * Link(next): 다음 노드를 가리키는 주소
* Node 내의 데이터는 다른 구조로 이루어질 수 있음
* 예) 문자열, 레코드, 또 다른 연결 리스트 등
* 첫번째 node를 head, 마지막 node를 tail, node의 갯수 등이 추상적 연결 리스트에 포함되는 요소

```
class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
```
### 연산 정의
* 특정 원소 참조(k번째)
* 리스트 순회
* 길이 얻어내기
* 원소 삽입
* 원소 삭제
* 두 리스트 합치기

#### 특정 원소 참조
```
def getAt(self, pos):
    if pos <= 0 or pos > self.nodeCount:
        return None
    i = 1
    curr = self.head
    while i < pos:
        curr = curr.next
        i += 1
    return curr
```

#### 리스트 순회
```
def traverse(self):
    answer = []
    i = 1
    while i < self.nodeCount:
        answer.append(self.getAt(i))
    return answer
```

### 배열과 비교한 연결 리스트
* 저장 공간
    * 배열: 연속한 위치
    * 연결 리스트: 임의의 위치
* 트특정 원소 지칭
    * 배열: 매우 간편 O(1)
    * 연결 리스트: 선형탐색과 유사 O(n)

#### 원소의 삽입
* pos가 가리키는 위치에 (1 <= pos <= nodeCount + 1) newNode를 삽입하고 성공/실패에 따라 True/False를 리턴
* 기본적인 코드 흐름 (예외 케이스 추가해야함)
```
def insertAt(self, pos, newNode)
    pref = self.getAt(pos - 1)
    newNode.next = prev.next
    prev.next = newNode
    self.nodeCount += 1
```
* 삽입하려는 위치가 맨 앞일 때
  * prev 없음
  * header 조정 필요
* 삽입하려는 위치가 맨 끝일 때
  * tail 조정 필요

##### 복잡도
* 맨 앞에 삽입하는 경우: O(1)
* 중간에 삽입하는 경우: O(n)
* 맨 끝에 삽입하는 경우: O(1)

#### 원소의 삭제
* pos가 가리키는 위치의 (1 <= pos <= nodeCount) node를 삭제하고 그 node의 데이터를 리턴
```
def popAt(self, pos):
```
* 삭제하려는 node가 맨 앞의 것일 때
    * prev 없음
    * head 조정 필요
* 리스트 맨 끝의 node를 삭제할 때
    * tail 조정 필요
    * prev를 찾을 방법이 없으므로 한번에 처리할 수 없다 → 앞에서부터 찾아와야 함
* 유일한 노드를 삭제할 때?\

##### 복잡도
* 맨 앞에서 삭제하는 경우: O(1)
* 중간에서 삭제하는 경우: O(n)
* 맨 끝에서 삭제하는 경우: O(n)
* 이를 해결하기 위해 이중연결리스트를 주로 사용함

#### 두 리스트의 연결
* 기본적인 코드 흐름
```
def concat(self, L):
    self.tail.next = L.head
    if L.tail:
        self.tail = L.tail
    self.nodeCount += L.nodeCount
```

