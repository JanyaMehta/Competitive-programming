if __name__ == '__main__':
    N = int(input())
    commands=[]
    for _ in range(N):
        x=input().split()
        if x[0]=="insert":
            commands.insert(int(x[1]),int(x[2]))
        elif x[0]=="print":
            print(commands)
        elif x[0]=="remove":
              commands.remove(int(x[1]))
        elif  x[0]=="append":
              commands.append(int(x[1]))
        elif x[0]=="sort":
              commands.sort()
        elif x[0]=="pop":
              commands.pop()
        elif x[0]=="reverse":
              commands.reverse()
