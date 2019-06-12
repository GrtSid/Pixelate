
def dest(a,z,shape,color):
    (x,y)=z
    print (x,y)
    i=0
    f=0
    if ((x==4) & (y==0) & (f==0)):
        x=x-1
        f=f+1
    if ((x==0) & (y==4) & (f==0)):
        y=y+1
        f=f+1
    if ((x==8) & (y==4) & (f==0)):
        y=y-1
        f=f+1
    if ((x==4) & (y==8) & (f==0)):
        x=x+1
        f=f+1
    def short_path(x,y,shape,color,i,f):
        def find(x,y,shape,color,i,f):
            #print (x,y)
            z=(x,y)
            # x=z[0]
            # y=z[1]
            m,n=check_quadrant(z,i)
            #print (m,n)
            if ((x<9) & (y<9) & (x>=0) & (y>=0)):
                if (a[x][y][0:4]==[0,0,x,y]):
                    #print (a[x][y][0:4])
                    b=[x,y,1000]
                    return b
                if ((a[x][y][0:4]==[shape,color,x,y]) & ((i!=0) | (f==1)) ):
                    b=[x,y,i]
                    f=f+1
                    return b
                else:
                    i=i+1
                    #if ((x<8) & (y<8) & (x>=0) & (y>=0)):
                    c=find(x+m,y,shape,color,i,f)
                    d=find(x,y+n,shape,color,i,f)
                    #    e=find(x,y-1,shape,color,i)
                        #print (d)
                    if (c[2]<d[2]):
                        return (c)
                    else:
                        return (d)
            else:
                return ([x,y,1000])
        s=find(x,y,shape,color,i,f)
        return s
    def check_quadrant(z,i):
        x=z[0]
        y=z[1]
        if ((x>=0) & (x<=4) & (y>=0) & (y<4)): #quad1
            m=-1
            n=1
            return m,n
        elif ((x>=4) & (x<=9) & (y>4) & (y<=9)): #quad 3
            m=1
            n=-1
            return m,n
        elif ((x>=0) & (x<4) & (y>=4) & (y<=9)): # quad2
            m=1
            n=1
            return m,n
        elif ((x>4) & (x<=9) & (y>=0) & (y<=4)): #quad4
            m=-1
            n=-1
            return m,n
        else:
            return (-1,-1)

    return (short_path(x,y,shape,color,0,f))
#z=(6,4)
#print (dest(a,z,'square','red'))
