# 입력받은 10개의 정수
numbers = list(map(int, input().split()))

# 짝수 번째 원소들의 합 (인덱스 1, 3, 5, 7, 9)
even_sum = sum(numbers[i] for i in range(1, 10, 2))

# 3의 배수 번째 원소들의 평균 (인덱스 2, 5, 8)
multiples_of_three = [numbers[i] for i in range(2, 10, 3)]
average_of_multiples_of_three = round(sum(multiples_of_three) / len(multiples_of_three), 1)

# 결과 출력
print(even_sum, average_of_multiples_of_three)
