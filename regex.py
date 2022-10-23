import re
txt = "What are regular expressions"
x = re.search("^What.*expressions%", txt)
if x:
    print("what")