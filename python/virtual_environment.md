# 가상환경
* 프로젝트 진행시 필요한 패키지만 설치하는 환경
* 기본 인터프리터 + 프로젝트 종류별 패키지 설치
* 다양한 패키지 관리 도구를 사용함

## 종류
* virtualenv: 가장 대표적인 가상환경 관리 도구(레퍼런스+패키지 개수)
* conda: 상용 가상환경 도구

### conda 사용
* 참고: [Conda 공식 사이트](https://conda.io)
* 가상환경 만들기
```
conda create  -n my_project python=3.4

activate my_project

(my_project) D:\workspace\12. python> …

```

* 패키지 설치
```
conda install <패키지명>

conda install jupyter

# 웹으로 파이썬 환경 구동 가능
jupyter notebook

```


* ipykernel (jupyter 인스톨 후)
```
# IPython 커널
python -m ipykernel install --user

```
* ipykernel 설치후 atom 에디터에서 hydrogen 사용 가능
* hydrogen : atom 에디터 플러그인으로 실시간으로 코드 결과를 확인 가능


