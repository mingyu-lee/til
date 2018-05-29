# Search (조회, 검색)
* 모든 document 데이터 조회
```
curl -XGET localhost:9200/basketball/record/_search?pretty

# 결과
{
  "took" : 2,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 2,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "basketball",
        "_type" : "record",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "team" : "Chicago Bulls",
          "name" : "Michael Jordan",
          "points" : 20,
          "rebounds" : 5,
          "assists" : 8,
          "submit_date" : "1996-10-11"
        }
      },
      {
        "_index" : "basketball",
        "_type" : "record",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "team" : "Chicago Bulls",
          "name" : "Michael Jordan",
          "points" : 30,
          "rebounds" : 3,
          "assists" : 4,
          "submit_date" : "1996-10-11"
        }
      }
    ]
  }
}

```

## Option
* q: 질의 `[q=필드명:질의어]`
```
# points == 30 인 것을 조회
curl -XGET 'localhost:9200/basketball/record/_search?q=points:30&pretty'

# 다중 index
curl -XGET 'localhost:9200/basketball, baseball/record/_search?q=points:30&pretty'
```
* df: 매개변수 질의
```
curl -XGET 'localhost:9200/_search/?q=point&df=name
```

## Search Request Body
* 직접 request body를 사용하여 검색
```
curl -XGET localhost:9200/basketball/record/_search -d
'{
	"query": {
		"term": {"points": 30}
	}
}' -H 'Content-Type: application/json'
```

