##modules 

#math 
#random 
# # to generate values randomly
# random 
# randint 
# choice
# choices
# sample 
# shuffle -->mutable sequence (list) 
# uniform 
# randrange(s,s,s)
# randonkbits(1,4,8)


#otp generation 
#guess the number 


#date() -- only deals with dates

# datetime() --date + time  
#apps 

#insta  --> msg     open -   current - time  lastseen 


# import datetime
from datetime import datetime,timedelta


#now()
print(datetime.now())

#2025-07-01 
# 1-7-25

print(datetime.strptime("25/07/01","%y/%m/%d"))
print(datetime.strptime("jul/01/25","%b/%d/%y"))



cur=datetime.now() 
print(cur)
print(cur.strftime("%d/%Y/%B"))
print(cur.strftime("%m/%d/%y"))
print(cur.strftime("%a"))
 
# Y 
# y  
# m - 1 -12
# B 
# b  
# d 1-30 
# A
# a

date="08/08/2025"   #day
d_obj=datetime.strptime(date,"%d/%m/%Y")
print(d_obj.strftime("%a"))


# dt = datetime(2025, 6, 1)
# print(dt)
# print(dt.replace(month=7))
# print(dt.replace(year=2030)) # Changes the year to 2030
# print(dt.replace(month=12, day=25)) # Changes the date to December 25
# print(dt.replace(hour=0, minute=30)) # Changes the time to midnight 



# print(datetime.now().weekday())
# print(datetime(1947,8,15).isoweekday()) 


# print(datetime(2025,7,1 ,9,50) + timedelta(days=10) ) 
# print(datetime(2025,7,1) - timedelta(days=100)) 
# print(datetime.now() + timedelta(hours=12))

# print(datetime.now() + timedelta(days=30,hours=10,minutes=2)) 

# print(datetime.now().isoformat()) 


# print(datetime.now().date()) 


# now()
# timedelta () 
# strptime("","")
# now()
# strftime("")
# replace()
# date() 
# time()


# write a function to return the day of the date


# take input of hours  + 
# your next notification will be in 
