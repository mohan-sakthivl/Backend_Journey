s="aaaabbcccddddffffff"
nodup=[]
for i in s:
    if i not in nodup:
        nodup+=i 
#print(nodup)
        count=0
        for j in s:
            if i == j:
                count+=1
        print(i,":",count)

