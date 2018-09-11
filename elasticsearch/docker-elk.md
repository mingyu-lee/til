# ELK 설치

도커를 기반으로 ELK를 설치해보려고 한다. ELK를 각각 도커 이미지로 설치해도 되지만, Docker Compose로 구성할 것이다.
[docker-elk](https://github.com/deviantony/docker-elk) 를 사용하여 설치해보자

## 사전 준비
* Docker 설치
* Docker Compose 설치
* docker-elk 레포지토리 클론

### 호스트
호스트 OS는 CentOS 7.2 버전을 사용한다.
Docker Engine이 올라가는 호스트 OS에서 Docker와 Docker Compose를 설치해야한다.

#### Dcoker 설치

Docker는 CE(Community Edition)버전과 EE(Enterprise Edition)이 있다. 여기서는 CE 버전을 설치할 것이다.
설치 과정은 공식문서를 참고했으며 패키지 관리자 yum을 이용하여 설치를 진행해보자.
[Install Docker CE on Linux](https://docs.docker.com/install/linux/docker-ce/centos/#install-using-the-repository)

```
# 1. 필요 패키지 설치
$ sudo yum install -y yum-utils device-mapper-persistent-data lvm2

# 2. CentOS용 docker-ce stable 버전 레포지토리 설정
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# 3. DockerCE 설치
$ sudo yum install -y docker-ce

# 4. Docker 시작
$ sudo service docker service

```

#### Docker Compose 설치

Docker Compose는 아래와 같은 절차로 설치하면 되는데, 중간에 1.22.0은 버전명이다.
다른 버전을 설치하려면 [버전 릴리즈](https://github.com/docker/compose/releases)에서 확인후 해당 버전으로 적어주면 된다.

```
# 1. Docker Compose 설치
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 2. 퍼미션 수정
$ sudo chmod +x /usr/local/bin/docker-compose

# 3. 테스트
$ docker-compose --version
```

#### docker-elk repository clone

작업 디렉토리에서 docker-elk git 레포지토리를 clone 한다.

```
$ git clone https://github.com/deviantony/docker-elk#requirements
```

#### SELinux 설정

SELinux가 활성화된 상태라면 다음 설정을 해줘야 한다.
```
$ chcon -R system_u:object_r:admin_home_t:s0 docker-elk/
```

### docker-elk 설정

docker-elk를 clone 받으면 docker-elk 폴더가 생긴다
폴더 구조는 다음와 같다

```
# docker-elk
.
+-- elasticsearch
|    +-- Dockerfile
|    +-- config
|    |    +-- elasticsearch.yml
+-- logstash
|    +-- Dockerfile
|    +-- config
|    |    +-- logstash.yml
|    +-- pipeline
|    |    +-- logstash.conf
+-- kibana
|    +-- Dockerfile
|    +-- config
|    |    +-- kibana.yml
+-- extenseions
|    +-- README.md
|    +-- curator...
|    +-- logspout ...
+-- docker-compose.yml
+-- README.md
+-- LICENSE
```

* Dockerfile: Docker 상에서 동작하는 컨테이너 구성 정보를 저장한 파일이다.
* docker-compose.yml: docker compose에 필요한 설정 파일이다.
   * [docker-elk docker-compose.yml](https://github.com/deviantony/docker-elk/blob/master/docker-compose.yml)

도커에 관련해서는 따로 포스팅을 할 예정이며, 다른 블로그나 책을 통해 금방 익힐 수 있으니 참고하면 된다.
기존에 설정된 docker-compose.yml 그대로 사용해도 테스트하는데 문제는 없다.


### docker-elk 실행

```
# docker-compose.yml이 있는 디렉토리에서 수행해야 한다
# build
$ docker-compose build

# 빌드를 통해 생성된 도커 이미지 확인
$ docker images

# up: 컨테이너 생성 및 구동, -d는 백그라운드로 실행 옵션
$ docker-compose up -d

# 컨테이너 목록 확인
$ docker-compose ps

# 컨테이너 로그 확인
$ docker-compose logs -f

# elasticsearch 인덱스 확인
$ curl -XGET localhost:9200/_cat/indices?v
```

컨테이너 목록 확인에 정상적으로 컨테이너 3개(elasticsearch, logstash, kibana)가 보이고, 로그에서도 문제가 없으면 정상적으로 작동된 것이다.
브라우저에서 localhost:5601로 접속하면 kibana 웹 UI 화면이 뜰 것이다.
아직은 elasticsearch에 데이터가 없기 때문에 볼 수 있는 데이터는 없다.

`Logstash`는 웹서버(Apache HTTP server, Nginx 등)의 access.log나 WAS의 로그, 애플리케이션 로그, DB 로그, JDBC, 웹소켓, 트위터 등 다양한 입력자원을 읽어들일 수 있고 elasticsearch에 데이터를 보내 kibana에서 시각화하여 확인할 수 있다.



