# name=input("enter the string to be rotated: ") #ythonp    thonpy   honpyt
# name=[1,2,3,4,5,6,7,8,9,10]
# rotations=int(input("enter the number of rotations: "))
# rotations=rotations%len(name)  #50%7 55%7 6 56%7 0
# print(rotations)
# for i in range(rotations):
#     name=name[1:len(name)]+name[0:1] #[2,3,4,5,6,7,8,9,10] +[1]
#     print(i)
# print(name) 
#develop 
#7
#14
#21 
#28
#35



name="wxyz" 
rotations=3
start=97 
end=122
res=""
for i in range(len(name)):
    char= name[i]  #x y z
    code=ord(char) # 119 120  121    122
    if code+rotations>122:   #120+3  123    125
        rem=end-code   ##122-120   2  122-121  1 122-122 0
        extra=rotations-rem   ##3 -2  1 3-1  2  3-0  3
        res+=chr(start+extra-1)  #97+1-1  97 a  97+2-1 97+1 98 b  97+3-1 97+2 99 c
    else:
        res+=chr(code+rotations) # 119+3  122 z
print(res)