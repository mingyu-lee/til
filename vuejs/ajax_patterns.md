# AJAX Patterns
* Vue에서 AJAX를 사용하는 가장 좋은 방법에 대해서는 개발자들 사이에서도 의견이 갈린다.
* 그 중 4가지의 디자인 패턴을 소개하며, 각각의 장단점을 알고 상황에 맞게 쓸 수 있어야 한다.
* AJAX Design Patterns in Vue.js
   1. Root instance
   2. Components
   3. Vuex ations
   4. Route navigation guards

---

## 1. Root instance
* 이 아키텍쳐에서는 root instance로부터 모든 AJAX 요청이 보내지고 모든 상태가 저장된다.
* 다른 하위 컴포넌트들이 data를 필요로 한다면, props를 통해 전달한다.
* 하위 컴포넌트들이 data 최신화를 원하면, 커스텀 이벤트를 통해 root instacne의 AJAX 요청을 호출한다.

* 예제
```
new Vue({
  data: {
    message: ''
  },
  methods: {
    refreshMessage(resource) {
      this.$http.get('/message').then((response) {
        this.message = response.data.message;
      });
    }
  }
})

Vue.component('sub-component', {
  template: '<div>{{ message }}</div>',
  props: [ 'message' ]
  methods: {
    refreshMessage() {
      this.$emit('refreshMessage');
    }
  }
});
```

### 장점
* 모든 AJAX 로직과 data를 한 곳에서 관리할 수 있다.
* 모든 컴포넌트들이 프레젠테이션에 집중할 수 있다.

### 단점
* 많은 props와 커스텀 이벤트가 필요하면서 앱의 크기가 커진다.

---

## 2. Components
* 이 아키텍쳐에서는 컴포넌트 별로 AJAX 요청과 상태를 독립적으로 관리한다.
* 일반적으로 컨테이너 역할을 하는 컴포넌트가 data를 관리하고 하위 컴포넌트들을 프레젠테이션에 집중시킨다.

* 예제
```
let mixin = {
  methods: {
    callAJAX(resource) {
      ...
    }
  }
}

Vue.component('container-comp', {
  // No meaningful template, I just manage data for my children
  template: '<div><presentation-comp :mydata="mydata"></presentation-comp></div>', 
  mixins: [ myMixin ],
  data() {
    return { ... }
  },

})

Vue.component('presentation-comp', {
  template: <div>I just show stuff like {{ mydata }}</div>,
  props: [ 'mydata' ]
})
```

### 장점
* 컴포넌트 결합도를 낮추고 재활용성을 높인다.
* data를 필요할 때 얻을 수 있다.

### 단점
* 다른 컴포넌트들과 data를 주고받기 쉽지 않다.
* 컴포넌트가 너무 많은 책임을 가지게 되거나 기능적 중복이 발생할 수 있다.

---

## 3. Vuex actions
* 이 아키텍쳐에서는 AJAX 로직과 상태를 Vuex Store에서 관리할 수 있다.
* 컴포넌트들은 action을 호출하여 새로운 data를 요청할 수 있다.
* 이 패턴을 구현하는 경우, AJAX요청(예, 로딩 스피너 숨기기, 버튼 재활성화)의 해결에 반응할 수 있도록 액션에서 promise를 반환하는 것이 좋다.

* 예제
```
store = new Vuex.Store({
  state: {
    message: ''
  },
  mutations: {
    updateMessage(state, payload) {
      state.message = payload
    }
  },
  actions: {
    refreshMessage(context) {
      return new Promise((resolve) => {
        this.$http.get('...').then((response) => {
          context.commit('updateMessage', response.data.message);
          resolve();
        });
      });
    }
  }
});

Vue.component('my-component', {
  template: '<div>{{ message }}</div>',
  methods: {
    refreshMessage() {
      this.$store.dispatch('refeshMessage').then(() => {
        // do stuff
      });
    }
  },
  computed: {
    message: { return this.$store.state.message; }
  }
});
```

### 장점
* 추가적인 props와 커스텀 이벤트 없이도 `Root instance` 패턴과 `Components` 패턴의 장점을 모두 가진다.

### 단점
* Vuex를 사용하기 위한 학습비용 등의 오버헤드

---

## 4. Route navigation guards
* 애플리케이션이 여러 페이지로 분할되고 route가 변경되면 해당 페이지와 하위 컴포넌트들에 필요한 모든 데이터를 가져온다.
* 이 방식의 주요 이점은 UI가 굉장히 단순해지는 것이다.
* 만약 컴포넌트들이 독립적으로 data를 가져오면, 컴포넌트 데이터가 임의의 순서로 입력되어 페이지가 예측 불가능하게 재전송된다.

* 예제
```
import axios from 'axios';

router.beforeRouteEnter((to, from, next) => {
  axios.get(`/api${to.path}`).then(({ data }) => {
    next(vm => Object.assign(vm.$data, data))
  });
})
```

### 장점
* UI를 보다 쉽게 예측할 수 있다.

### 단점
* data가 준비될 때가지 페이지가 렌더링 되지 않으므로 전체적으로 느려진다.
* routes를 사용하지 않는다면 도움이 되지 않는다.


# 참고
* [https://vuejsdevelopers.com/2017/08/28/vue-js-ajax-recipes](https://vuejsdevelopers.com/2017/08/28/vue-js-ajax-recipes)