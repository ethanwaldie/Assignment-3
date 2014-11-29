


course_desc_page = "http://www.cs.toronto.edu/~guerzhoy/180/assignments/a3/csc_short.htm"

def get_individual_courses(course_desc_page):
    import urllib.request
    f = urllib.request.urlopen(course_desc_page)
    page = f.read().decode("utf-8")
    f.close()
    print(page)    

if __name__ == '__main__':
    get_individual_courses(course_desc_page)


