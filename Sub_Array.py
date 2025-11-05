print('-----------------------------')
print('Chack Sub Array Maximum Sum ')
print('-----------------------------\n')
def SubArray():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    l=[0];
    for st in range(len(arr)):
        for end in range(st,len(arr)):
            l.append(sum(arr[st:end+1]))
    print ('This is Max SubArray Number = ',max(l)) 
SubArray()
    
      