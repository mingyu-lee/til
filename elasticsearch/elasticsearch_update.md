# UPDATE
* 데이터 삽입 / 수정

## Create Document
```
curl -XPOST http://localhost:9200/users/user/1 -d '
{"name": "Kim Tae Hee", "age": 30}'

# Error
{
  "error" : "Content-Type header [application/x-www-form-urlencoded] is not supported",
  "status" : 406
}

curl -XPOST http://localhost:9200/users/user/1 -d '
{"name": "Kim Tae Hee", "age": 30}' -H 'Content-Type: application/json'

# Check
curl -XGET http://localhost:9200/users/user/1?pretty

{
  "_index" : "users",
  "_type" : "user",
  "_id" : "1",
  "_version" : 1,
  "found" : true,
  "_source" : {
    "name" : "Kim Tae Hee",
    "age" : 30
  }
}
```

## Add Field
* _update 옵션 사용
```
curl -XPOST http://localhost:9200/users/user/1/_update?pretty -d '
{ "doc" : { "birthYear": 1989 } }' -H 'Content-Type: application/json'

# Check
curl -XGET http://localhost:9200/users/user/1?pretty

{
  "_index" : "users",
  "_type" : "user",
  "_id" : "1",
  "_version" : 2,
  "found" : true,
  "_source" : {
    "name" : "Kim Tae Hee",
    "age" : 30,
    "birthYear" : 1989 # 추가
  }
}

```
* users Index의 user Type에서 1번째 Document에  birthYear라는 Field를 추가

## Update Field
```
curl -XPOST http://localhost:9200/users/user/1/_update?pretty -d '
{ "doc" : { "birthYear": 1980} }' -H 'Content-Type: application/json'

# Check
curl -XGET http://localhost:9200/users/user/1?pretty

{
  "_index" : "users",
  "_type" : "user",
  "_id" : "1",
  "_version" : 3,
  "found" : true,
  "_source" : {
    "name" : "Kim Tae Hee",
    "age" : 30,
    "birthYear" : 1980
  }
}

```
* users Index의 user Type에서 1번째 Document에  birthYear Field 값 수정

## Script를 활용한 Update
```
curl -XPOST http://localhost:9200/users/user/1/_update?pretty -d '
{ "script" : "ctx._source.age += 9" }' -H 'Content-Type: application/json'

# Check
curl -XGET http://localhost:9200/users/user/1?pretty

{
  "_index" : "users",
  "_type" : "user",
  "_id" : "1",
  "_version" : 5,
  "found" : true,
  "_source" : {
    "name" : "Kim Tae Hee",
    "age" : 39,
    "birthYear" : 1980
  }
}

```
* users Index의 user Type에서 1번째 Document에  age Field 값 수정 (스크립트 활용)

