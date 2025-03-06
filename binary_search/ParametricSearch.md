# Parametric Search 매개변수 탐색
파라메트릭 서치
- 최적화 문제를 결정 문제로 바꿔서 이진 탐색으로 푸는 방법이다.

## Optimization Problem : 최적화 문제
### - 문제 상황을 만족하는 변수의 **최솟값, 최댓값**을 구하는 문제

## Decision Problem : 결정 문제
### - **Yes / No Problem**


## 파라메트릭 서치
###  - 매개변수 Parameter가 주어지면 true or false 가 결정되어야 한다.
###  - 가능한 해의 영역이 연속적이어야 한다. (ex. O - O - O - X - X  - X - X)
###  - 범위를 반씩 줄여가면서 가운데 값이 true인지 false인지 구한다.
###  - 이진 탐색과 똑같은 원리

주로 다른 알고리즘과 섞여 많이 출제된다.
- 파라미터가 주어졌을때 True와 False를 체크해주는 함수를 따로 만들어서 구현
```markdown
f(index) {
    paametric search 알고리즘 주로 나오고
    return T/F
} 
```

