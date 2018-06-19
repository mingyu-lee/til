# 모듈
* 파이썬의 Module은 .py 파일을 의미
* 같은 폴더에 Module에 해당하는 .py 파일과 사용하는 .py을 저장한 후 import 문을 사용해서 Module 호출

```
# american_age.py
import datetime
from dateutil.parser import parse

def get_american_age(birthday):
  dt = datetime.datetime;
  now = dt.now()
  year = int(now.strftime("%Y"))
  parsed_birthday = parse(birthday)
  isAfter = int(now.strftime("%M%d")) >= int(parsed_birthday.strftime("%M%d"))

  return year - int(parsed_birthday.strftime("%Y")) - int((0 if isAfter else 1))

get_american_age("1989-05-24")
29
```

## Namespace
* 모듈을 호출할 때 범위 정하는 방법
* 모듈 안에는 함수와 클래스 등이 존재 가능
* 필요한 내용만 골라서 호출할 수 있음
* from과 import 키워드를 사용함
```
# Alias 설정하기: 모듈명을 별칭으로 사용
import datetime as dt
date_now = dt.datetime.now()
print(date_now)
2018-06-17 15:42:03.968068

# 모듈에서 특정 함수 또는 클래스만 호출하기
from dateutil.parser import parse
parsed_birthday = parse("1989-05-24")
print(parsed_birthday)
1989-05-24 00:00:00

# 모듈에서 모든 함수 또는 클래스를 호출하기
from dateutil.parser import *
parsed_birthday = parse("1989-05-24")
print(parsed_birthday)
1989-05-24 00:00:00

```

## Built-in Modules
* 파이썬이 기본 제공하는 라이브러리
* 문자처리, 웹, 수학 등 다양한 모듈이 제공됨
* 별다른 조치없이 import 문으로 활용 가능
* (공식 표준 라이브러리 검색)[https://docs.python.org/3/library/]


