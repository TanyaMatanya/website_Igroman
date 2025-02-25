import math

def quadratic_roots(a, b, c):
    """Знайти корені квадратного рівняння ax² + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        return "Комплексні корені"

def is_prime(n):
    """Перевірити, чи число є простим"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """Знайти найбільший спільний дільник двох чисел (алгоритм Евкліда)"""
    while b:
        a, b = b, a % b
    return a

def is_palindrome(n):
    """Перевірити, чи є число паліндромом"""
    return str(n) == str(n)[::-1]

def factorial(n):
    """Знайти факторіал числа"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_perfect(n):
    """Перевірити, чи є число досконалим"""
    if n < 2:
        return False
    sum_divisors = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n

def is_armstrong(n):
    """Перевірити, чи є число Армстронга"""
    num_str = str(n)
    power = len(num_str)
    sum_powers = sum(int(digit) ** power for digit in num_str)
    return sum_powers == n

def find_max(numbers):
    """Знайти найбільше число в списку"""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

def is_leap_year(year):
    """Перевірити, чи є рік високосним"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def sum_digits(n):
    """Обчислити суму цифр числа"""
    return sum(int(digit) for digit in str(abs(n)))

def find_primes(n):
    """Знайти всі прості числа в діапазоні від 1 до N"""
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Приклад використання функцій
if name == "main":
    print("Корені рівняння (a=1, b=5, c=6):", quadratic_roots(1, 5, 6))
    print("Чи 17 просте число?", is_prime(17))
    print("НСД(48, 18):", gcd(48, 18))
    print("Чи 12321 паліндром?", is_palindrome(12321))
    print("Факторіал 5:", factorial(5))
    print("Чи 28 досконале число?", is_perfect(28))
    print("Чи 153 число Армстронга?", is_armstrong(153))
    print("Найбільше число в [1, 5, 3, 9, 2]:", find_max([1, 5, 3, 9, 2]))
    print("Чи 2020 високосний рік?", is_leap_year(2020))
    print("Сума цифр 123:", sum_digits(123))
    print("Прості числа до 20:", find_primes(20))