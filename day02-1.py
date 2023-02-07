#Day 03
#자료구조

# 숫자의 합 구하기 (https://www.acmicpc.net/problem/11720)
# 1. n값 받기
# 2. numbers 변수에 list 함수 이용해 숫자를 한 자리씩 나누어 받기
# 3. sum 변수 선언

n = input()

numbers = list(input())

sum = 0
for number in numbers:
    sum += int(number)

print("sum : ",sum)
