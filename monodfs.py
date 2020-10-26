# Xingjian Wang
# ID: 971063330
# October 24, 2020
# CS 441-HW1

import time

def distribution(opNum):
    nSum=[]
    
    #There is no monopole for the two values, 
    #so first assign two values to room.
    room=[opNum[0]]
    opNum.pop(0)
    if(len(opNum)>=1):
        room.append(opNum[0])
        opNum.pop(0)
        nSum.append(room[0]+room[1])
    else:
        return room, opNum
    
    #Store the result of adding each number 
    #in the room to the other numbers in sNum.
    #Then select a number that does not exist in sNum 
    #from opNum and add it to the room.
    i=0
    while True:
        if len(opNum)==0:
            break
        if opNum[i] not in nSum:
            room.append(opNum[i])
            temp=opNum[i]
            opNum.pop(i)
            i=i-1
            for j in range(len(room)-1):
                stemp=temp+room[j]
                if stemp not in nSum:
                    nSum.append(stemp)
                    
        if set(opNum)<set(nSum):
            break
        i=i+1
    return room, opNum

#Add the numbers in each room in pairs 
#and check if the result is stored in this room.
def verification(rooms):
    ver=True
    for i in range(len(rooms)):
        for j in rooms[i]:
            for k in rooms[i]:
                if j!=k and j+k in rooms[i]:
                    ver=False
                    print("ERROR: ")
                    print("In room "+repr(i+1)+": "+repr(j)+"+"+repr(k)+"= "+repr(j+k))
    if ver:
        print("Verified successfully!")

num=int(input("Max num:"))
rNum=int(input("Num of rooms:"))
start=time.perf_counter()
opNum=list(range(1,num+1))  #optional numbers
rooms=[]
for i in range(rNum):
    if len(opNum)==0:
        break
    room,opNum=distribution(opNum)
    rooms.append(room)

#print result
print()
if len(opNum)!=0:
    print("Allocation failed")
for i in range(len(rooms)):
    print("Room"+repr(i+1)+" :")
    print(rooms[i])
if len(opNum)!=0:
    print("Left:")
    print(opNum)

#print result of verification
print()
print("Verification:")
verification(rooms)
end=time.perf_counter()
print('Running time: %s Seconds'%(end-start))