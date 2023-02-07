#Day 03
#자료구조

# import sys
# input = sys.stdin.readline

# number = int(input())
# for i in range(number):
#     f, s = map(int, input().split())
#     print(f + s)

# 구간 합 구하기 1 (https://www.acmicpc.net/problem/11659)
# 1. suNo 숫자 개수, quizNo 질의 개수
# 2. numbers 변수에 숫자 데이터 저장
# 3. prefix_sum 합 배열 변수 선언
# 4. temp  변수 선언

import sys
input = sys.stdin.readline
suNo ,quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0
for number in numbers:
    temp += number
    prefix_sum.append(temp)

for no in range(quizNo):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start -1])

