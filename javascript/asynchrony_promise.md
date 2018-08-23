# 자바스크립트 비동기

## 목차
1. [들어가며](#1-들어가며)
2. [자바스크립트에서 비동기란?](#2-자바스크립트에서-비동기란)
3. [Promise](#3-promise)

## 1. 들어가며
백엔드 개발자이지만 프론트엔드 개발자/퍼블리셔가 없어서 풀스택으로 업무를 진행하고 있다.
간단한 페이지 수정, CSS 수정도 하지만 주로 자바스크립트를 통해 프론트단 로직을 작성하는 일이 많다.
모놀리틱 애플리케이션이라 Spring + JSP 템플릿 구조에 jQuery를 사용 중이다.

최근에는 vue.js를 라이브러리 형태로 사용하며 jQuery로 하기엔 귀찮고 불편한 부분들을 vue로 대체하고 있다.
그 중 대부분은 서버에 API를 호출하고 JSON으로 결과를 받아오면, 리스트를 뿌리거나 동적으로 화면을 구현하는 일이다.
비동기로 API 호출 시 jQuery의 $.ajax를 주로 사용했는데, 콜백헬에 빠지는 문제를 해결하려다보니 promise에 대해서 알게되었다.

이번 글에서는 자바스크립트 콜백헬 문제와 이를 해결하기 위해 ES6 표준인 Promise에 대해 알아보려고 한다.


## 2. 자바스크립트에서 비동기란?
비동기(Asynchrony)라는 용어는 컴퓨터 프로그래밍에서 메인 프로그램의 플로우에 독립적인 이벤트의 발생과 그러한 이벤트들을 다루는 방법을 의미한다.
하나의 프로그램은 메인 프로세스 또는 쓰레드가 있으며 메인 함수로 부터 출발하여 로직의 수행, 함수의 호출 등의 코드 흐름대로 프로그램이 작동된다.
비동기는 새로운 쓰레드 또는 프로세스를 만들어 메인 함수의 흐름과는 병렬적으로 코드를 진행하는 것을 말한다.

하지만 자바스크립트는 단일 쓰레드 기반이고 모든 코드는 순차적으로 실행되므로 병렬적으로 수행할 수 없다. 그래서 자바스크립트에서는 비동기 논-블로킹 I/O 모델을 통해 비동기 프로그래밍을 수행한다.
자바스크립트 작업은 차단되지만 I/O 작업은 차단되지 않는다. I/O 작업은 병렬적으로 Ajax 또는 WebSocket 연결을 통해 데이터를 가져오는 등의 작업을 할 수 있는데, 자바스크립트 코드 실행과 병렬적으로 수행할 수 있다.
그러나 자바스크립트가 작업을 수행하는 것은 아니다.

그럼 누가 수행하는 것인가?
바로 자바스크립트가 동작하는 호스팅 환경이다. 우리가 익히 알고있는 웹브라우저 혹은 Node.js가 JS엔진이 올라가는 호스팅 환경이다.
(최근에는 로봇, IoT 디바이스에도 JS엔진을 올려 자바스크립트가 사용되기도 한다)
여러 호스팅 환경의 공통으로 내장된 메커니즘인 이벤트 루프를 통해 비동기 프로그래밍이 가능해진다.

자바스크립트 엔진과 메모리, 콜스택, 이벤트루프 등에 대해 자세한 내용은 [참고: 자바스크립트는 어떻게 작동하는가? (시리즈연재)](https://engineering.huiseoul.com/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%9E%91%EB%8F%99%ED%95%98%EB%8A%94%EA%B0%80-%EC%97%94%EC%A7%84-%EB%9F%B0%ED%83%80%EC%9E%84-%EC%BD%9C%EC%8A%A4%ED%83%9D-%EA%B0%9C%EA%B4%80-ea47917c8442)을 참조하길 바란다.

웹 브라우저로 예로 들면,

1. JS엔진 내부의 콜스택 영역이 있고, 스택 순서대로 프로그램이 동작
2. AJAX 비동기 코드에서 WebAPI의 AJAX 함수를 호출
   * WebAPI는 웹 브라우저의 내장 API이며 $.ajax 처럼 AJAX를 호출하면 이 API를 사용하는 것이다.
   * 자바스크립트가 수행하는게 아닌, 호스팅 환경이 수행한다는 말이 이 때문이다.
3. WebAPI의 AJAX 작업이 끝나면 결과(콜백)를 이벤트 루프의 콜백큐(이벤트큐)에 넣는다.
4. 콜스택이 비어졌을 때, 이벤트 루프는 작업 결과를 콜백큐에서 콜스택으로 밀어넣는다.
5. 콜스택에서 비동기 작업의 결과가 수행된다. (콜백함수)

### 콜백헬(Callback Hell)
자바스크립트 비동기 작업을 수행하면, 그 결과를 콜백 함수를 통해 받고 결과에 대한 후처리를 한다.

<script async src="//jsfiddle.net/MingyuLee/gj7v2tnz/10/embed/js,html,css,result/dark/"></script>

위의 예제를 보면 처음에 getPosts를 호출 후에 done 부분에서 계속 다음 ajax 요청을 호출하는 것을 볼 수 있다.
done은 jQuery AJAX의 success 콜백 옵션이고 deferred.done()을 참조한다.
[Deferred Object](http://api.jquery.com/category/deferred-object/)를 참고하면, jQuery 1.5에 나온 여러 콜백들을 콜백 큐에 등록할 수 있는 유틸리티 오브젝트이다.
자세한 내용은 jQuery API 공식문서를 참고하길 바란다.

예제는 콜백헬의 진가를 제대로 보여준 코드는 아니다. 더 콜백헬스러운 코드라면, done안에 $.ajax.done($.ajax.done($.ajax.done(...) 이러한 구조가 진짜 콜백헬이다.
이렇게 콜백헬임에도 불구하고 사용하는 이유는 비동기이므로 앞의 비동기가 완료된 후에 수행해야하는 로직이라면 비동기의 콜백으로 해야된다.
그렇지 않고 단순히 다음 라인에 코딩을 하면 비동기 결과를 받지도 않았는데 JS엔진은 다음 라인의 코드를 수행하므로 아무 의미가 없는 로직이 수행되고 오류가 발생할 수도 있다.


## 3. Promise

비동기 메소드를 연결할 때, 콜백헬은 가독성이 떨어지고 각 중첩된 콜백마다 에러를 체크해줘야 하는 단점이 있다.
또 try-catch 블록 내에서 비동기 함수를 사용할 때 콜백 함수 내의 예러를 캐치하지 못한다는 단점이 있다.
예외가 호출자 방향으로 전파되는데 비동기 함수 호출자는 콜스택에서 이미 사라졌기 때문이다.

이를 보완하기 위해 `Promise`를 사용한다

`Promise`는 비동기식 작업의 최종 완료 또는 실패를 나타내는 객체이다.
```javascript
let promise = new Promise(function(resolve, reject) {
   setTimeout(resolve, 100, 'foo');
});

console.log(promise);
// [object Promise]
```

#### 문법
```
new Promise(function(resolve, reject) { ... });
```
생성자 함수를 통해 인스턴스화한다. 생성자 함수는 비동기 작업을 수행할 성공시 resolve, 실패시 reject 콜백 함수를 인자로 받는다.

#### Promise 상태

`Promise`는 비동기 처리에 대한 세 가지 상태를 갖는다.

|상태|설명|
|------| ------|
|pending(대기)| fulfiled 또는 rejected가 아닌 상태 |
|fulfilled(이행)| promise.then(f)에서 f가 콜되자마자의 상태 |
|rejected(실패)| promise.then(undefined, r)에서 r이 콜되자마자의 상태|

추가적으로 settled, resolve, unresolved라는 표현을 쓰기도 하는데, 각각의 설명은 다음과 같다.

|상태|설명|
|------| ------|
|settled| pending이 아닐 때를 말하며, `Promise`의 상태는 아닌 언어적 편의를 위한 표현이다. |
|resolved| 기본적으로 settled되어 이행(fulfilled)이든 실패(rejected)든 처리가 해소된 상태를 말하며, 연결된 `Promise`가 있을 경우에도 사용되는 용어|
|unresolved| 기본적으로 resolved가 아닌 상태를 말하며, pending인 상황에 사용되는 용어 |


[States and Fates](https://github.com/domenic/promises-unwrapping/blob/master/docs/states-and-fates.md)를 참고하면 정확히 알 수 있다.
앞의 세 가지 상태는 [Promise 표준](https://promisesaplus.com/)의 2.1 Promise States에 명시된 객체의 상태를 나타낸다.
뒤의 세 가지 표현 중 settled는 pending이 아닐 때를 부르기 편하기 위해 사용되는 용어이다.

resolved와 unresolved는 함수가 해결되었냐 안되었냐의 함수의 관점에서 사용되는 용어인 것 같다. (개인적인 추측)

* `Promise` 기본 사용법 및 에러 처리
<script async src="//jsfiddle.net/MingyuLee/ejd4yfxo/17/embed/js,html,css,result/dark/"></script>

마지막 코드를 보면 then 메소드에서 일부러 에러를 발생시켰고, console에서는 catch에서만 에러가 잡힌다.
then 메소드의 두번째 콜백 함수는 비동기 처리 중 에러가 발생하여 reject 함수가 호출된 상태만을 캐치한다.
그러나 catch 메소드를 쓰면 then 메소드 내부에서 발생한 에러도 캐치하므로, 에러 캐치는 catch 메소드를 쓰는게 좋다.

* `Promise` 연결(chain)
<script async src="//jsfiddle.net/MingyuLee/fsx5ue8y/embed/js,html,css,result/dark/"></script>
주의할 점은 then() 메소드 안에 {} 블록에 코딩되어 있다면, return을 해줘야 다음 then()에서 `Promise`를 받을 수 있다.


## 참고
* [Getting to know asynchronous JavaScript: Callbacks, Promises and Async/Await](https://medium.com/codebuddies/getting-to-know-asynchronous-javascript-callbacks-promises-and-async-await-17e0673281ee)
* [MDN Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
* [자바스크립트 Promise 쉽게 이해하기](https://joshua1988.github.io/web-development/javascript/promise-for-beginners/)
* [PoiemaWeb - Promise](https://poiemaweb.com/es6-promise)
* [참고: 자바스크립트는 어떻게 작동하는가? (시리즈연재)](https://engineering.huiseoul.com/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%9E%91%EB%8F%99%ED%95%98%EB%8A%94%EA%B0%80-%EC%97%94%EC%A7%84-%EB%9F%B0%ED%83%80%EC%9E%84-%EC%BD%9C%EC%8A%A4%ED%83%9D-%EA%B0%9C%EA%B4%80-ea47917c8442)

