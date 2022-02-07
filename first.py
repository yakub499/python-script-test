import os

Name=os.getenv("Name")
db_name1=os.getenv("db_name")
def test():
    print("This is first python code for test" + Name)
    print(db_name1)
def test2():
    print("this second function")
test()
test2()
    
