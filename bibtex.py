def extract_author(simple_author_1):
    list_tokenize_name=simple_author_1.split("and")
    if len(list_tokenize_name)>1:
        authors_list = []
        for tokenize_name in list_tokenize_name:
            splitted=tokenize_name.split(",")
            authors_list.append((splitted[0].strip(),splitted[1].strip()))
        return authors_list
    tokenize_name= simple_author_1.split(",")
    if len(tokenize_name)>1:
        return (tokenize_name[0],tokenize_name[1].strip())
    tokenize_name=simple_author_1.split(" ")
    length_tokenize_name=len(tokenize_name)
    if length_tokenize_name==1:
        return simple_author_1, ""
    elif length_tokenize_name==2:
        return (tokenize_name[1],tokenize_name[0])
    else:
        return (tokenize_name[2],tokenize_name[0]+" "+tokenize_name[1])



