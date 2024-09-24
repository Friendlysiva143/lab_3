em_details={
    "name":["sk","pk","ck","vk","dk"],
    "ages":[18,19,21,16,20],
    "salary":[23000,25000,24000,20000,26000]
}
m=[]
for k,v in em_details.items():
    if k=="salary":
        print(min(v))
        print(max(v))
        x=v.index(max(v))
        print(sum(v))
        for i in v:
            if i>23000:
                m.append(v.index(i))
for i,j in em_details.items():
    if i=="name":
        print(j[x])
        for c in m:
            print(j[c])
        
    
    
