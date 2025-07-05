##getcwd 

import os 
# print(os.getcwd())
#mkdir
#mkdirs  -->nested directories 
#chdir 
#rmdir 
#removedirs 
#listdir -[] 
#rename



# print(os.path.exists("C:\my_files\Batch\\37R\python_classes\day_7\\test.py")) ##\tab space
# print(os.path.exists("C:\my_files\Batch\\37R\python_classes\day_7\\new.py")) ##\n new line


# print(os.path.isfile("C:\my_files\Batch\\37R\python_classes\day_7"))

# base_path="C:\my_files\Batch\\37R\python_classes"
# user_inp=input("enter the folder(day_1): ")
# cur_path=os.path.join(base_path,user_inp)

# if os.path.exists(cur_path):
#    os.chdir(cur_path)
#    print(os.getcwd())
# else:
#     print("folder does not exist")

# print(os.path.basename("C:\my_files\Batch\\37R\python_classes"))

# print(os.path.abspath("os.py")) 
# print(os.path.abspath("new.py")) 
# print(os.path.abspath("../day_6/sample.txt"))

#run time environment
# .env

# for i in os.environ:
#     print(i)

# print(os.getenv("path"))


##task running in the system  -- process
# print(os.getpid())
# print(os.getppid())
# print(os.name)
# print(os.getlogin())
# print(os.times())