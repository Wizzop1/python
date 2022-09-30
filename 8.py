from re import X


def listIntoString(friends):
    str1 =""
    return (str1.join(friends))

friends = [input().split()]

for friend in range(len(friends)):
    if len(friend) == 4:
        friends.append(friend)
print(friends)