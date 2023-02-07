#Day 03
#자료구조

# 평균 구하기 (https://www.acmicpc.net/problem/1546)
# 1. n 과목 수 입력
# 2. mylist에 점수 정보 저장
# 3. mymax에 최댓값 저장
# 4. sum에 모든 데이터 값 더하기

n = int(input())
mylist = list(map(int, input().split()))
print(mylist)
mymax = max(mylist)
sum = sum(mylist)

# mymax = 0
# for score in mylist:
#     if int(score) > mymax:
#         mymax = int(score)

print(sum / mymax / n * 100)