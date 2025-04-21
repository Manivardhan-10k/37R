# nested loops:
# iterating sequence 

##Start   Stop(-1)   Step
# for number in range(100,0,-1):
#     print("hi",number)

#print 19 table upto 10 multiples 19 X 1= 19
# for mul in range(1,10+1):
#     print(f"19 X {mul} = {19*mul}")


#tables from 1 -10
#multiples from 1 -20 
# count=0
# for table in range(1,11):#1 
#     if table%2==0: 
#      for mul in range(1,21):#1 -   20
#         count+=1
#         print(f"{table} X {mul} = {table*mul}")#1 X 1 = 1  1 X2 =2
#     print(f"end of {table} table")
# print(count)   
    

fe=["html","css","js","bootstrap","react","next"]
be=["python","java","c","django","flask","c","node","c++"]

technologies=["html","java","python","node","css","vuejs","html"] ##[fe,be,be,be,fe]
##iterate the tech list 
#we need to compare the element whether fe or be 
##if matches add fe/be 
# out=[]
# for tech in technologies:
#     if tech in fe:
#         out.append("front-end")
#     elif tech in be:
#         out.append("back-end")
# print(out)
# for index in range(0,len(technologies)): ##
#     if technologies[index] in fe:
#         technologies[index]="front-end"
#     elif technologies[index] in be:
#         technologies[index]="back-end"
#     else:
#         technologies[index]=""
# print(technologies)




# string="we will get back to you" ##sm=we   lg=will
# words=string.split(" ")
# sm=words[0] #we
# lg=words[0] #we
# sm_words=[]
# lg_words=[]
# for word in words: #we 
#     if len(word)<=len(sm):
#         sm_words.append(word)
#         sm=word
#     elif len(word)>=len(lg):
#         lg_words.append(word)
#         lg=word
# print(" ".join(sm_words)," ".join(lg_words))


# fibanocci series: 
# 0 1 1 2 3 5 8 13 21 34 55 89 144 ....
##3rd fibanocci number after 50
a=0 
b=1 
count=0
for i in range(1,101):
    # if i==5000:
    if a>50:
        count+=1
    if count==3:
       print(a)
    c=a+b #1
    a=b 
    b=c