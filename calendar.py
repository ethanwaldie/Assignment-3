


course_desc_page = "http://www.cs.toronto.edu/~guerzhoy/180/assignments/a3/csc_short.htm"

def get_individual_courses(course_desc_page):
    import urllib.request
    f = urllib.request.urlopen(course_desc_page)
    page = f.read().decode("utf-8")
    f.close()
    print(page)    

course_des = 'CSC209H1"></A> <P><B>CSC209H1<BR>Software Tools and Systems Programming [24L, 12T]</B> <P>Software techniques in a Unix-style environment, using scripting languages and a machine-oriented programming language (typically C). What goes on in the operating system when programs are executed. Core topics: creating and using software tools, pipes and filters, file processing, shell programming, processes, system calls, signals, basic network programming.<BR>Exclusion: <A HREF="crs_csc.htm#CSC372H1">CSC372H1</A>, 408H1, <A HREF="crs_csc.htm#CSC369H1">CSC369H1</A>, 468H1, <A HREF="crs_csc.htm#CSC469H1">CSC469H1</A>.<BR> Prerequisite: <A HREF="crs_csc.htm#CSC207H1">CSC207H1</A>/enrolment in Bioinformatics and Computational Biology (BCB) subject POSt; CGPA 1.5/enrolment in a CSC subject POSt.<BR> DR=SCI; BR=5<BR><HR>' 

def get_course_details(course_des):
    
    course_info = []
    
    course_info.append(course_des[:8])
    
    pos = course_des.find('Prerequisite:')
    
    course_info.append( course_des[(pos + 13):])
    
    return course_info
    

    
    
    
    
    
    
    
    
    


if __name__ == '__main__':
    #get_individual_courses(course_desc_page)
    
    get_course_details(course_des)

    

