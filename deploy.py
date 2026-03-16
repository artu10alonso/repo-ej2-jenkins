import os

def deployf1():

    print("... en deploy.py ...")
    path = os.getcwd()
    print(path)

    os.mkdir('folder_deploypy')

if __name__ == "__main__":
    
    deployf1()