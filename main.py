try:
    from python_test_package import greet, some_global_variable
    print(greet(some_global_variable))
except ModuleNotFoundError as e:
    print(f'Erorr: {e}')
