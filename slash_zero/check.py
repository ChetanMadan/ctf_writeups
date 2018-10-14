from sys import argv

if len(argv)<2:
        print ("Enter string")
else:
        Flag=False
        damnstr=argv[1]
        for i in range(len(damnstr)-3):
                val=damnstr[i:i+3]
                pos=damnstr[i+3:].find(val)
                if pos !=-1:
                        print (str(i)+":"+str(pos+i+3))
                        Flag=True
                        print (val, damnstr[pos+i+3:pos+i+6])
                        break
        if not Flag:
                print ("No repeat occurance found")