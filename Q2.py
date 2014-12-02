paths = { "A": [ ["B","C"]],
            "B": [ ["D"], ["E"] ],
            "D": [ ["F"], ["G"] ],
            "C": [ ["H"], ["X"] ] }

def expand_one_course(req, path):
    #print(req)
    
    prereq = []
    
    for i in range(len(req)):
        if req[i][-1] not in path.keys():
            prereq.append(req[i])
        else:
            for x in range(len(path[req[i][-1]])):
                prereq.append(req[i] + path[req[i][-1]][x])
    
    return prereq
    
def expand_all_courses(course, path):
    Base = []

    course = expand_one_course(course, path)
    
    for option in course:
        if option[-1] not in path.keys():
            Base.append(True)
        else:
            Base.append(False)
    
    if False not in Base:
        return course
        
    return expand_all_courses(course, path)


def get_all_paths_to_course(course, path):
    
    options = []
    for prereq in path[course]:
        for item in prereq:
            tmp = []
            if item in path.keys():
                tmp = (expand_all_courses([[item]], path))
                print(tmp)
            
            if len(options) == 0:
                options = tmp
            else:

                tmpath = options[:]
                options = []
                for x in range(len(tmp)):
                    for y in range(len(tmpath)):
                        options.append(tmpath[y] + tmp[x])
                        
            print ("options", options)
    return options
                    