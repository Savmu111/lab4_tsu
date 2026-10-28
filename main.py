"""Главный модуль демонстрации работы решений Лабораторной работы № 4."""

from func_tools import (
    factorial_reduce,
    filter_even_numbers,
    log_calls,
    memoize,
    repeat_call,
)


@log_calls
def calculate_power(base: int, exponent: int) -> int:
    """Возведение числа в степень для демонстрации логирования."""
    return base ** exponent


@memoize
def tribonacci(n: int) -> int:
    """Последовательность Трибоначчи для демонстрации кэширования."""
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


@repeat_call(iterations=3, tag="DISPATCH")
def send_notification(service: str, status_code: int) -> str:
    """Имитация отправки уведомления для демонстрации декоратора с параметрами."""
    report = f"Служба {service} ответила с кодом {status_code}"
    print(f"   => {report}")
    return report


def main() -> None:
    print("=== Лабораторная работа № 4. Вариант 2 ===\n")

    # 1. Задание 2 (средняя): Фильтрация чётных чисел
    print("--- 1. Задание 2: Фильтрация чётных значений (filter + lambda) ---")
    data_sample = [14, 21, 33, 42, 55, 68, 77, 80, 99, 102]
    even_subset = filter_even_numbers(data_sample)
    print(f"Набор данных: {data_sample}")
    print(f"Только чётные: {even_subset}\n")

    # 2. Задание 4 (средняя): Факториал через reduce
    print("--- 2. Задание 4: Факториал через свертку reduce ---")
    target_val = 7
    print(f"Факториал {target_val}! = {factorial_reduce(target_val)}\n")

    # 3. Задание 7 (средняя): Декоратор логирования
    print("--- 3. Задание 7: Логирование вызова функции ---")
    power_result = calculate_power(3, 4)
    print(f"Итоговый результат: {power_result}\n")

    # 4. Задание 2 (повышенная): Мемоизация через декоратор
    print("--- 4. Задание 2 (повыш.): Мемоизация (Трибоначчи) ---")
    print(f"Первый расчет tribonacci(7) = {tribonacci(7)}")
    print(f"Повторный запрос tribonacci(7) = {tribonacci(7)}\n")

    # 5. Задание 6 (повышенная): Декоратор с параметрами
    print("--- 5. Задание 6 (повыш.): Декоратор с параметрами ---")
    send_notification("AuthService", 200)


if __name__ == "__main__":
    main()