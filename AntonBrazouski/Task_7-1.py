class file_context_manager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('inside enter')

    def __exit__(self, exception_type, exception_value,
                exception_traceback):
        # print(f"self={self}, exception_type={exception_type}")
        print('inside exit')

    def read(self):
        pass


with file_context_manager('filename', 'mode') as f:
    pass
    
    #data = f.read()
