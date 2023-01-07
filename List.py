if __name__ == '__main__':
    N = int(input())
    ans=[]
    for i in range(N):
        elemnt=input().split()
        if elemnt[0]=="insert":
            ans.insert(int(elemnt[1]),int(elemnt[2]))
        if elemnt[0]=="print":
            print(ans)
        if elemnt[0]=="remove":
            ans.remove(int(elemnt[1]))
        if elemnt[0]=="append":
            ans.append(int(elemnt[1]))
        if elemnt[0]=="sort":
            ans.sort()
        if elemnt[0]=="pop":
            ans.pop()
        if elemnt[0]=="reverse":
            ans.reverse()
        
   
