import collections
#To identify each group, compute the modulo 26 difference between each letter in a word with the first letter in it.
def groupStrings(strings):
    groups = collections.defaultdict(list)
    for s in strings:
        key = [(ord(c) - ord(s[0]))% 26 for c in s]
        groups[tuple(key)].append(s)
    return groups.values()#if sorrted reqd return sorted
    # return map(sorted, groups.values())
print groupStrings(["abc","bcd","acef", "xyz", "az", "ba", "a", "z"])