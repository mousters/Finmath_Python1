def split_string(func):
    def wrapper():
        output=func()
        splitted=output.split()
        return splitted
    return wrapper

