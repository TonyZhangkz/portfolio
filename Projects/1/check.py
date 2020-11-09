def A(file):    
    start = 0
    end = 0
    line_num=0
    end_list = []
    for line in file:
        line_num+=1
        if (("AFFIRMATIVE COVENANTS" in line) or ( "Affirmative Covenants" in line) or ("Information Covenants" in line))and (line_num>400):
            start = line_num
        if ("NEGATIVE COVENANTS" in line) or ("Negative Covenants" in line)and (line_num>100):
            end = line_num
    j = 0
    l = []
    for line_alt in file:
        j += 1
        if j>=start and j<=end:
            l.append(line_alt.rstrip())
    return(l)

def B(file,mod=3):    
    start = 0
    end = 0
    line_num=0
    end_list = []
    for line in file:
        line_num+=1
        if (("COVENANTS" in line) or ("FINANCIAL INFORMATION" in line) or ( "Affirmative Covenants." in line) or ( "Financial Statements." in line))and (line_num>100):
            start = line_num
        if ((line.strip().startswith("Section")) or (line.strip().startswith("SECTION"))) and (line_num>100):
            end_list.append(line_num)
    for i in range(len(end_list)):
            if end_list[i] >start:
                end = end_list[i+mod]
                break
    l = []
    j = 0
    for line_alt in file:
        j += 1
        if j>=start and j<=end:
            l.append(line_alt.rstrip())
    return(l)

def C(file,mod=10):
    start = 0
    end = 0
    line_num=0
    end_list = []
    for line in file:
        line_num+=1
        if ("Reporting Requirements" in line) or ("REPORTING REQUIREMENTS" in line)  or ("FINANCIAL STATEMENTS" in line) and (line_num>400):
            start = line_num
        if ("SECTION" in line) or ("Section" in line) and (line_num>400):
            end_list.append(line_num)
    for i in range(len(end_list)):
            if end_list[i] >start:
                end = end_list[i+mod]
                break
    l = []
    j = 0
    for line_alt in file:
        j += 1
        if j>=start and j<=end:
            l.append(line_alt.rstrip())
    return(l)

def D(file,mod=400):
    search = input("Please type in the search keyword")
    start = 0
    line_num = 0
    for line in file:
        line_num+=1
        if ((search in line) or (search.upper() in line)) and (line_num>400):
            start = line_num
    end = start+mod
    j = 0
    l = []
    for line_alt in file:
        j += 1
        if j>=start and j<=end:
            l.append(line_alt.rstrip())
    return(l)

    
def P(listed):
    key_list_1 = ["project","budget","forecast","anticipat","pro forma"," plan ","Project","Budget","Forecast"]
    key_list_2 = ["month"]
    for word in key_list_1:
        print(word[0:2],any(word in ele for ele in listed))
    print("mo",any(i == True for i in [any(word in ele for ele in listed) for word in key_list_2]))
    return(None)

def X(listed_file):
    for line in listed_file:
        print(line)

def whole(file):
    l = []
    for line in file:
        l.append(line)
    return(l)

def head(file):
    i = 0
    for line in file:
        i += 1
        print(line.rstrip())
        if i>300:
            break
