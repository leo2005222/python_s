# 컴퓨터가 생각하는 수를 맞추기
# 기회는 6번
# 6번 이후에는 정답을 출력한다.
import random

q = random.randint(1, 100)
for x in range(1, 7):
    num = int(input("%d번째 예상숫자:" % x))
    if num == q:
        print("정답!")
        break
    if num > q:
        print("DOWN")
    else:
        print("UP")

if num == 6:
    print("정답은 %d이야" % q)

