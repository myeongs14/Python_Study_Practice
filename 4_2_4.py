# 입력과 출력 [문제4] 한줄 구구단
# 사용자로부터 2~9 까지의 숫자중 하나를 입력받아 해당 숫자의 구구단을 한줄로 출력하는 프로그램을 작성하시오.
# 실행 예
# 구구단을 출력할 숫자를 입력하세요(2~9): 2
# 2 4 6 8 10 12 14 16 18
#-------------------------------------------------------------------

num = int(input("구구단을 출력할 숫자를 입력하세요(2~9) :"))
for i in range(1,10):
    print(i * num, end=' ')