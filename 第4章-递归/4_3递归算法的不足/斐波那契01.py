# 简单递归，造成资源的极大浪费


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(10))
