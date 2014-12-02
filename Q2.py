courses = { "A": [ ["B"], ["C"] ],
            "B": [ ["D"], ["E"] ],
            "D": [ ["F"], ["G"] ],
            "C": [ ["H"] ] }

def expand_one_course(req, path):
    print(req)
    
    prereq = []
    
    for i in range(len(req)):
        print(req[i])
        print(req[i][-1])
        if req[i][-1] not in path.keys():
            prereq.append(req[i])
            return prereq
        else:
            for x in range(len(path[req[i][-1]])):
                print(path[req[i][-1]])
                prereq.append(req[i] + path[req[i][-1]][x])
                print(prereq)
    
    return prereq
    
def expand_all_courses(course, path):
    Base = []
    
    for option in course:
        print("option", option[-1])
        if option[-1] not in path.keys():
            Base.append(True)
        else:
            Base.append(False)
    if False not in Base:
        return course
        
    return expand_all_courses(expand_one_course(course, path), path)