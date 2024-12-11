def print_pattern(n):
    # 첫 번째 부분 출력
    for i in range(n):
        # 공백 출력
        print(" " * (n - 1 - i), end="")
        # @ 출력
        print(" ".join(["@"] * (i + 1)))
    
    # 두 번째 부분 출력
    for i in range(n - 1):
        # 공백 출력
        print(" " * (i + 1), end="")
        # @ 출력
        print(" ".join(["@"] * (n - 1 - i)))

# 입력 받기
n = int(input())
# 패턴 출력
print_pattern(n)
