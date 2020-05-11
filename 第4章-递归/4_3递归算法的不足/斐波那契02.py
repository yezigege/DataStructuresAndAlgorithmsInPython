# 使用线性递归计算第n个斐波那契数


def good_fib(n):
    if n <= 1:
        return n, 0
    else:
        (a, b) = good_fib(n - 1)
        return a + b, a


if __name__ == '__main__':
    print(good_fib(10))
