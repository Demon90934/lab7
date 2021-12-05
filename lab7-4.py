def inp():
    n = int(input("Введите целое число n>=0:"))
    m = int(input("Введите целое число 0<=m<=n:"))
    return n, m


def c(m, n):
    if (m == 0) or (m == n):  # Если m равно 0 или m равно n, возвращаем 1
        return 1
    else:
        return c(m, n - 1) + c(m - 1, n - 1)


def out(res):
    print(res)


def out_wrong():
    print("Ошибка! Некорректные значения")


""" Основная программа """
n, m = inp()
if (n >= m) and (m >= 0):  # Проверяем условие 0 <= m <= n
    res = c(m, n)
    out(res)
else:
    out_wrong()
