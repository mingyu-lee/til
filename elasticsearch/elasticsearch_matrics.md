# Metric Aggregation

* 집계 프레임워크는 검색 쿼리를 기반으로 집계 된 데이터를 제공한다.
* 데이터의 복잡한 요약을 만들기 위해 작성할 수있는 집계(Aggregations)라고하는 단순한 빌딩 블록을 기반으로한다.
* Document 조합을 통해서 어떠한 값을 도출할 때 사용하는 방법

## 종류
* 평균 (Avg)
* 최대 (Max)
* 최소 (Min)
* 합계 (Sum)
* 통계 집계(Stat)
* 백분위 (Percentiles)
* 카디널리티 (Cardinality)
* 확장 통계(Extended Stats)
* 지리적 경계(Geo Bounds)
* 지중 중심(Geo Centroid)
* 백분위 순위(Percentile Ranks)
* 스크립트 매트릭(Scripted Metric)
* 인기 조회(Top Hits)
* 값의 수(Value Count)



## Example
```
curl -XGET localhost:9200/_search?pretty --data-binary @avg_points_aggs.json -H 'Content-Type: Application/json'

# 결과
{
  "took" : 160,
  "timed_out" : false,
  "_shards" : {
    "total" : 15,
    "successful" : 15,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 27,
    "max_score" : 0.0,
    "hits" : [ ]
  },
  "aggregations" : {
    "avg_score" : {
      "value" : 25.0
    }
  }
}

```
* avg_points_aggs.json [참고](https://raw.githubusercontent.com/minsuk-heo/BigData/master/ch03/avg_points_aggs.json)
```
{
    "size": 0,
    "aggs": {
        "avg_score": {
            "avg": {
                "field": "points"
            }
        }
    }
}

```
