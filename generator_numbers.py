import re


txt = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
PATTERN = "\\d+\\.\\d{2}"


def generator_numbers(t: str):
    while True:
        match = re.search(PATTERN, t)
        if not match:
            break
        yield match.group(0)
        t = t[match.end():]


def sum_profit(text: str, func: callable):
    s = 0
    for n in generator_numbers(text):
        print(n)
        s = s + float(n)
    return s


def main():
    print(f"Загальний дохід: {sum_profit(txt, generator_numbers)}")


if __name__ == '__main__':
    main()
