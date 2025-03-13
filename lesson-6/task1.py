def check(func):
    def wrapper(a, b):
        try:
            if b == 0:
                return "Denominator can't be zero"
            return func(a, b)
        except Exception as e:
            return f"An error occurred: {e}"
    return wrapper

@check
def divide(a, b):
    return a / b

