# dictionary: 
# word: meaning 
# word:meaning

# dict 
# it is a datatype that store the data in key value pairs 
# the key should always be a string


#list tuple string
# my_dict={
#     "name":"manivardhan",
#     "mob":98948022338,
#     "emp":True,
#     "skills":["FE","BE","Cloud"],
#     "address":{
#         'drno':75
#     },
#         "mob":123,
#         "nickname":"manivardhan"
# }
# print(my_dict['name'])
# print(my_dict['skills'])
# print(my_dict["mob"])

# print(len(my_dict))
# user_mob=my_dict["mob"]
# print(user_mob)

##get -- to get the value of key 
# print(my_dict.get("address"))

#keys  -- it returns the total keys in dict
# print(type(my_dict.keys()))


#values --- returns the values in a list
# print(my_dict.values())


#items

# print(my_dict.items())

# my_dict["city"]="hyd"
# my_dict["languages"]=["tel","hin","eng"]


#update 
# my_dict.update({"role":"FS developer"})

# my_dict.pop("address")
# my_dict.pop("mob")
# my_dict.pop("nickname")
# my_dict.clear()
# del my_dict


# for i in my_dict:
#     print(my_dict[i])
 



num=[1,2,3,4,5,6,7,8,9,10,-13]
prime=[]
non_prime=[]
#only prime nums are to be added 
for i in range(0,len(num),1): #0 
    number=num[i]  ##1 
    ##we have to check whether number  is prime or not
    fact=0  ## for storing the factors of a number  
    for j in range(1,number+1,1): ##1    
        if number%j==0:
            fact+=1  ##1
    if fact==2:
        prime.append(number) #2 3 5 7 
print(prime)

#create my_details with these keys
# name 
# skills :[]
# languages :[]


