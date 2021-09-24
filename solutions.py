# Use this file to implement your solutions
def biggest(n):
    big = 0
    for i in range(len(n)):
        if n[i]>big:
            big = n[i]
    return big
def biggest2(n):
    big2 = [0,0]
    for i in range(len(n)):
        if n[i]>big2[0]:
            big2.pop(0)
            big2.insert(0,n[i])
            big2.sort()
    return big2
def biggestn(n,m):
    bign = [0 for i in range(m)]
    for i in range(len(n)):
        if n[i]>bign[0]:
            bign.pop(0)
            bign.insert(0,n[i])
            bign.sort()
    return bign
def ffindstring(fname,s):
    sum = 0
    with open(fname) as file:
        for line in file.readlines():
            for i in s.split("\n"):
                if i in line:
                    sum+=1
        if sum >= len(s.split("\n")):
            return True
        else:
            return False
def panagram(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in alpha:
        if i not in s.lower():
            return False
    else:
        return True
def breakdown(amt,denominations):
    ans = {}
    for i,j in denominations.items():
        if amt>=i:
            if amt-(i*j)>=0 and j!=0:
                ans[i]=j
                amt=amt-(i*j)
            else:
                for k in range(1,j):
                    if amt-(i*k)<i and amt-(i*k)>=0:
                        ans[i]=k
                        amt=amt-(i*k)
    if amt==0:
        return ans
    else:
        return "NotAvailable"
