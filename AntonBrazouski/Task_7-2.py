from contextlib import contextmanager 



@contextmanager
def file_opener(afile): 
    print('enter')
    print(afile)
    file_object = None
    try:
        file_object = open(afile, 'r')
    
        print(file_object.read())

        

    except FileNotFoundError:
        print('not found')

    finally:
        yield
        
        print('exit')
        file_object.close()

    


    

    


with file_opener('file_path') as manager:
    print('with')

