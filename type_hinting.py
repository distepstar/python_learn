# Type Hinting
# Python is dynamic type language
# Depending the datatypes in run time

# install mypy for type checking
# pip install mypy
# mypy type_hinting.py

# Typescript like type hinting
# def function_name(parameter: type) -> return_type:
def my_func(my_param: int) -> str:
    return f"{my_param + 10}"


def other_func(other_param: str):
    print(other_param)

# still world cuz python is dynamic type
other_func(my_func(10))

# python 3.9
# def dosth(param: list[int]):