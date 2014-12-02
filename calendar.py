
course_desc_page = "http://www.cs.toronto.edu/~guerzhoy/180/assignments/a3/csc_short.htm"

def get_individual_courses(course_desc_page):
    import urllib.request
    f = urllib.request.urlopen(course_desc_page)
    page = f.read().decode("utf-8")
    f.close()
    lis = page.rsplit('<P><B>')
    for x in lis:
        if 'DR=sci; BR=5' not in x:
            lis.remove(x)
    return lis
    
         
def get_course_details(course_des):
    
    course_info = []
    
    for i in range(len(course_des)):
        
        course_info.append(course_des[:8])
        
        pos = course_des.find('Prerequisite:')
        
        course_info.append( course_des[(pos + 13):])
    
    return course_info



course_lists = [ ["CSC148H1", "/", "CSC150H1", ",", "CSC165H1", "/", "CSC240H1", "/",
"CSC148H1", ";", "/"] ]


def expand_one_or(course_lists):
    
    new_course_lists = []
    
    for lis in course_lists:
        pos = lis.index('/')
        temp1 = lis[:pos] + lis[pos+2:]
        temp2 = lis[:pos-1] + lis[pos+1:]
        
        new_course_lists.append(temp1)
        new_course_lists.append(temp2)
    return new_course_lists


if __name__ == '__main__':
    print (expand_one_or(course_lists))

def prereq_str_to_list(prereq_str):
    
    course_options = []
    
    while prereq_str.find("</A>") > 0:
        pos = prereq_str.find("</A>")
        print (pos)
        
        course_options.append(prereq_str[pos-8:pos])
        
        print(course_options)
        if prereq_str[pos+4:pos+5] != ' ':
            course_options.append(prereq_str[pos+4:pos+5])
        print(course_options)
        prereq_str= prereq_str[pos + 4:]
        
        print(prereq_str)
        
    
    return course_options
        

if __name__ == '__main__':
    

