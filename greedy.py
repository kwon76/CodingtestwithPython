#greedy.py
## 그리디 알고리즘 대표 예제 - 거스름돈 ##
n = int(input()) #n = 거슬러 줘야 할 돈
count = 0 #최종 동전 개수

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin
  n %= coin

print(count)