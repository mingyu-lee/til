# 매직 넘버 치환
* 소스 코드에 특정한 숫자(매직 넘버(magic number))를 직접 작성하는 것은 나쁜 코딩 스타일

## 나쁜 예
```
public class MagicNumber {
    public static void main(String[] args) {
        MagicNumber magicNumber = new MagicNumber();
        MagicNumber.Player player = magicNumber.new Player("Hoonmaro");
        // 0은 공격
        player.action(0);
        // 1은 방어
        player.action(1);
    }

    public class Player {

        private String name;

        public Player() {
        }

        public Player(String name) {
            this.name = name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public void action(int command) {
            if (command == 0) {
                attack();
            } else if (command == 1) {
                defence();
            }
        }

        private void attack() {
            System.out.println(this.name + " is going to Attack!!");
        }

        private void defence() {
            System.out.println(this.name + " is going to Defence!!");
        }

    }
}
```

## 나쁜이유
1. 매직 넘버의 의미를 알기 어렵다
   * 0과 1이 무슨 의미인가?
   * COMMAND_ATTACK과 같은 기호 상수를 쓰면 의미를 알기 쉽다
2. 매직 넘버는 수정하기 어렵다
   * 0 또는 1 커맨드 숫자가 변경 될 경우 치환해야 하는데, 만약 많은 곳에서 동일한 커맨드를 쓴다면?
   * 손이 많이 가고, 틀리기 쉽고, 빼먹는 경우가 생길 수도 있다.

## 카탈로그


<table>
  <thead>
    <tr><th align="left"> 이름 </th><th align="left"> 매직 넘버를 기호 상수로 치환 (Replace Magic Number with Symbolic Constant) </th></tr>
  </thead>
  <tbody>
    <tr><td align="left"> 상황 </td><td align="left"> 상수를 사용하고 있음                                                       </td></tr>
    <tr>
        <td align="left"> 문제 </td>
        <td align="left">
            • 매직 넘버는 알기 어려움<br>
            • 매직 넘버가 여러 곳에 있으면 변경하기 어려움
        </td>
    </tr>
    <tr><td align="left"> 해법 </td><td align="left"> 매직 넘버를 기호 상수로 치환함                                             </td></tr>
    <tr>
    <td align="left"> 결과 </td>
        <td align="left">
            <strong>장점</strong><br>
            <span style="padding-left: 10px">• 상수의 의미를 알기 쉬워짐</span><br>
            <span style="padding-left: 10px">• 기호 상수의 값을 변경하면 상수를 사용하는 모든 곳이 변경됨</span><br>
            <strong>단점/주의</strong>
            <span style="padding-left: 10px">• 이해하기 어려운 이름을 사용하면 오해가 생길 수 있음</span><br>
        </td>
    </tr>
    <tr>
        <td align="left">방법</td>
        <td align="left">
            <ol>
                <li>
                    <strong>기호 상수 선언하기</strong>
                    <ul>
                        <li>1. 기호 상수 선언</li>
                        <li>2. 매직 넘버를 기호 상수로 치환</li>
<li>3. 기호 상수에 의존하는 다른 매직 넘버를 찾아서 기호 상수를 사용한 표현식으로 변환</li>
<li>4. 컴파일</li>
                    </ul>
                </li>
                <li>
                    <strong>2. 테스트</strong>
                    <ul>
<li>1. 모든 기호 상수 치환이 끝나면 컴파일해서 테스트</li>
<li>2. 가능하다면 기호 상숫값을 변경한 후 컴파일해서 테스트 |</li>
                    </ul>
                </li>
            </ol>
        </td>
    </tr>
<tr>
<td align="left">
관련 항목
</td>
<td align="left">
• 분류 코드를 클래스로 치환<br>
• 분류 코드를 상태/전략 패턴으로 치환
</td>
</tr>
  </tbody>
</table>


## 리팩토링

### 기호 상수 선언하기
1. 기호 상수 선언
* public static final 클래스 필드 사용
* 또는 enum 사용
* 어떤 클래스 안에서만 사용할 기호 상수를 선언할 경우 private 접근지시자를 사용할 수 있다
```
public static final int COMMAND_ATTACK = 0;
public static final int COMMAND_DEFENCE = 1;
```

2. 매직 넘버를 기호 상수로 치환
* 0, 1과 같은 매직 넘버를 기호 상수로 치환
```
// if (command == 0) {
if (command == COMMAND_ATTACK) {

// else if (command == 1) {
} else if (command == COMMAND_DEFENCE) {


// player.action(0)
// player.aciton(1)
player.action(Player.COMMAND_ATTACK);
player.action(Player.COMMAND_DEFENCE);
```

