x=[]
s=0
T=int(input())
for n in range(T):
    temp=[]
    lst=[]
    N=int(input())
    cities=list(map(int, input().split()))
    P=int(input())
    for j in range(P):
        lst.append(int(input()))
    for j in range(P):
        ct=0
        for i in range(0,2*N,2):
            if cities[i]>cities[i+1]:
                (cities[i],cities[i+1])=(cities[i+1],cities[i])
            for k in range(cities[i],cities[i+1]+1,1):
                if lst[j]==k:
                    ct=ct+1            
        temp.insert(j,ct)
    x.append(temp)
    print('\n')
for j in x:
    s=s+1
    print('Case #{}:'.format(s),end=' ')
    for l in j:
        print(l,end=' ')
    print()
