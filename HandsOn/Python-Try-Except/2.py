# try with many exceptions
try:
    print(x)
except NameError:
    print('x is not defined')
except:
    print('something went wrong')