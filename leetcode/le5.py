# write the function is_anagram
def is_anagram(test, original):
    l1 = []
    l1 [:0] = test
    l2 = []
    l2 [:0] = original
    
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        l1[i] = l1[i].lower()
        l2[i] = l2[i].lower()
    l1.sort()
    l2.sort()
    print(l1)
    print(l2)
    if l1 == l2:
        return True
    else:
        return False
print(is_anagram("jmuSS","suSmj"))