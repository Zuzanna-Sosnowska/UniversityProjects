def permutations1(list, perms=[]):
    if len(list) == 0:
        return perms
    else:
        res = []
        for a in list:
            newL = [*list]
            newL.remove(a)
            
            newPerms = []
            if perms == []:
                newPerms = [[a]]
            else:
                newPerms = [perm + [a] for perm in perms]
                
            res += permutations1(newL, newPerms)    

        return res
    
def permutations(list):
    stack = []
    stack.append([])
    n = len(list)
    
    while len(stack) != 0:
        v = stack.pop()
        
        if len(v) == n:
            yield v
        else:
            for i in range(n):
                if list[i] not in v:
                    stack.append(v + [list[i]])
            

for p in permutations([1,2,3]):
    print(p)
    