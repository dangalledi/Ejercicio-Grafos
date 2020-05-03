def fix(vec,DIC):
        for i in range(len(DIC)):
            str1 = str(i)
            str2 = DIC[i]
            print(str1,str2)
            vec = vec.replace(str1,str2)
        v = vec.replace(' ','')#[(1,2,4),(2,3,5)]
        v = v.replace('[(','')#1,2,4),(2,3,5)]
        v= v.replace(')]','')#1,2,4),(2,3,5
        v= v.replace('),(',':')#1,2,4:2,3,5
        v = v.split(":")#['1,2,4', '2,3,5']

        n = []
        t = []
        for i in v: #['1,2,4', '2,3,5']
            c = i.split(",")#['1','2','4']
            for x in c:#'1'
                n.append(x)#str -> int
            t.append(tuple(n)) #t = [1,2,4.0]
            n = []
        return t

def fix2(vec):
        v = vec.replace(' ','')#[(1,2,4),(2,3,5)]
        v = v.replace('[(','')#1,2,4),(2,3,5)]
        v= v.replace(')]','')#1,2,4),(2,3,5
        v= v.replace('),(',':')#1,2,4:2,3,5
        v = v.split(":")#['1,2,4', '2,3,5']

        n = []
        t = []
        for i in v: #['1,2,4', '2,3,5']
            c = i.split(",")#['1','2','4']
            for x in c:#'1'
                n.append(int(x))#str -> int
            t.append(tuple(n)) #t = [1,2,4.0]
            n = []
        return t