3. 기호 상수에 의존하는 다른 매직 넘버를 기호 상수를 사용한 표현식으로 변환
* 상수 의존 관계는 상수 사이에 의존 관계가 있어 한 상수의 변경이 다른 상수에게도 영향을 미치는 경우를 말한다.
* 이 때, 표현식으로 의존 관계를 표현해야 한다.
```
// public static final int MAX_INPUT_LENGTH = 100;
// public static final int WOR_ARE_LENGTH = 100 * 2;

public static final int MAX_INPUT_LENGTH = 100;
public static final int WOR_ARE_LENGTH = MAX_INPUT_LENGTH * 2;
```

### 테스트
1. 모든 기호 상수 치환이 끝나면 컴파일해서 테스트
   * 테스트 결과는 리팩토링하기 전과 같아야 한다.

2. 가능하다면 기호 상숫값을 변경한 후 컴팡리해서 테스트
   * 기호 상수의 값을 다른 값으로 변경한 후 테스트하면 빠드린 곳이 없는지 확인할 수 있다.
   * COMMAND_ATTACK 값을 0에서 1000으로 변경해도, 매직 넘버가 없다면 테스트가 성공하지만 매직 넘버가 있다면 테스트가 실패한다.


## 리팩토링 후

```
public class MagicNumber {
    public static void main(String[] args) {
        MagicNumber magicNumber = new MagicNumber();
        MagicNumber.Player player = magicNumber.new Player("Hoonmaro");
        player.action(Player.COMMAND_ATTACK);
        player.action(Player.COMMAND_DEFENCE);
    }

    public class Player {

        public static final int COMMAND_ATTACK = 0;
        public static final int COMMAND_DEFENCE = 1;


        private String name;

        public Player() {
        }

        public Player(String name) {
            this.name = name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public void action(int command) {
            if (command == COMMAND_ATTACK) {
                attack();
            } else if (command == COMMAND_DEFENCE) {
                defence();
            }
        }

        private void attack() {
            System.out.println(this.name + " is going to Attack!!");
        }

        private void defence() {
            System.out.println(this.name + " is going to Defence!!");
        }

    }
}
```
* 기호 상수가 충분한 정보를 제공하므로 주석이 필요 없다.

## 더 나은 리팩토링
* 기호 상수로 만든다고 해도 실제로는 상수 값이므로 매직 넘버를 직접 적어도 문제없이 컴파일 된다.
* 실수가 생길 수 있다.
* 커맨드 클래스 객체를 활용하거나 enum을 활용한다.

### enum 활용
* 자바 5부터 enum을 사용할 수 있다.

```
public class EnumMagicNumber {
    public static void main(String[] args) {
        EnumMagicNumber magicNumber = new EnumMagicNumber();
        Player player = new Player("Hoonmaro");
        player.action(Player.Command.ATTACK);
        player.action(Player.Command.DEFENCE);
    }
}

// Player 클래스 분리
public class Player {

    public enum Command {
        ATTACK,
        DEFENCE
    }

    private String name;

    public Player() {
    }

    public Player(String name) {
        this.name = name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void action(Command command) {
        if (command == Command.ATTACK) {
            attack();
        } else if (command == Command.DEFENCE) {
            defence();
        }
    }

    private void attack() {
        System.out.println(this.name + " is going to Attack!!");
    }

    private void defence() {
        System.out.println(this.name + " is going to Defence!!");
    }

}

```
* 기존 Player Inner 클래스를 분리하였다.
* 증첩 enum 은 암묵적으로 static 클래스 이기 때문에 Inner 클래스 안에 선언할 수 없기 때문이다.
* [Java Language Spec 8.9 Enums](https://docs.oracle.com/javase/specs/jls/se7/html/jls-8.html#jls-8.9) 참고
* enum을 활용하여 직관적으로 의미를 전달 할 수 있다.
* 상수가 아니므로 잘못 사용된 곳에서 컴파일에서 경고가 발생하여 에러를 사전에 방지할 수 있다.

## 기호 상수가 적합하지 않은 경우
* 배열 길이
   * 배열 길이는 배열 객체에 length라는 필드가 있다.
   * 기호 상수가 언제나 올바른 배열길이가 아닐 수도 있다.
* 잘 알려진 값을 대체하는 기호 상수 (오히려 가독성이 떨어짐)

## 바이트 코드에 내장된 상수에 주의
* 필드값이 컴파일할 때 정해지는 상수일 경우 리컴파일시 변경된 값으로 바뀌겠지만,
* 이를 사용하는 다른 클래스에서는 리컴파일 하기 전에 이전 상수 값을 가지고 있으므로 문제가 발생한다.
* 매직 넘버를 치환한 모든 소스코드를 리컴파일 해야 정상 작동 된다.




