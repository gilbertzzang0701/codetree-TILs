# 변수 선언 및 입력
n = int(input())
	
# n칸의 정사각형에 각각 i + 1의 값을 출력합니다.
for i in range(n):
	for j in range(n):
		print(i + 1, end="")
	print()