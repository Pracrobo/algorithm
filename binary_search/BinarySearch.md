# 이진 탐색 , 이분 탐색 , Binary Search
- 책이 일렬로 A-Z 까지 꽂혀있는 목록이 있다면, 쉽고 단순하고 무식한 방법은 하나씩 찾아 보는 것
- 배열 for  문을 돌려서 선형 탐색으로 찾는 것이다.

- 이진 탐색은 정렬된 A-Z 책 목록 중 가운데 "Y"를 뽑았다면, 우리가 찾는 'Romeo and Juliet'은 앞쪽에 있는 것
- 절반씩 봐서 찾는 것 1/2 1/2 1/2
- ex) 술게임 Up & Down


## 주의점
- 정렬이 되어 있어야 탐색을 할 수 있다.
- 살펴 보는 범위를 절반씩 줄여가면서 답을 찾는다.


## 정렬 시간 복잡도 : O(NlogN) 
## 이진 탐색 시간 복잡도 : O(logN) 
###  겷과적으로 이진 탐색  시간 복잡도 : O (NlogN)
### 미리 정렬되어 있는 경우면, 이진 탐색만 하면 되니깐  시간 복잡도 : O(logN)

## 선형 탐색 vs 이진 탐색
### 선형 탐색 시간 복잡도: O(N)
### 이진 탐색의 경우 : N번 이상의 선형 탐색일 경우, 시간 복잡도가 줄어들기 때문에 효윻적

## C++ : lower / upper_bound
- 정렬된 벡터값 vector 의 포인터를 반환, begin(), end(), 값 
- begin() 과 end()의 차이는 [A, B) 이다. 
- upper_bound: 값보다 큰 값을 반환(초과), O(log N)
- lower_bound : 값보다 같거나 큰 값을 반환(이상), O(log N)
- ex) Python range
```c++
vector<int> v = {0(여기가 begin()지점:  index 0) , 1, 3, 3, 6, 6, 6, 7, 8, 8, 9};(여기가 end() 지점) 
int three = upper_bound(v.begin(), v.end(), 3) - lower_bound(v.begin(), v.end(), 3); // upper_bound: index 4 - lower_bound: index 2 = 2
int four = upper_bound(v.begin(), v.end(), 4) - lower_bound(v.begin(), v.end(), 4); // upper_bound: index 4 - lower_bound: index 4 = 0
int six = upper_bound(v.begin(), v.end(), 6) - lower_bound(v.begin(), v.end(), 6); // upper_bound: index 7 - lower_bound: index 4 = 3

printf("number of 3: %d\n", three); // 2
printf("number of 4: %d\n", four); // 0
printf("number of 6: %d\n", six); // 3
```

## Python : bisect_left/right
- `bisect.bisect_left`, `bisect_right` 두개
- c++와 동일한 작동법
```python
from bisect import bisect_left, bisect_right
v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)
three = bisect_right(v, 3) - bisect_left(v, 3)
four = bisect_right(v,4) - bisect_left(v, 4)
six = bisect_right(v, 6) - bisect_left(v, 6)

print(f'nuhmber of 3: {three}') # 2
print(f'nuhmber of 4: {four}') # 0
print(f'nuhmber of 6: {six}') # 3
```







