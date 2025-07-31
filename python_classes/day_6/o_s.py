# datetime 

# from datetime import datetime,timedelta
# print(datetime.now())
# print(datetime(2023,3,25,10,15,59))
# print(datetime.strptime("2025/Aug/3","%Y/%b/%d"))
# print(datetime.now().strftime("%A"))
# print(datetime.now() - timedelta(days=365))
# date=datetime(2022,1,10)
# print(date)
# updated_date=date.replace(day=15)
# print(updated_date) 





# OS   
import os  
#directory /folder  management 

##cwd --current working directory
print(os.getcwd())
 
 
 ##chdir  --change directory 
# os.chdir("C:\my_files\Batch\\37R\python_classes\day_5") 
# os.chdir("C:\my_files") 

# print(os.getcwd())
##mkdir make directory
# os.mkdir("sample_from_os")
 
# file_list=os.listdir()
# if "data.py" in file_list:
#     print("exists")
# else:
#     print("does not exist")

# mkdir 
# chdir 
# listdir 
# getcwd

# os.makedirs("sample_from_os/outer/inner")


# os.remove("sample_from_os")
# os.remove("system32")


#rmdir  --> remove directory 
# os.rmdir("sample.txt")
# os.removedirs("outer/inner") 
# os.mkdir("oldname")
# os.rename("oldname","newname")


# if not os.path.exists("C:\my_files\Batch\\37R\python_classes\day_7"):
#     os.mkdir("day_7")



# print(os.path.isdir("./sample.txt"))
# print(os.path.isfile("./sample.txt"))
# print(os.path.isfile("./data.py"))
# print(os.path.isdir("C:\my_files\Batch\\37R\python_classes\day_5")) 


# print(os.cpu_count()) ##cpu core count