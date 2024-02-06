from typing import List, Dict, Union, TypeVar


def my_mul(data: list) -> float:
    result = 1
    for num in data:
        result = result * num
    return result


# Pseudo types

Data = List[float | int]


def my_mul2(data: Data) -> float:
    result = 1
    for num in data:
        result = result * num
    return result


my_mul2([1, 2, 3])

dict_of_users: Dict[int, str] = {
    1: "Jane",
    2: "Jon"
}

# Unions
Number = Union[float, int]


def add(x: Number, y: Number) -> Number:
    return x + y


# Generics

T = TypeVar("T", int, str, float)


def calculator(x: T, y: T) -> T:
    return x + y


print(calculator(3, 5))
print(calculator("Hello", "World"))
print(calculator(3.5, 1.4))