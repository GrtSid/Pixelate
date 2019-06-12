from collections import defaultdict
dict={(0,0):'0',(0,1):'1',(0,2):'2',(0,3):'3',(0,4):'4',(0,5):'5',(0,6):'6',(0,7):'7',(0,8):'8',(1,0):'9',(1,1):'10',(1,2):'11',(1,3):'12',(1,4):'13',(1,5):'14',(1,6):'15',
(1,7):'16',(1,8):'17',(2,0):'18',(2,1):'19',(2,2):'20',(2,3):'21',(2,4):'22',(2,5):'23',(2,6):'24',(2,7):'25',(2,8):'26',(3,0):'27',(3,1):'28',(3,2):'29',(3,3):'30',(3,4):'31',(3,5):'32',
(3,6):'33',(3,7):'34',(3,8):'35',(4,0):'36',(4,1):'37',(4,2):'38',(4,3):'39',(4,4):'40',(4,5):'41',(4,6):'42',(4,7):'43',(4,8):'44',(5,0):'45',
(5,1):'46',(5,2):'47',(5,3):'48',(5,4):'49',(5,5):'50',(5,6):'51',(5,7):'52',(5,8):'53',(6,0):'54',(6,1):'55',(6,2):'56',(6,3):'57',(6,4):'58',(6,5):'59',(6,6):'60',(6,7):'61',(6,8):'62',
(7,0):'63',(7,1):'64',(7,2):'65',(7,3):'66',(7,4):'67',(7,5):'68',(7,6):'69',(7,7):'70',(7,8):'71',(8,0):'72',(8,1):'73',(8,2):'74',(8,3):'75',(8,4):'76',(8,5):'77',(8,6):'78',(8,7):'79',(8,8):'80'}
dict1={0:(0,0),1: (0,1) ,2: (0,2) ,3: (0,3) ,4: (0,4) ,5: (0,5) ,6: (0,6) ,7: (0,7) ,8: (0,8) ,9: (1,0) ,10: (1,1) ,11: (1,2) ,12: (1,3) ,13: (1,4) ,14: (1,5) ,15:
 (1,6) ,16: (1,7) ,17: (1,8) ,18: (2,0) ,19: (2,1) ,20: (2,2) ,21: (2,3) ,22: (2,4) ,23: (2,5) ,24: (2,6) ,25: (2,7) ,26: (2,8) ,27: (3,0) ,28: (3,1) ,29: (3,2) ,30: (3,3) ,31: (3,4) ,32:
 (3,5) ,33: (3,6) ,34: (3,7) ,35: (3,8) ,36:(4,0),37: (4,1) ,38: (4,2) ,39: (4,3) ,40: (4,4) ,41: (4,5) ,42: (4,6) ,43: (4,7) ,44: (4,8) ,45:
 (5,0) ,46: (5,1) ,47: (5,2) ,48: (5,3) ,49: (5,4) ,50: (5,5) ,51: (5,6) ,52: (5,7) ,53: (5,8) ,54: (6,0) ,55: (6,1) ,56: (6,2) ,57: (6,3) ,58: (6,4) ,59: (6,5) ,60: (6,6) ,61: (6,7) ,62:
 (6,8) ,63: (7,0) ,64: (7,1) ,65: (7,2) ,66: (7,3) ,67: (7,4) ,68: (7,5) ,69: (7,6) ,70: (7,7) ,71: (7,8) ,72: (8,0) ,73: (8,1) ,74: (8,2) ,75: (8,3) ,76: (8,4) ,77: (8,5) ,78: (8,6) ,79: (8,7) ,80: (8,8) }
def paths(source,destination):
    s=dict[source]
    s=int(s)
    d=dict[destination]
    d=int(d)
    class Graph:
        def __init__(self,vertices):
            self.V=vertices
            self.a=[]
            self.path=[]
            self.graph=defaultdict(list)
        def addEdge(self,u,v):
            self.graph[u].append(v)
        def printAllPathsUtil(self,u,d,visited):
            visited[u]=True
            self.path.append(u)
            #print (self.path)
            if (u==d):
                self.a.append(self.path[:])
                #print (self.path)
            else:
                for i in self.graph[u]:
                    if visited[i]==False:
                        self.printAllPathsUtil(i,d,visited)
            self.path.pop()
            visited[u]= False
        def printAllPaths(self,s,d):
            visited=[False]*(self.V)
            self.printAllPathsUtil(s,d,visited)

    g=Graph(81)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 7)
    g.addEdge(7, 8)
    g.addEdge(8, 17)
    g.addEdge(17, 26)
    g.addEdge(26, 35)
    g.addEdge(35,44)
    g.addEdge(44, 53)
    g.addEdge(53, 62)
    g.addEdge(62, 71)
    g.addEdge(71, 80)
    g.addEdge(80, 79)
    g.addEdge(79, 78)
    g.addEdge(78, 77)
    g.addEdge(77, 76)
    g.addEdge(76, 75)
    g.addEdge(75, 74)
    g.addEdge(74, 73)
    g.addEdge(73, 72)
    g.addEdge(72, 63)
    g.addEdge(63, 54)
    g.addEdge(54, 45)
    g.addEdge(45, 36)
    g.addEdge(36, 27)
    g.addEdge(27, 18)
    g.addEdge(18, 9)
    g.addEdge(9, 0)
    g.addEdge(38, 29)
    g.addEdge(29, 20)
    g.addEdge(20, 21)
    g.addEdge(21, 22)
    g.addEdge(22, 23)
    g.addEdge(23, 24)
    g.addEdge(24, 33)
    g.addEdge(33, 42)
    g.addEdge(42, 51)
    g.addEdge(51, 60)
    g.addEdge(60, 59)
    g.addEdge(59, 58)
    g.addEdge(58, 57)
    g.addEdge(57, 56)
    g.addEdge(56, 47)
    g.addEdge(47, 38)
    g.addEdge(36, 37)
    g.addEdge(37, 38)
    g.addEdge(38, 39)
    g.addEdge(4, 13)
    g.addEdge(13, 22)
    g.addEdge(22, 31)
    g.addEdge(41, 42)
    g.addEdge(43, 44)
    g.addEdge(58, 49)
    g.addEdge(58, 67)
    g.addEdge(67, 76)
    g.addEdge(38, 37)
    g.addEdge(37, 36)
    g.addEdge(58, 67)
    g.addEdge(67, 76)
    g.addEdge(42, 43)
    g.addEdge(43, 44)
    g.addEdge(22, 13)
    g.addEdge(13, 4)
    g.addEdge(76,67)
    g.addEdge(67,58)
    g.addEdge(42,41)
    # s = 3
    # d = 20
    #print (dict[(0,1)])
    #print (dict1[2])
    g.printAllPaths(s, d)
    #print (g.a)
    for i in range(len(g.a)):
        if (i==0):
            min=len(g.a[0])
            li=g.a[0]
        elif (len(g.a[i])>len(g.a[i-1]) and len(g.a[i-1])<len(g.a[0])):
            min=len(g.a[i-1])
            li=g.a[i-1]
        elif ((len(g.a[i-1])>len(g.a[i]) and len(g.a[i])<len(g.a[0]))):
            min=len(g.a[i])
            li=g.a[i]

    l1=[]
    for i in li:
        l1.append((dict1[i]))
    return l1
# so=(6,4)
# de=(4,2)
# print (paths(so,de))
