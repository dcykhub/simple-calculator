# This is a simple calculator in Python, written by dcykhub.

from typing import Callable, NamedTuple


class User_Input(NamedTuple):
    operator: str
    num_1: float
    num_2: float


def switch_case(operator: str) -> Callable[[float, float], float] | None:
    number_from_user_input = result = float

    def plus(num_1: number_from_user_input, num_2: number_from_user_input) -> result:
        return num_1 + num_2

    def minus(num_1: number_from_user_input, num_2: number_from_user_input) -> result:
        return num_1 - num_2

    def multiply(num_1: number_from_user_input, num_2: number_from_user_input) -> result:
        return num_1 * num_2

    def divide(num_1: number_from_user_input, num_2: number_from_user_input) -> result:
        return num_1 / num_2

    match operator:
        case "+":
            return plus
        case "-":
            return minus
        case "*":
            return multiply
        case "/":
            return divide
        case _:
            return None


def get_result(operator_func: Callable[[float, float], float] | None, num_1: float, num_2: float) -> float | None:
    if callable(operator_func):
        try:
            return operator_func(num_1, num_2)
        except ZeroDivisionError:
            return None

def get_user_input() -> User_Input:
    raw_input = input("<<< ").strip().split()
    return User_Input(operator = str(raw_input[1]), num_1 = float(raw_input[0]), num_2 = float(raw_input[2]))

def main() -> None:
    while True:
        user_input = get_user_input()
        operator_func = switch_case(user_input.operator)
        if callable(operator_func):
            print(">>>", get_result(operator_func = operator_func, num_1 = user_input.num_1, num_2 = user_input.num_2))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
