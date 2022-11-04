def scope_test():
    
    def do_local():
        spam = "local"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal"
    
    def do_global():
        global spam
        spam = "global"
    spam = "test"
    do_local()
    print("After local assignment: ", spam)
    do_nonlocal()
    print("After nonlocal",spam)
    do_global()
    print("After global",spam)

scope_test()
print("In global scope", spam)