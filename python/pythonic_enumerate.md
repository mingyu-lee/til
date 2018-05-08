# Enumerate
* List의 element를 추출할 때 번호를 붙여서 추출
* 텍스트 마이닝, NLP 처리의 기본이 되는 기법
```
for i, v in enumerate(['one', 'two', 'three']):
	print (i, v)
0 one
1 two
2 three
	
for i, v in enumerate("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus quis sapien accumsan, tristique lectus sed, volutpat diam. Aenean facilisis venenatis pretium. Phasellus at sodales odio, eu vestibulum massa. Ut et pellentesque elit. Integer iaculis feugiat venenatis. Vestibulum mattis eros et nisi elementum, et tincidunt sem hendrerit. Nullam pulvinar magna pharetra nisi tincidunt, quis fringilla urna pretium.".split()):
	print(i, v)
	
0 Lorem
1 ipsum
2 dolor
3 sit
4 amet,
…
53 fringilla
54 urna
55 pretium.

```
