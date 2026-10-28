"""Модуль функционального программирования для Лабораторной работы № 4."""

from functools import reduce, wraps
import operator
from typing import Any, Callable, Dict, List, Tuple


# =====================================================================
# СРЕДНЯЯ СЛОЖНОСТЬ: Задание 2 — Отфильтровать чётные числа из списка
# =====================================================================
def filter_even_numbers(items: List[int]) -> List[int]:
    """Отбирает только чётные целые числа с использованием filter."""
    return list(filter(lambda val: val % 2 == 0, items))


# =====================================================================
# СРЕДНЯЯ СЛОЖНОСТЬ: Задание 4 — Факториал через reduce
# =====================================================================
def factorial_reduce(number: int) -> int:
    """Вычисляет n! через свертку последовательности reduce и operator.mul."""
    if number < 0:
        raise ValueError("Факториал отрицательного числа не определен.")
    if number in (0, 1):
        return 1
    return reduce(operator.mul, range(2, number + 1), 1)


# =====================================================================
# СРЕДНЯЯ СЛОЖНОСТЬ: Задание 7 — Декоратор для логирования вызова функции
# =====================================================================
def log_calls(target: Callable) -> Callable:
    """Декоратор трассировки вызовов с выводом аргументов и возвращаемого значения."""
    @wraps(target)
    def inner(*args: Any, **kwargs: Any) -> Any:
        positional = [str(arg) for arg in args]
        keyword = [f"{k}={v}" for k, v in kwargs.items()]
        params_str = ", ".join(positional + keyword)

        print(f"[TRACE] -> Старт: {target.__name__}({params_str})")
        outcome = target(*args, **kwargs)
        print(f"[TRACE] <- Завершено: {target.__name__} => {outcome}")
        return outcome

    return inner


# =====================================================================
# ПОВЫШЕННАЯ СЛОЖНОСТЬ: Задание 2 — Мемоизация функции через декоратор
# =====================================================================
def memoize(target: Callable) -> Callable:
    """Декоратор кэширования чистых функций с поддержкой args и kwargs."""
    storage: Dict[Tuple[Tuple[Any, ...], Tuple[Tuple[str, Any], ...]], Any] = {}

    @wraps(target)
    def inner(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key in storage:
            print(f"[CACHE HIT] Значение для {target.__name__}{args} получено из памяти")
            return storage[cache_key]

        computed = target(*args, **kwargs)
        storage[cache_key] = computed
        return computed

    return inner


# =====================================================================
# ПОВЫШЕННАЯ СЛОЖНОСТЬ: Задание 6 — Декоратор с параметрами
# =====================================================================
def repeat_call(iterations: int = 2, tag: str = "EXEC") -> Callable:
    """Параметрический декоратор, выполняющий функцию заданное число раз."""
    if iterations < 1:
        raise ValueError("Количество повторений должно быть не меньше 1.")

    def decorator(target: Callable) -> Callable:
        @wraps(target)
        def inner(*args: Any, **kwargs: Any) -> Any:
            result = None
            for step in range(1, iterations + 1):
                print(f"[{tag} {step}/{iterations}] Выполнение {target.__name__}...")
                result = target(*args, **kwargs)
            return result

        return inner

    return decorator