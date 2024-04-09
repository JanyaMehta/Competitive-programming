if __name__ == '__main__':
    name_list=[]  # to append names to this list
    score_list=[] # to append scores to this list
    records=[]     # to append both names and scores to this list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])  #doing append thing
        name_list.append(name)
        score_list.append(score)
     
    # removing duplicates and sorting in score_list to find second_low    
    score_list= list(set(score_list)) 
    score_list.sort()
    second_low=score_list[1]
    
    #list comprehension used
    # i[0] (in record which  is name), i.e names in output list print
    # only when i[1] (in record which is score)
    # is equal to second_low ]    
    
    output= [i[0] for i in records if i[1]==second_low]
    output.sort()
    for i in output:
        print(i)
        
