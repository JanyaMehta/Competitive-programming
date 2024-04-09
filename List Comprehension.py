if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
    list=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in 
    range(z+1) if i+j+k !=n ]
    
    print(list)
    
   #In Python, the interpreter determines the scope of each loop in a list comprehension based on the order of the loops. The loop that appears first in the list comprehension expression is considered to be at the outermost level, and subsequent loops are nested within it.