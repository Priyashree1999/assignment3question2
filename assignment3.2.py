def rev_of_string(a):#python
    print("After reversing the string: ",end='')
    for i in range((len(a))-1,-1,-1):
        
        print(a[i],end='')
    
    return a  
    
    
    
n='1234abcd'
print("Before reversing the string: ",n)
rev_of_string(n)

 