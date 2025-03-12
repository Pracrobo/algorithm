# Dynamic Programming
- 문제를 쪼개서 작은 문제의 답을 구하고 그걸로 더 큰 문제의 답을 구하는 걸 반복
- 분할 정복과 비슷한 느낌

## 구현 2가지 방법
### Top-down 
- 구현 : 재귀
- 저장방식 : 메모제이션 Memoization
- 한번 구한 답들은 저장해둔다
- 부분 문제들의 답을 한번 구했으면 또구하지 않도록(중복연산 방지) cache에 저장해두고 다음부턴 갖다 쓰는것
- 메모이제이션
- 필요한 부분 문제만 구한다.(Lazy-Evaluation)
- Top-down 방식에서 사용


### Bottom-up
- 구현 : 반복문
- 저장방식 : 타뷸레이션 Tabulation


* 피보나치 수열 Fibonacci 
f(0) = 0
f(1) = 1
f(i+2) = f(i+1) + f(i)