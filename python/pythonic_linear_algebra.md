# Linear Algebra

### 선형
* 직선 또는 그와 비슷한 성질을 가진 대상
* 일반적으로 1차함수 형태 = 선형성

### 대수학
* 문자에 숫자를 대입하여 푸는 문제
* 1개 이상의 변수를 가진 다항방정식을 푸는 문제

## Vector
* `배달, 운반하다`의 의미를 가진 단어가 어원
* 벡터는 크기와 방향을 가짐
* 스칼(scalar)라는 크기만 가짐
* 일반적인 연산에서는 2개이상의 변수를 처리
* 변수 하나하나가 Vector의 element로 표시됨

### Vector의 덧셈
* Element 위치를 대응하는 원소들의 덧셈
```
V = [ v1, v2, v3 ]
U = [ u1, u2, u3 ]

V + U = [v1 + u1, v2 + u2, v3 + u3 ] 
```

### Vecotr 법칙
* 결합 법칙: (u + v) + w = u + (v + w)
* 교환 법칙: u + v = v + u

### Scalar Vector
* a(u+v) = au + av


## Matrix
* Python으로 Matrix(행렬)을 표시하는 다양한 방법이 존재

```
# List로 표현 (2차원 배열)
matrix_list = [[3,6], [4,5]]

# Tuple로 표현
matrix_tuple = [(3, 6), (4, 5)]

# dict로 표현
matrix_dict = { (0, 0): 3, (0, 1): 6, (1, 0): 4, (1, 1): 5}
```

### Matrix Addition
```
matrix_a = [[1, 2], [7, 8]]
matrix_b = [[3, 4], [9, 10]]

result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]

print(result)

[[4, 6], [16, 18]]
```

