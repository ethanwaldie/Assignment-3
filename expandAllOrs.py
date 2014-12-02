
lis =[["CSC148H1", "/", "CSC150H1", ",", "CSC165H1", "/", "CSC240H1", "/",
"CSC148H1"]]

def expand_one_or(L):
    
    new_course_lists= []
    
    for lis in L:
        pos = lis.index("/")
        temp1 = lis[:pos] + lis[pos+2:]
        temp2 = lis[:pos-1] + lis[pos+1:]
        
        new_course_lists.append(temp1)
        new_course_lists.append(temp2)
        
    return new_course_lists
        
def expand_all_ors(preq_lis):
    
    if '/' not in preq_lis[0]:
        return preq_lis
    
    
    return expand_all_ors(expand_one_or(preq_lis))

def clean_combine(preq_lis):
    
    for i in range(len(preq_lis)):
        tmp = []
        for course in preq_lis[i]:
            course = course.strip(",")
            if course not in tmp and course != '':
                tmp.append(course)
        preq_lis[i] = tmp
            
    return preq_lis  

def eliminate_duplicates(preq_lis):
    tmp2 = []
    remove_index = []    
    
    for i in range(len(preq_lis)):
            tmp = sorted(preq_lis[i])
            if tmp not in tmp2:
                tmp2.append(tmp)
            else:
                remove_index.append(preq_lis[i])
                
    for e in remove_index:
        pos = preq_lis.index(e)
        del preq_lis[pos]
        
    preq_lis = clean_combine(preq_lis)
    
    return preq_lis