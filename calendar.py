
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
    
    course_info.append(course_des[:8])
    
    pos = course_des.find('Prerequisite:')
    
    course_info.append( course_des[(pos + 13):])
    
    return course_info

def expand_one_or(course_lists):
    
    new_course_lists = []
    
    for lis in course_lists:
        pos = lis.index('/')
        temp1 = lis[:pos] + lis[pos+2:]
        temp2 = lis[:pos-1] + lis[pos+1:]
        
        new_course_lists.append(temp1)
        new_course_lists.append(temp2)
    return new_course_lists


def prereq_str_to_list(prereq_str):
    
    course_options = []
    
    while prereq_str.find("</A>") > 0:
        pos = prereq_str.find("</A>")
        
        course_options.append(prereq_str[pos-8:pos])
        
        if prereq_str[pos+4:pos+5] != ' ':
            course_options.append(prereq_str[pos+4:pos+5])
        prereq_str= prereq_str[pos + 4:]
    return course_options
        
        


if __name__ == '__main__':
    
    course_des = 'CSC209H1"></A> <P><B>CSC209H1<BR>Software Tools and Systems Programming [24L, 12T]</B> <P>Software techniques in a Unix-style environment, using scripting languages and a machine-oriented programming language (typically C). What goes on in the operating system when programs are executed. Core topics: creating and using software tools, pipes and filters, file processing, shell programming, processes, system calls, signals, basic network programming.<BR>Exclusion: <A HREF="crs_csc.htm#CSC372H1">CSC372H1</A>, 408H1, <A HREF="crs_csc.htm#CSC369H1">CSC369H1</A>, 468H1, <A HREF="crs_csc.htm#CSC469H1">CSC469H1</A>.<BR> Prerequisite: <A HREF="crs_csc.htm#CSC207H1">CSC207H1</A>/enrolment in Bioinformatics and Computational Biology (BCB) subject POSt; CGPA 1.5/enrolment in a CSC subject POSt.<BR> DR=SCI; BR=5<BR><HR>'
    
    page = get_course_details(course_des)
    
    test = '<A HREF="crs_csc.htm#CSC148H1">CSC148H1</A>/<A HREF="crs_csc.htm#CSC150H1">CSC150H1</A>, <A HREF="crs_csc.htm#CSC165H1">CSC165H1</A>/<A HREF="crs_csc.htm#CSC240H1">CSC240H1</A>/(<A HREF="crs_csc.htm#CSC148H1">CSC148H1</A> as given before FALL 2003); CGPA 1.5/enrolment in a CSC subject POSt.<BR>'

    prereq_str = prereq_str_to_list(test)
    
    expand_one = expand_one_or([prereq_str])
    
    print(expand_one)
    
    expand_one = expand_one_or(expand_one)
    
    print(expand_one)
    
    expand_one = expand_one_or(expand_one)
    
    print(expand_one)
    
