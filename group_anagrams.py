
def group_anagrams(str):
    res=[]
    map={}
    for word in s:
        key= ''.join(sorted(word))
        if key in map:
            map[key].append(word)
        else:
            map[key] = [word]

    print(list(map.values()))    
    return list(map.values())


s=['eat','tea','ate','abc','cba']
group_anagrams(s)