# Bulk
* 대량 입력(bulk post)
```
curl -XPOST http://localhost:9200/_bulk?pretty --data-binary @classes.json -H 'Content-Type: application/json'
```

* [classes.json](https://raw.githubusercontent.com/minsuk-heo/BigData/master/ch02/classes.json)