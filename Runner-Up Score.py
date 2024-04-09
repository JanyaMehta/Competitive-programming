if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr= list(set(arr))# remove duplicates
    arr.sort() # Sort the list of unique elements
    print(arr[-2])
    #set() method is used to convert an iterable to a sequence with unique elements in Python, 
