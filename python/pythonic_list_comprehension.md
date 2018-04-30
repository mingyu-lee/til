# List Comprehension
* 기존 List 사용하여 간단히 다른 List를 만드는 기법
* 포괄적인 List, 포함되는 리스트라는 의미로 사용됨
* 파이썬에서 가장 많이 사용되는 기법 중 하나
* 일반적으로 for + append 보다 속도가 빠름


```
# General
result = []
for i in range(10):
   result.append(i)

result
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Pythonic Code List Comprehension
result = [i for i in range(10)]
result
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [i for i in range(10) if i % 2 == 0]
result
[0, 2, 4, 6, 8]

# Nested For Loop를 활용
abc = ['A', 'B', 'C']
numbers = [1, 2, 3, 4, 5]
result = [i + str(j) for i in abc for j in numbers]

result
['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5']

words = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus quis sapien accumsan, tristique lectus sed, volutpat diam. Aenean facilisis venenatis pretium. Phasellus at sodales odio, eu vestibulum massa. Ut et pellentesque elit. Integer iaculis feugiat venenatis. Vestibulum mattis eros et nisi elementum, et tincidunt sem hendrerit. Nullam pulvinar magna pharetra nisi tincidunt, quis fringilla urna pretium.".split()

two_demension_list = [[w.upper(), w.lower(), len(w)] for w in words]

two_demension_list
[['LOREM', 'lorem', 5], ['IPSUM', 'ipsum', 5], ['DOLOR', 'dolor', 5], ['SIT', 'sit', 3], ['AMET,', 'amet,', 5], ['CONSECTETUR', 'consectetur', 11], ['ADIPISCING', 'adipiscing', 10], ['ELIT.', 'elit.', 5], ['VIVAMUS', 'vivamus', 7], ['QUIS', 'quis', 4], ['SAPIEN', 'sapien', 6], ['ACCUMSAN,', 'accumsan,', 9], ['TRISTIQUE', 'tristique', 9], ['LECTUS', 'lectus', 6], ['SED,', 'sed,', 4], ['VOLUTPAT', 'volutpat', 8], ['DIAM.', 'diam.', 5], ['AENEAN', 'aenean', 6], ['FACILISIS', 'facilisis', 9], ['VENENATIS', 'venenatis', 9], ['PRETIUM.', 'pretium.', 8], ['PHASELLUS', 'phasellus', 9], ['AT', 'at', 2], ['SODALES', 'sodales', 7], ['ODIO,', 'odio,', 5], ['EU', 'eu', 2], ['VESTIBULUM', 'vestibulum', 10], ['MASSA.', 'massa.', 6], ['UT', 'ut', 2], ['ET', 'et', 2], ['PELLENTESQUE', 'pellentesque', 12], ['ELIT.', 'elit.', 5], ['INTEGER', 'integer', 7], ['IACULIS', 'iaculis', 7], ['FEUGIAT', 'feugiat', 7], ['VENENATIS.', 'venenatis.', 10], ['VESTIBULUM', 'vestibulum', 10], ['MATTIS', 'mattis', 6], ['EROS', 'eros', 4], ['ET', 'et', 2], ['NISI', 'nisi', 4], ['ELEMENTUM,', 'elementum,', 10], ['ET', 'et', 2], ['TINCIDUNT', 'tincidunt', 9], ['SEM', 'sem', 3], ['HENDRERIT.', 'hendrerit.', 10], ['NULLAM', 'nullam', 6], ['PULVINAR', 'pulvinar', 8], ['MAGNA', 'magna', 5], ['PHARETRA', 'pharetra', 8], ['NISI', 'nisi', 4], ['TINCIDUNT,', 'tincidunt,', 10], ['QUIS', 'quis', 4], ['FRINGILLA', 'fringilla', 9], ['URNA', 'urna', 4], ['PRETIUM.', 'pretium.', 8]]

one_demension_list = [elem for two_elem in two_demension_list for elem in two_elem]

['LOREM', 'lorem', 5, 'IPSUM', 'ipsum', 5, 'DOLOR', 'dolor', 5, 'SIT', 'sit', 3, 'AMET,', 'amet,', 5, 'CONSECTETUR', 'consectetur', 11, 'ADIPISCING', 'adipiscing', 10, 'ELIT.', 'elit.', 5, 'VIVAMUS', 'vivamus', 7, 'QUIS', 'quis', 4, 'SAPIEN', 'sapien', 6, 'ACCUMSAN,', 'accumsan,', 9, 'TRISTIQUE', 'tristique', 9, 'LECTUS', 'lectus', 6, 'SED,', 'sed,', 4, 'VOLUTPAT', 'volutpat', 8, 'DIAM.', 'diam.', 5, 'AENEAN', 'aenean', 6, 'FACILISIS', 'facilisis', 9, 'VENENATIS', 'venenatis', 9, 'PRETIUM.', 'pretium.', 8, 'PHASELLUS', 'phasellus', 9, 'AT', 'at', 2, 'SODALES', 'sodales', 7, 'ODIO,', 'odio,', 5, 'EU', 'eu', 2, 'VESTIBULUM', 'vestibulum', 10, 'MASSA.', 'massa.', 6, 'UT', 'ut', 2, 'ET', 'et', 2, 'PELLENTESQUE', 'pellentesque', 12, 'ELIT.', 'elit.', 5, 'INTEGER', 'integer', 7, 'IACULIS', 'iaculis', 7, 'FEUGIAT', 'feugiat', 7, 'VENENATIS.', 'venenatis.', 10, 'VESTIBULUM', 'vestibulum', 10, 'MATTIS', 'mattis', 6, 'EROS', 'eros', 4, 'ET', 'et', 2, 'NISI', 'nisi', 4, 'ELEMENTUM,', 'elementum,', 10, 'ET', 'et', 2, 'TINCIDUNT', 'tincidunt', 9, 'SEM', 'sem', 3, 'HENDRERIT.', 'hendrerit.', 10, 'NULLAM', 'nullam', 6, 'PULVINAR', 'pulvinar', 8, 'MAGNA', 'magna', 5, 'PHARETRA', 'pharetra', 8, 'NISI', 'nisi', 4, 'TINCIDUNT,', 'tincidunt,', 10, 'QUIS', 'quis', 4, 'FRINGILLA', 'fringilla', 9, 'URNA', 'urna', 4, 'PRETIUM.', 'pretium.', 8]
```

