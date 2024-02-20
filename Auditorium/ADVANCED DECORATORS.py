inputs = eval(input())
# TODO: Create the logging_decorator() function 👇


def logging_decorator(function):

    def wrapper(*args):
        string = f"{args[0]}"
        for n in args[1:]:
            string += f",{n}"
        print(f"You called {function.__name__}({string})")
        print(f"It returned: {function(*args)}")
    return wrapper
# TODO: Use the decorator 👇


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
