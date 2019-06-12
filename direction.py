def direction(x,y):
    #print (x,y)
    if ((x==-1) & (y==0)):
        return 'u'
    elif((x==1) & (y==0)):
        return 'd'
    elif((x==0) & (y==1)):
        return 'r'
    elif((x==0) & (y==-1)):
        return 'l'
def string(dir,x,y):
    if(((dir=='u') & (x==0) & (y==1))  |  ((dir=='r') & (x==1) & (y==0)) | ((dir=='d') & (x==0) & (y==-1)) | ((dir=='l') & (x==-1) & (y==0))):  # Condition for right direction
        # error()
        return('r')
        # file=open('string.txt','a')
        # file.write(path)
        # file.close()
    elif(((dir=='u') & (x==0) & (y==-1)) | ((dir=='r') & (x==-1) & (y==0)) | ((dir=='d') & (x==0) & (y==1)) | ((dir=='l') & (x==1) & (y==0))):  # Condition for left direction
        #error()
        return('l')
        # file=open('string.txt','a')
        # file.write(path)
        # file.close()
    elif(((dir=='u') & (x==-1) & (y==0)) | ((dir=='r') & (x==0) & (y==1)) | ((dir=='d') & (x==1) & (y==0)) | ((dir=='l') & (x==0) & (y==-1))):  # Condition for forward direction
        return('f')
        # file=open('string.txt','a')
        # file.write(path)
        # file.close()

# file=open('string.txt','w+')
# file.write('')
# file.close()
points=[[0,3],[0,4],[1,4],[2,4],[2,5],[2,6],[3,6],[4,6],[4,7]]
dir='r'
source=points[0]
path=""
for i in range(len(points)-1): #points is the list of points of the path to be traversed
    # a=points[i][0]
    # b=points[i][1]
    # x=points[i][0]-source[0]
    #
    # y=points[i][1]-source[1]
    # print (y)
    #print (dir)
    # a=points[i+1][0]
    # b=points[i+1][1]
    x=points[i+1][0]-points[i][0]
    y=points[i+1][1]-points[i][1]
    #print (string(dir,x,y))
    path=path+string(dir,x,y)
    dir=direction(x,y)
    # source=points[i]
    file=open('string.txt','w+')
    file.write(path)
    file.close()
    file=open('string.txt','a')
    file.write('0')
    file.close()
