# 문제
# 두 양의 정수가 주어졌을 때, 두 수 사이에 있는 정수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 두 정수 A와 B가 주어진다.

# 출력
# 첫째 줄에 두 수 사이에 있는 수의 개수를 출력한다.

# 둘째 줄에는 두 수 사이에 있는 수를 오름차순으로 출력한다.

import sys


if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().split())

    if a < b:
        c = list(range(a + 1, b))
    else:
        c = list(range(b + 1, a))

    print(c.__len__())
    for i in c:
        if i != c[-1]:
            print(i, end=" ")
        else:
            print(i)
