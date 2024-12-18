# 첫 번째 줄에서 원소의 개수 n을 입력 받습니다.
n = int(input())

# 두 번째 줄에서 n개의 원소를 입력 받습니다. 공백을 기준으로 숫자들을 받습니다.
numbers = list(map(int, input().split()))

# 각 숫자의 제곱을 계산하고, 그 결과를 공백을 구분자로 출력합니다.
squared_numbers = [str(num ** 2) for num in numbers]
print(" ".join(squared_numbers))
