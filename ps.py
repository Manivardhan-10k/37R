num=[[1,2,3,-4,-10,-22],[4,5,6],[7,-8,9,2]]
minimum=[]
##REQ:  to find the least num in each sublist
# 1. we need to iterate the main list
# 2. iterate the sublist
# 3.take first element as a min for comparision 
# 4.if the temp is greater than element ,assign element to temp
# for sub in num:
#       temp= sub[0] #4
#       for val in sub:  #
#             if val<temp: # 1<1  -4<1
#                   temp=val
#       minimum.append(temp)           
# print(minimum)      
            
            

            
    
# print(minimum)



ch_list=[1,"*",2,"*",3,4,"*",6,5,"*"]  ##[1,2,3,4,6,5,"*","*","*","*"]
num=[]
string=[]
# print(str(1).isdigit())
## 48-57

# print()

# for i in ch_list:     
#     if ord(str(i))>=48 and ord(str(i))<=57:
#         num.append(i)
#     else:
#         string.append(i)
# num.extend(string)
# print(num)



# num.sort( reverse=True)
# print(num)


# num=[2,3,1]
# for i in range(len(num)):#0   9
#     for j in range(len(num)):# 
#         if num[j] < num[i]:##
#             print(num[i],num[j])
#             temp=num[i]
#             num[i]=num[j] 
#             num[j]=temp
#             print(num[i],num[j])
# print(num)    

        
# a=10 
# b=20 
# temp=a #10
# a=b#20
# b=temp
# print(a,b)



# string=["hi","hello","hey"]
# string.sort()
# print(string)



num=[2,3,4,5,2,1,3,2]
unq=[]
for i in num:
    if  i not in unq:
        unq.append(i)     
print(unq) 
#[2, 3, 4, 5, 1,"*","*","*"]

#[2, 3, 4, 5,"*",1,"*","*"]


