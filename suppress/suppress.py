class suppress():
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, self.exc_type):
            return True
        else:
            return False

if __name__ == '__main__':
    with suppress(TypeError):
        print("Hi!")
        print("It's nice to meet you,", name)
        print("Goodbye!")
