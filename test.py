import os

def testf1():

    print("... en test.py ...")
    path = os.getcwd()
    files = os.listdir(path)
    print(files)

    os.mkdir('folder_testpy')

if __name__ == "__main__":
    
    testf1()