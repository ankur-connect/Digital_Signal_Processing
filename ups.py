def upsampler(A,fact):
    if(fact==2):
        un=[]
        for i in A:
            un.append(i)
            un.append(0)
        yn=[]
        for i in range(len(un)-1):
            yn.append(un[i]+0.5*(un[i-1]+un[i+1]))
        yn.append(un[-2]/2.0)
        
        return yn
    if(fact==3):
        un=[]
        un=[]
        for i in A:
            un.append(i)
            un.append(0)
            un.append(0)
        yn=[]
        for i in range(len(un)-2):
            yn.append(un[i]+0.5*(un[i-1]+un[i+1]))
        yn.append(un[-3]*2/3.0)
        yn.append(un[-3]/3.0)
        return yn
    
def main():
    A=[2,4,2]
    y=upsampler(A,2)
    print(y)


if __name__=='__main__':
    main()