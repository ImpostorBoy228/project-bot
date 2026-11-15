import fnmatch
for u in range(0,10**10, 3023):
    if fnmatch.fnmatch(str(u), "1?954*21"):
        print(u)
    
