def disemvowel(string2):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s
print(disemvowel("This website is for losers LOL!"))