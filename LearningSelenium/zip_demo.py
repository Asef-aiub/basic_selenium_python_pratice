list1=["bangladesh","india","pakistan","nepal","bhutan"]
list2=["dhaka","delhi","islamabad","kathmandu","thimpu"]
s=zip(list1,list2)
print(list(s))
for x,y in zip(list1,list2):
    print(x,y)

total_cost=[56,55,67]
sale_price=[78,89,90]
for x,y in zip(total_cost,sale_price):
    print(y-x)