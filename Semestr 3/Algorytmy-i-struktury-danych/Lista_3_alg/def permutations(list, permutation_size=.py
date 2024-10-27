def permutations(list, permutation_size=0, perms=[]):
    if permutation_size == len(list):
        return perms
    else:
        res = []
        for a in list:
            new_perms = [perm + [a] for perm in perms]
            res += permutations(list.pop, permutation_size + 1, new_perms)
        return res
