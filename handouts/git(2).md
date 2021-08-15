---
marp: true
---

# git, github

## SSAC

### Python을 활용한 비즈니스 빅데이터 분석가 양성과정

---

<!--
paginate: true
theme: default
size: 16:9
footer : Python을 활용한 비즈니스 빅데이터 분석가 양성과정,  Wooyoung Choi, 2021
-->

## git with ipynb

---

## Pros

- github에 ipynb 파일을 업로드 시 레이아웃 그대로 유지
- md와 함께 작성하면 하나의 완벽한 보고서를 생성할 수 있음

---

## The problem is..

- ipynb 포맷은 blob으로 저장 시 히스토리 추적이 불가

---

## Solutions

1. Clear All outputs and save
2. Convert to python
    ```
    $jupyter nbconvert {filename} --to="python" --output-dir="/dest" --
    output="{filename}"
    ```
3. install github app [ReviewNB](https:www.reviewnb.com/)

---
## Review your code with your mate

---

### Abstract

1. Add your mate(reviewer) to collaborator on settings
2. make branch and do your work.
3. push your code to remote/{your branch}
4. compare & create pull request
5. review and request change or approve
6. merge your pull request

---

## Practice

다음의 문제를 해결하고 리뷰어로부터 승인을 받으세요.
문제 마다 각각 ipynb 파일을 생성하여 진행해야 하며, 리뷰는 총 세번 이루어져야 합니다.

1. fizzbuzz
2. Egyptian division
3. password generator

---

## Solve and merge!

다음의 문제에 대해 코드로 풀어내거나 번역 혹은 설명하는 문서를 만들고 리뷰어에게 승인받으세요.

1. [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
2. [Birthday problem](https://en.wikipedia.org/wiki/Birthday_problem)

<link href="https://fonts.googleapis.com/css?family=Nanum+Gothic:400,800" rel="stylesheet">
<link rel='stylesheet' href='//cdn.jsdelivr.net/npm/hack-font@3.3.0/build/web/hack-subset.css'>

<style>
h1,h2,h3,h4,h5,h6,
p,li, dd, table > * > * {
font-family: 'Nanum Gothic', Gothic;
}
span, pre {
font-family: 'Hack', monospace;
}
</style>