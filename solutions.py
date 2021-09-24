# Use this file to implement your solutions
def biggest(n):
    big = 0
    for i in range(len(n)):
        if n[i]>big:
            big = n[i]
    return big
def biggest2(n):
    big = [0,0]
    for i in range(len(n)):
        if n[i]>big[0]:
            big.pop(0)
            big.insert(0,n[i])
            big.sort()
    return big
def biggestn(n,m):
    big = [0 for i in range(m)]
    for i in range(len(n)):
        if n[i]>big[0]:
            big.pop(0)
            big.insert(0,n[i])
            big.sort()
    return big




def panagram(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in alpha:
        if i not in s.lower():
            return False
    else:
        return True
panagram('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
