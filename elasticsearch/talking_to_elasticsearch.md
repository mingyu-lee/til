# Elasticsearch와 통신

## Java API
자바를 사용하여 Elasticsearch와 통신할 경우, 코드에서 사용할 수 있게 기본 두 개의 클라이언트를 제공한다.

### Node client
`Node client`는 로컬 클러스터를 비 데이터 노드로 결합한다. 데이터 자체는 보관하지 않지만 데이터가 클러스터에서 어떤 노드에 있는지 알고있으며 해당 노드에 직접 요청을 보낼 수 있다.

### Transport client
경량 전송 클라이언트는 원격 클러스터에 요청을 보낼 때 사용할 수 있다. 클러스터 자체가 결합되지 않고 단순히 요청을 클러스터의 노드에 전달한다.


이 두 Java Client는 `Elasticsearch transport protocol`를 사용하여 9300 포트를 통해 클러스터와 통신한다. 클러스터 안의 노드들은 9300 포트를 통해 서로 통신한다. 만약 9300 포트가 열려있지 않다면, 클러스터로부터 노드를 사용할 수 없다.

Java client는 Elasticsearch의 메이저 버전과 같아야한다. 같지 않다면 서로 이해할 수 없다.


## RESTful API
다른 언어들은 RESTful API를 사용하여 9200 포트를 통해 Elasticsearch와 통신할 수 있다. `curl` 명령어를 사용해서 통신할 수도 있다.

Elasticsearch는 여러 언어들의 공식적인 클라이언트를 제공한다. Groovy, JavaScript, .NET, PHP, Perl, Python, Ruby 등이 있다.
[Elasticsearch Clients](https://www.elastic.co/guide/en/elasticsearch/client/index.html)에서 더 자세한 사항을 확인할 수 있다.

Elasticsearch에 대한 요청은 여느 HTTP 요청과 같다.
```
curl -X<VERB> '<PROTOCOL>://<HOST>:<PORT>/<PATH>?<QUERY_STRING>' -d '<BODY>'
```
* VERB: HTTP 메소드 (GET, POST, PUT, HEAD, DELETE)
* PROTOCOL: http 또는 https
* HOST: Elasticsearch 클러스터에 있는 노드의 호스트 이름 또는 로컬 머신의 `localhost`
* PORT: Elasticsearch HTTP 서비스가 실행되고있는 포트 번호 (기본 9200)
* PATH: API 엔드포인트(예를 들어, _count는 클러스터안의 document 갯수를 반환함). Path는 _cluster/stats 또는 _nodes/stats/jvm 과 같이 여러 컴포넌트를 포함할 수 있다.
* QUERY_STRING: 선택적 쿼리 문자열 매개 변수(예: ?pretty는 읽기 쉽도록 JSON 응답을 예쁘게 출력한다)
* BODY: JSON 형태의 요청 본문(요청시 필요한 경우)

예를 들어, 클러스터 안의 document들의 갯수를 알고 싶다면 아래와 같이 요청을 보낸다.

```
# 단순히 요청
curl -XGET 'http://localhost:9200/_count?pretty'

# 파라미터가 필요한 경우
curl -XGET 'http://localhost:9200/_count?pretty' -d '{
    "query": {
        "match_all": {}
    }
}
```

Elasticsearch는 `200 OK`와 같은 HTTP 상태 코드와 (`HEAD` 요청을 제외한) JSON 형태의 응답 본문을 반환한다. 위의 예제와 같은 요청에 대해서는 아래와 같이 응답을 반환한다.

```
{
    "count": 0,
    "_shards": {
        "total": 5,
        "successful": 5,
        "failed": 0
    }
}
```

만약 header에 대한 정보를 보고 싶다면 curl 명령어에 -i 옵션을 추가하면 된다.

```
curl -i -XGET 'localhost:9200/'
```


## 참고
* [Talking to Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/guide/current/_talking_to_elasticsearch.htm)