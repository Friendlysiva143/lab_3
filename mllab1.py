em_details={
    "name":["sk","pk","ck","vk","dk"],
    "ages":[18,19,21,16,20],
    "salary":[23000,25000,24000,20000,26000]
}
for k,v in em_details.items():
    if k=="salary":
        print(min(v))
        print(max(v))
print(em_details.name)
