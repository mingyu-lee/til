# Elasticsearch
* 분산형 RESTful 검색 및 분석 엔진
* [Elastic Stack](https://www.elastic.co/)의 핵심
* 데이터를 중심부에 저장하여 예상되는 항목을 검색
* 예상치 못한 항목을 발견
* [Elasticsearch](https://www.elastic.co/kr/products/elasticsearch)

## 구조
* Index
* Type
* Document
* Field
* Mapping

| Elasticsearch  |Relational DB|
|---|---|
|Index|Database|
|Type|Table|
|Document|Row|
|Field|Column|
|Mapping|Schema|

## CRUD

| Elasticsearch | Relational DB | CRUD   |
|---------------|---------------|--------|
| POST          | INSERT        | Create |
| GET           | SELECT        | Read   |
| PUT           | UPDATE        | Update |
| DELETE        | DELETE        | Delete |

* POST(등록)
   * curl -XPOST localhost:9200/users/user/1 -d '{xxx}'
   * insert into user values ( xxx )
* GET(조회)
   * curl -XGET localhost:9200/users/user/1
   * select * from user where id = 1
* PUT(수정)
   * curl -XPUT localhost:9200/users/user/1 -d '{xxx}'
   * update user set xxx where id = 1
* DELETE(삭제)
   * curl -XDELETE localhost:9200/users/user/1
   * delete from user where id = 1
* 접미어로 ?pretty를 붙이면 결과를 정렬된 JSON Format을 수 있음
* -d @파일명 명령어를 통해 파일로 데이터 핸들링 가능

