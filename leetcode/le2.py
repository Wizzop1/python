def get_count(sentence):
    count = 0
    vow = ["a","e","i","o","u"]
    for i in range(len(vow)):
        for letter in sentence:
            if letter == vow[i]:
                count +=1
    return count
print(get_count("abracadabra"))