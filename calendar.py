
import urllib.request
    
def get_individual_courses(course_desc_page):
    '''Returns a list of all the different course descriptions including the 
    course name itself (which is located at the begining of the string). This
    function assumes that the notaion '<P><B>' Denotes a new entry for each
    course and that the words 'DR=sci; BR=5' denote a course entry and not
    the first part of the course.
    
    Arguments:
    Course_desc_page -- HTML link as a string
    '''
    f = urllib.request.urlopen(course_desc_page)
    page = f.read().decode("utf-8")
    f.close()
    lis = page.rsplit('<P><B>')
    for x in lis:
        if 'DR=sci; BR=5' not in x:
            lis.remove(x)
    return lis
    
         
def get_course_details(course_des):
    '''Returns a list of with the course name as the first element and the 
    subsequent course description of only the prerequisites. This function
    assumes that the notation 'Prerequisite:' means that the list of
    prerequisites begins and the ';' notation means the list of prerequisits
    ends.
    Arguments:
    course_des -- str
    '''
    
    course_info = []
    
    course_info.append(course_des[:8])
        
    pos = course_des.find('Prerequisite:')
    
    course_info.append(course_des[(pos + 13):])
    
    pos = course_info[1].find(';')
    
    course_info[1] = course_info[1][:pos]
    
    return course_info

def prereq_str_to_list(prereq_str):
    
    course_options = []
    
    while prereq_str.find("</A>") > 0:
        pos = prereq_str.find("</A>")
        
        course_options.append(prereq_str[pos-8:pos])
        
        if prereq_str[pos+4:pos+5] != ' ':
            course_options.append(prereq_str[pos+4:pos+5])
        prereq_str= prereq_str[pos + 4:]
    return course_options

def expand_one_or(L):
    
    new_course_lists = []
    
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

def remove_duplicates(preq_lis):
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
def build_prerequisite_dict(course_desc_page):
    '''Returns a dictionary of all the courses on the website as the keys and
    all of the possible sets of course prerequisites as the values.
    
    Arguments:
    course_desc_page -- HTML
    '''
    
    prerequisite_dict = {}
    
    #Read in the HTML page
    courses = get_individual_courses(course_desc_page)
   
    
    course_details = [] 
    for course in courses:
        course_details.append(get_course_details(course))
    
    for course_dec in course_details:
        course_dec[1] = prereq_str_to_list(course_dec[1])
        
    for course_description in course_details:
        prerequisite_dict[course_description[0]] = [course_description[1]]
        
    for k in prerequisite_dict.keys():
        tmp = expand_all_ors(prerequisite_dict[k])
        
        tmp = remove_duplicates(tmp)
        
        prerequisite_dict[k] = tmp
    
    return prerequisite_dict


if __name__ == '__main__':
    
    course_desc_page = "http://www.cs.toronto.edu/~guerzhoy/180/assignments/a3/csc_short.htm"

    
    testing = build_prerequisite_dict(course_desc_page)

