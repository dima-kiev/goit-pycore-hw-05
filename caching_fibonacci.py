def caching_fibonacci(k):
    cache = dict([(0, 0), (1, 1)])

    def fibonacci(n):
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci(k)


def main():
    print(caching_fibonacci(10))


if __name__ == '__main__':
    main()
